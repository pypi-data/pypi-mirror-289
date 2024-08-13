import os
from pathlib import Path
import re
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


from finter.modeling.meta_portfolio.base import (
    BaseMetaPortfolio,
    BaseParameters,
)
from finter.framework_model.submission.helper_submission import submit_model
from finter.settings import logger
from finter.framework_model.portfolio import BasePortfolio
from finter.data import ContentFactory
from finter.backtest.simulator import Simulator
from finter.backtest import USStockBacktestor, VietnamBacktestor
from finter.framework_model.submission.helper_poetry import prepare_docker_submit_files

from typing import Optional
from contextlib import contextmanager
from tempfile import TemporaryDirectory


class RiskParityMetaPortfolio(BaseMetaPortfolio):
    risk: str = ""
    lookback_periods: str = ""
    rebalancing_periods: str = ""

    lookback_period_map = {"3M": 63, "6M": 126, "12M": 252}
    rebalancing_period_map = {"1W": "W", "1M": "M", "1Q": "Q"}

    class Parameters(BaseParameters):
        risk: str
        lookback_periods: str
        rebalancing_periods: str

    # Helper functions
    def daily_return_to_nav(cls, daily_returns):
        def calculate_nav(daily_return):
            # 첫 값이 1로 시작하는 NaV 시리즈 생성
            nav_series = (1 + daily_return).cumprod()
            # 첫 값 1을 시리즈의 시작에 추가
            return nav_series

        return {
            alpha: calculate_nav(daily_returns[alpha]) for alpha in daily_returns.keys()
        }

    def calculate_previous_start_date(cls, start_date, lookback_days):
        start = datetime.strptime(str(start_date), "%Y%m%d")
        previous_start = start - timedelta(days=lookback_days)
        return int(previous_start.strftime("%Y%m%d"))

    def retain_first_of_period(cls, data: pd.Series, period: str) -> pd.Series:
        tmp = data.index[-2:-1].append(data.index[0:-1])
        mask = data.index.to_period(period) != tmp.to_period(period)
        return data[mask]

    def calculate_volatility(cls, ret_dict, alpha_set, lookback_periods):
        return {
            alpha: ret_dict[alpha].rolling(window=lookback_periods).std()
            for alpha in alpha_set
        }

    def calculate_MDD(cls, ret_dict, alpha_set, lookback_periods):
        def calculate_DD(series):
            nav = (1 + series).cumprod()
            dd = pd.Series(nav).cummax() - nav
            return dd.max()

        return {
            alpha: ret_dict[alpha]
            .rolling(window=lookback_periods)
            .apply(lambda x: calculate_DD(x))
            for alpha in alpha_set
        }

    def calculate_TuW(cls, ret_dict, alpha_set, lookback_periods):
        def calculate_tuw(series):
            nav = (1 + series).cumprod()
            dd = pd.Series(nav).cummax() - nav
            return (dd > 0).astype(int).sum()

        return {
            alpha: ret_dict[alpha]
            .rolling(window=lookback_periods)
            .apply(lambda x: calculate_tuw(x))
            for alpha in alpha_set
        }

    def risk_parity_weights(cls, volatilities):
        inv_volatilities = 1 / volatilities
        weights = inv_volatilities / inv_volatilities.sum()
        return weights

    def get_alphas(cls, alpha_loader, alpha_set):
        alpha_dict = {
            alpha: alpha_loader.get_alpha(alpha)
            .replace(0, np.nan)
            .dropna(how="all")
            .dropna(how="all", axis=1)
            .fillna(0)
            for alpha in alpha_set
        }
        ret_columns = set()
        for alpha in alpha_set:
            ret_columns.update(alpha_dict[alpha].columns)
        return alpha_dict, list(ret_columns)

    def get_summary(cls, alpha_dict, close, universe):
        def backtest(alpha, close, universe):
            bt = Simulator(
                alpha.fillna(0),
                close,
                initial_cash=1e8,
                buy_fee_tax=0,
                sell_fee_tax=30,
                slippage=10,
            )
            if universe in ["us_etf", "us_stock"]:
                bt = USStockBacktestor(
                    alpha.fillna(0),
                    close,
                    initial_cash=1e8,
                    buy_fee_tax=0,
                    sell_fee_tax=30,
                    slippage=10,
                )
            elif universe == "vn_stock":
                bt = VietnamBacktestor(
                    alpha.fillna(0),
                    close,
                    initial_cash=1e8,
                    buy_fee_tax=40,
                    sell_fee_tax=50,
                    slippage=10,
                )
            bt.run()
            return bt.summary

        return {
            alpha: backtest(alpha_dict[alpha], close, universe)
            for alpha in alpha_dict.keys()
        }

    def get(cls, start, end):
        cls.lookback_periods = cls.lookback_period_map.get(
            cls.lookback_periods, cls.lookback_periods
        )

        pre_start = cls.calculate_previous_start_date(start, cls.lookback_periods * 4)

        alpha_loader = cls.alpha_loader(pre_start, end)
        alpha_dict, ret_columns = cls.get_alphas(alpha_loader, cls.alpha_set)

        model_info = cls.get_model_info()
        universe = "kr_stock"

        if model_info["exchange"] == "us":
            if model_info["instrument_type"] == "stock":
                universe = "us_stock"
            elif model_info["instrument_type"] == "etf":
                universe = "us_etf"
        elif model_info["exchange"] == "vnm":
            if model_info["instrument_type"] == "stock":
                universe = "vn_stock"

        cls.close = ContentFactory(universe, pre_start, end).get_df("price_close")
        cls.summary_dict = cls.get_summary(alpha_dict, cls.close, model_info)
        cls.ret_dict = {
            alpha: cls.summary_dict[alpha].nav.pct_change() for alpha in cls.alpha_set
        }

        risk_calculation_method = {
            "Volatility": cls.calculate_volatility,
            "MDD": cls.calculate_MDD,
            "TuW": cls.calculate_TuW,
        }

        cls.risk_df = pd.DataFrame(
            risk_calculation_method[cls.risk](
                cls.ret_dict, cls.alpha_set, cls.lookback_periods
            )
        )

        period = cls.rebalancing_period_map.get(cls.rebalancing_periods, "M")
        parsed_risk = cls.retain_first_of_period(cls.risk_df, period)

        cls.weights = parsed_risk.apply(cls.risk_parity_weights, axis=1)
        weights = cls.weights.reindex(cls.risk_df.index).ffill()

        cls.scaled_dict = dict()

        for alpha in cls.alpha_set:
            cls.scaled_dict[alpha] = (
                alpha_dict[alpha]
                .mul(weights[alpha].loc[alpha_dict[alpha].index], axis=0)
                .reindex(columns=ret_columns)
                .fillna(0)
            )

        combined_position = pd.DataFrame(
            index=cls.risk_df.index, columns=ret_columns
        ).fillna(0)
        for alpha in cls.alpha_set:
            combined_position += cls.scaled_dict[alpha]
        return combined_position.shift(1).loc[str(start) : str(end)]

    @classmethod
    def submit(
        cls,
        model_name: str,
        staging: bool = False,
        outdir: Optional[str] = None,
        **kwargs,
    ):
        """
        Submits the portfolio model to the Finter platform.

        :param docker_submit: Whether to submit the model using Docker.
        :param outdir: if not null, submitted code and json file are saved.
        :return: The result of the submission if successful, None otherwise.
        """
        prepare_docker_submit_files(model_name)
        return super().submit(model_name, staging, outdir, docker_submit=True, **kwargs)
