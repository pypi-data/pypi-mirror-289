# -*-coding:utf-8-*-
# 每日突破前高，配合板块突破。买点在于情绪节点和回踩位置
# 突破40日高点, 昨日未突破

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
        初选标，最大涨幅大于6.5，成交额大于1亿
        Parameters
        ----------
        bar

        Returns
        -------

        """
        code = bar["code"]
        high = round(bar["high"], 2)
        high_limit = round(bar["high_limit"], 2)
        close = round(bar["close"], 2)
        pre_close = round(bar["pre_close"], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        amount = bar["amount"]

        # if high_limit == high and amount > pow(10, 8):
        if high_rate > 6 and amount > pow(10, 8):
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
        # today_volume = today_bar["volume"]
        # pre_volume = pre_bar["volume"]
        # pre_high = round(pre_bar['high'])
        max_20_high = max(bars[20:-1]["close"])
        min_20_low = min(bars[20:-1]["close"])
        max_30_high = max(bars[10:-1]["close"])

        today_high = today_bar["high"]
        # print(bars['close'][-11:])
        last_10_close = np.mean(bars[-6:-1]['close'])
        first_10_close = np.mean(bars[:6]['close'])
        # MA30 = talib.SMA(bars['close'], 30)[-1]
        # MA20 = talib.SMA(bars['close'],20)[-1]

        # 振幅
        alp = 100 * (max_20_high - min_20_low) / min_20_low
        # 最近20日振幅小于50%
        if today_high > max_30_high and alp < 50:
            # 前N日未突破
            for i in range(-3, -1):
                close = round(bars[i]['close'], 2)
                high = round(bars[i]['high'], 2)
                max_high = round(max(bars[:i - 1]['high']), 2)
                if close > max_high:
                    break
                if i == -2:
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
                    if str(symbol).startswith('30'):
                        continue
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == 41:
                        self.on_day_bar(bars)
                # save_mongodb('QuadQuanta', 'daily_breakup',
                #              {'_id': date, 'symbol_list': self.res_symbol})
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
    start_time = trade_days_until_today[-3]
    test = DailyNLimit(start_date=start_time,
                       end_date=end_time,
                       frequency='daily', solid=True)
    # test = DailyNLimit(
    #     start_date="2023-05-04", end_date="2023-05-04", frequency="daily", solid=True
    # )
    test.syn_backtest()


if __name__ == "__main__":
    daiyl_n_limit()
