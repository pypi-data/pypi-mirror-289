# 加速涨停
# 昨日大分歧涨停，今日缩量板

import sys
import os
import numpy as np
import datetime
# import talib
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


class AccLimit(BaseStrategy):
    def __init__(
            self, code=None, start_date=None, end_date=None, frequency="day", **kwargs
    ):
        super().__init__(code, start_date, end_date, frequency, **kwargs)
        self.pre_volume_dict = {}
        self.symbol_list = []
        self.res_symbol = []
        self.success_symbol = []
        self.fail_symbol = []
        self.hold_symbol = []

        self.start_date = start_date

    def init(self):
        pass

    def pick_symbol(self, bar):
        """
        初选标，最大涨幅大于6.5，成交额大于1亿
        Parameters
        ----------
        bar

        Returns
        -------

        """
        code = bar["code"]
        high = round(bar["high"], 2)
        open_ = round(bar["open"], 2)
        high_limit = round(bar["high_limit"], 2)
        close = round(bar["close"], 2)
        pre_close = round(bar["pre_close"], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        close_rate = 100 * (close - pre_close) / pre_close
        # open_rate = 100 * (open_ - pre_close) / pre_close
        amount = bar["amount"]

        if amount > pow(10, 8):
            if high_rate > 8:
                # if high_rate - close_rate > 4.5:
                if high_limit == high:
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
        pre_high_limit = round(pre_bar["high_limit"], 2)
        pre_high = round(pre_bar["high"], 2)
        today_close = round(today_bar["close"], 2)
        today_high = round(today_bar["high"], 2)
        today_open = round(today_bar["open"], 2)
        pre_close = round(today_bar["pre_close"], 2)
        pre_two_close = round(pre_bar["pre_close"], 2)
        pre_open = round(pre_bar["open"], 2)
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        today_high_rate = 100 * (today_high - pre_close) / pre_close
        today_open_rate = 100 * (today_open - pre_close) / pre_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        # print(bars['close'][-11:])
        # MA60 = talib.SMA(bars['close'], 60)[60:]
        # # 30收盘价价序列
        # close_60 = bars['close'][60:]

        if pre_close == pre_high_limit == pre_high:
            self.res_symbol.append(code)
            if today_close == today_high:
                self.success_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        next_N_day = 0
        for i in range(0, len(self.trading_date) - next_N_day):
            try:
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data["date"] == date]
                self.code_list = np.unique(self.today_data["code"])

                for bar in self.today_data:
                    if str(bar["code"]).startswith("688") or str(bar["code"]).startswith("30"):
                        continue
                    self.pick_symbol(bar)

                N_day = 2
                history_N_data = get_bars(self.symbol_list, end_time=date, count=N_day)

                for symbol in self.symbol_list:
                    if str(symbol).startswith('30'):
                        continue
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == N_day:
                        self.on_day_bar(bars)

                if len(self.res_symbol) > 0:
                    logger.info(f"日期{date}")
                    logger.info(f"{self.res_symbol}")
                    # logger.info(f"{self.success_symbol}")
                    logger.info(f"回测标数量 {len(self.res_symbol)}")
                    logger.info(f"回测标数量 {len(self.success_symbol) / len(self.res_symbol)}")

                self.res_symbol = []
                self.success_symbol = []
                self.hold_symbol = []
                self.fail_symbol = []
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
    test = AccLimit(
        start_date="2022-06-05", end_date="2022-12-01", frequency="daily", solid=True
    )
    test.syn_backtest()


if __name__ == "__main__":
    daiyl_n_limit()
