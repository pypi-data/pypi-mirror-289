# -*-coding:utf-8-*-
# N字涨停模式

import sys
import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import talib
from tqdm import tqdm
import datetime

from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]


class ThreeLimit(BaseStrategy):
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
        self.res_three_symbol = []
        self.res_break_symbol = []
        self.res_fall_symbol = []
        self.break_count = 0
        self.limit_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        pre_two_bar = bars[-2]
        pre_three_bar = bars[-3]
        pre_four_bar = bars[-4]
        pre_five_bar = bars[-5]
        max_high = round(np.max(bars['high']), 2)
        min_low = round(np.min(bars[1:]['low']), 2)

        pre_close = round(pre_bar['close'], 2)
        pre_open = round(pre_bar['open'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)
        pre_volume = pre_bar['volume']

        pre_two_close = round(pre_two_bar['close'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_two_open = round(pre_two_bar['open'], 2)
        pre_two_volume = pre_two_bar['volume']

        pre_three_close = round(pre_three_bar['close'], 2)
        pre_three_low = round(pre_three_bar['low'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_three_high = round(pre_three_bar['high'], 2)

        pre_high_rate = 100 * (pre_high - pre_two_close) / pre_two_close
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        pre_two_high_rate = 100 * (pre_two_high - pre_three_close) / pre_three_close
        pre_two_close_rate = 100 * (pre_two_close - pre_three_close) / pre_three_close

        pre_four_close = round(pre_four_bar['close'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        pre_five_close = round(pre_five_bar['close'], 2)
        pre_five_limit = round(pre_five_bar['high_limit'], 2)

        if pre_four_close == pre_four_limit and pre_three_close < pre_three_limit:

            if pre_five_close < pre_five_limit and pre_close < pre_limit:
                # 涨停价格未突破高点
                if pre_close * 1.1 < max(pre_three_high, pre_four_limit) * 1.01:
                    # if min_low > pre_three_low * 0.99:
                    self.res_three_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                # print(date_date)
                last_date = self.trading_date[i - 1]

                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': date})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                self.daily_break_symbol = []
                self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                self.daiyl_symbol = self.daily_limit_symbol + self.daily_break_symbol
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=6)

                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 6:
                        self.on_day_bar(bars[:-1])
                logger.info(f"日期{date}")
                logger.info(f"三日N字：{self.res_three_symbol}")

                self.res_symbol = []
                self.res_three_symbol = []
                self.res_break_symbol = []
                self.res_fall_symbol = []
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
    # test = NLimit(start_date=start_time,
    #               end_date=end_time,
    #               frequency='daily')
    test = ThreeLimit(start_date='2022-12-01',
                      end_date='2023-01-31',
                      frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
