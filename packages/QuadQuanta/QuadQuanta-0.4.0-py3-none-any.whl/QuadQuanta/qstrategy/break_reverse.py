# -*-coding:utf-8-*-
# 炸板次日反包
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


class NLimit(BaseStrategy):
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
        self.res_open_limit_symbol = []
        self.break_count = 0
        self.limit_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']

        pre_close = round(pre_bar['close'], 2)
        pre_open = round(pre_bar['open'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_low = round(pre_bar['low'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)
        pre_volume = pre_bar['volume']

        # 昨日炸板
        pre_alp_rate = 100 * (pre_high - pre_low) / pre_low
        if pre_close < pre_limit and pre_high== pre_limit:
            self.res_symbol.append(code)


    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                # print(date_date)

                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code'])
                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': date})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                self.daily_break_symbol = []
                self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                self.daiyl_symbol = self.daily_limit_symbol + self.daily_break_symbol
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=2)

                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688') or str(symbol).startswith('30'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 2:
                        self.on_day_bar(bars[:-1])
                logger.info(f"日期{date}")

                if len(self.res_symbol) > 0:
                    logger.info(f"炸板反包:{self.res_symbol}")

                self.res_symbol = []
                self.res_two_symbol = []
                self.res_test_two_symbol = []
                self.res_break_symbol = []
                self.res_fall_symbol = []
                self.res_open_limit_symbol = []
                # 找连扳标
                next_date = self.trading_date[i + 1]

                double_limit_symbol = query_mongodb('QuadQuanta', 'daily_double_limit', sql={
                    '_id': next_date})[0]['symbol_list']
                break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': next_date})
                break_symbol = [symbol_data['code'] for symbol_data in break_dict]
                res_symbol = double_limit_symbol + break_symbol
                N_type_limit = []
                break_limit = []
                two_limit = []
                for symbol in res_symbol:
                    if symbol in self.res_symbol:
                        N_type_limit.append(symbol)
                    elif symbol in self.res_break_symbol:
                        break_limit.append(symbol)
                    elif symbol in self.res_two_symbol:
                        two_limit.append(symbol)
                # print(f"N字成功连板:{next_date} - {N_type_limit}")
                # print(f"炸板N字成功连板:{next_date} - {break_limit}")
                # print(f"两日N字成功连板:{next_date} - {two_limit}")

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
    test = NLimit(start_date='2023-01-21',
                  end_date='2023-02-01',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
