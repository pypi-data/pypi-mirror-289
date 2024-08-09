# -*-coding:utf-8-*-
# X日N字涨停
# 今日涨停首板，N个交易日内曽涨停或炸板。
# 涨停价格小于上次涨停日最高点的1.1倍

import sys
import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
import datetime

from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]


class LongNLimit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day',
                 **kwargs):
        super().__init__(code, start_date, end_date, frequency, **kwargs)
        self.pre_volume_dict = {}
        self.symbol_list = []
        self.res_symbol = []
        self.res_two_symbol = []
        self.res_two_break_symbol = []
        self.res_break_symbol = []
        self.res_fall_symbol = []
        self.res_test_two_symbol = []
        self.res_open_limit_symbol = []
        self.break_count = 0
        self.limit_count = 0

    def init(self):
        pass

    def if_break_limit(self, bar):
        limit = round(bar['high_limit'], 2)
        close = round(bar['close'], 2)
        high = round(bar['high'], 2)
        pre_close = round(bar['pre_close'], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        if high == limit and high_rate > 6 and high_rate < 12 and close < limit:
            return True
        else:
            return False

    def if_limit(self, bar):
        limit = round(bar['high_limit'], 2)
        close = round(bar['close'], 2)
        high = round(bar['high'], 2)
        pre_close = round(bar['pre_close'], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        if close == limit and high_rate > 6 and high_rate < 12:
            return True
        else:
            return False

    def on_day_bar(self, bars: np.ndarray):
        code = bars[-1]['code']
        pre_close = round(bars[-1]['close'], 2)
        if not self.if_limit(bars[-1]):
            for i, bar in enumerate(bars[:-1]):
                if self.if_limit(bar):
                    limit_close = round(bar['close'], 2)
                    limit_low = round(bar['pre_close'], 2)

                    max_high = max(bars[i:]['high'])
                    min_low = min(bars[i:]['close'])
                    if max_high < 1.1 * limit_close and pre_close < limit_close * 1.05 \
                            and min_low > limit_low * 0.99:
                        self.symbol_list.append(code)
                    break
            for i, bar in enumerate(bars[:-1]):
                if self.if_break_limit(bar):
                    limit_close = round(bar['close'], 2)
                    limit_low = round(bar['pre_close'], 2)

                    max_high = max(bars[i:]['high'])
                    min_low = min(bars[i:]['close'])
                    if max_high < 1.1 * limit_close and pre_close < limit_close * 1.05 \
                            and min_low > limit_low * 0.99:
                        self.symbol_list.append(code)
                    break

    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')

                self.history_N_data = get_bars(code=self.subscribe_code, end_time=date, count=11)

                for symbol in self.subscribe_code:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 11:
                        self.on_day_bar(bars)
                logger.info(f"日期{date}")
                logger.info(f"{self.symbol_list}")
                self.symbol_list = []


            except Exception as e:
                logger.warning(e)
                continue


def n_limit():
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-3]
    test = LongNLimit(start_date=start_time,
                      end_date=end_time,
                      frequency='daily')
    # test = LongNLimit(start_date='2023-03-03',
    #                   end_date='2023-04-08',
    #                   frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
