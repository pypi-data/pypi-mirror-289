# -*-coding:utf-8-*-
# 长时间N字 涨停3-10个交易日后
# 昨日收盘最低大于涨停起点，最高不超过2个涨停。

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

    def if_limit(self, bar):
        limit = round(bar['high_limit'], 2)
        close = round(bar['close'], 2)
        high = round(bar['high'], 2)
        if close == limit:
            return True
        else:
            return False

    def on_day_bar(self, bars: np.ndarray):
        code = bars[-1]['code']
        pre_close = round(bars[-1]['pre_close'], 2)
        if self.if_limit(bars[-1]):
            for i, bar in enumerate(bars[:-1]):
                if self.if_limit(bar):
                    limit_close = round(bar['close'], 2)
                    limit_low = round(bar['low'], 2)

                    max_high = max(bars[i:-1]['high'])
                    min_low = min(bars[i:-1]['close'])
                    if max_high < 1.1 * limit_close and pre_close < limit_close:
                        self.symbol_list.append(code)
                    break

    def syn_backtest(self):
        self.total_assert = []
        for i in range(10, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                start_date = self.trading_date[i - 10]
                end_date = self.trading_date[i - 3]

                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': {'$gte': start_date, '$lte': end_date}})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                self.daily_break_symbol = []
                # self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                #     'date': {'$gte':start_date,'$lte':end_date}})
                # self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                self.daiyl_symbol = self.daily_limit_symbol + self.daily_break_symbol
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=11)

                for symbol in self.daiyl_symbol:
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
    # test = LongNLimit(start_date=start_time,
    #                   end_date=end_time,
    #                   frequency='daily')
    test = LongNLimit(start_date='2023-04-03',
                      end_date='2023-05-08',
                      frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
