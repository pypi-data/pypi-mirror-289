# 冲高 或炸板股次日继续冲高或炸板

# -*-coding:utf-8-*-
# N字涨停模式

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


class BreakNLimit(BaseStrategy):
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
        self.res_break_symbol = []
        self.res_fall_symbol = []
        self.res_test_two_symbol = []
        self.break_count = 0
        self.limit_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        today_bar = bars[-1]
        pre_bar = bars[-2]
        code = pre_bar['code']
        pre_two_bar = bars[-3]

        today_high = round(today_bar['high'], 2)
        today_limit = round(today_bar['high_limit'], 2)

        pre_close = round(pre_bar['close'], 2)
        pre_open = round(pre_bar['open'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)


        pre_two_close = round(pre_two_bar['close'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)

        today_high_rate = 100 * (today_high - pre_close) / pre_close
        pre_fall_rate = 100 * (pre_high - pre_close) / pre_close

        pre_high_rate = 100 * (pre_high - pre_two_close) / pre_two_close

        # 前日炸板
        if pre_two_high == pre_two_limit and pre_two_close < pre_two_high:
            # 昨日冲高回落
            if pre_close < pre_limit and pre_high_rate > 5 and pre_fall_rate > 3:
                # if today_high > pre_close:
                # if today_high_rate > 5:
                if today_high == today_limit:
                    self.res_break_symbol.append(code)

        # # 前日冲高回落
        # if pre_two_high_rate > 9 and pre_two_high_rate - pre_two_close_rate > 3:
        #     if pre_close < pre_limit and pre_two_high < pre_two_limit:
        #         if pre_three_close < pre_three_limit:
        #             self.res_fall_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(2, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                last_two_day = self.trading_date[i-2]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                # print(date_date)

                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code'])
                self.daily_limit_dict = []
                # self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                #     'date': date})
                # self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                self.daily_break_symbol = []
                self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': last_two_day})
                self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                self.daiyl_symbol = self.daily_break_symbol
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=3)

                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 3:
                        self.on_day_bar(bars)
                logger.info(f"日期{date}")

                # logger.info(f"次数{(self.limit_count + self.break_count)}")

                # logger.info(f"封板率{self.limit_count / (self.limit_count + self.break_count)}")

                if len(self.res_symbol) > 0:
                    logger.info(f"N字板:{self.res_symbol}")

                if len(self.res_break_symbol) > 0:
                    logger.info(f"炸板N字板:{self.res_break_symbol}")

                if len(self.res_fall_symbol) > 0:
                    logger.info(f"冲高回落N字板:{self.res_fall_symbol}")

                self.res_symbol = []
                self.res_two_symbol = []
                self.res_test_two_symbol = []
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
    # test = BreakNLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily')
    test = BreakNLimit(start_date='2022-01-13',
                       end_date='2022-11-20',
                       frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
