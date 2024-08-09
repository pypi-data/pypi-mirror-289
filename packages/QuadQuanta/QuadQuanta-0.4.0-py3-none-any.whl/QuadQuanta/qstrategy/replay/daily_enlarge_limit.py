# 放量涨停标
# -*-coding:utf-8-*-
# N字涨停潜在标的
# 一日N字涨停和炸板一日涨停: 成功率高的在于前一日大跌，反转。
# 次日波动和开盘后的活跃度

import sys
import os
import numpy as np
import datetime
import talib
from QuadQuanta.data.update_data import update_day_bar
from QuadQuanta.core.strategy import BaseStrategy

# from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb

# from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]
# 振幅
Amplitude = 6


class DailyNLimit(BaseStrategy):
    def __init__(
        self, code=None, start_date=None, end_date=None, frequency="day", **kwargs
    ):
        super().__init__(code, start_date, end_date, frequency, **kwargs)
        self.pre_volume_dict = {}
        self.symbol_list = []
        self.res_symbol = []

        self.start_date = start_date

    def init(self):
        pass

    def pick_symbol(self, bar):
        """
        初选标，选择最高涨幅大于7，成交额度大于1亿的股票
        Parameters
        ----------
        bar

        Returns
        -------

        """
        code = bar["code"]
        high = round(bar["high"], 2)
        pre_close = round(bar["pre_close"], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        amount = bar["amount"]

        if high_rate > 6.5 and amount > pow(10, 8):
            self.symbol_list.append(code)

    def on_day_bar(self, bars: np.ndarray):
        """
        成交量大于昨日两倍，最高点大于最近20日高点（突破股）,20个交易日振幅在20%内
        Parameters
        ----------
        bars

        Returns
        -------

        """
        today_bar = bars[-1]
        code = today_bar["code"]
        pre_bar = bars[-2]
        today_volume = today_bar["volume"]
        pre_volume = pre_bar["volume"]
        max_high = max(bars[:-1]["high"])
        min_low = min(bars[:-1]["low"])

        today_high = today_bar["high"]

        # 振幅
        alp = 100 * (max_high - min_low) / min_low
        if today_volume > 1.5 * pre_volume and today_high > max_high and alp < 50:
            # MA10 = talib.SMA(bars[:-1]['close'], 10)[-1]
            # 连续10日收盘价大于20日线
            # 上升趋势
            # MA30 = talib.SMA(bars[:-1]['close'], 20)
            # if MA10 > MA20:
            self.res_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                until_trade_days = get_trade_days(
                    start_time="2018-01-01", end_time=date
                )
                self.today_data = self.day_data[self.day_data["date"] == date]
                self.code_list = np.unique(self.today_data["code"])

                for bar in self.today_data:
                    if str(bar["code"]).startswith("688"):
                        continue
                    self.pick_symbol(bar)
                history_N_data = get_bars(self.symbol_list, end_time=date, count=41)

                for symbol in self.symbol_list:
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == 41:
                        self.on_day_bar(bars)
                logger.info(f"日期{date}")
                logger.info(f"{self.res_symbol}")
                self.res_symbol = []
                self.symbol_list = []

            except Exception as e:
                logger.warning(e)
                continue


def daiyl_n_limit():
    # try:
    #     update_day_bar()
    # except Exception as e:
    #     print(e)
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time="2014-01-01", end_time=end_time)
    start_time = trade_days_until_today[-2]
    # test = DailyNLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily', solid=True)
    test = DailyNLimit(
        start_date="2023-03-01", end_date="2023-04-01", frequency="daily", solid=True
    )
    test.syn_backtest()


if __name__ == "__main__":
    daiyl_n_limit()
