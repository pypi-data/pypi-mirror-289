# -*-coding:utf-8-*-
# 封板成功率统计

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


class LimitRate(BaseStrategy):
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

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        pre_two_bar = bars[-2]
        pre_three_bar = bars[-3]
        pre_four_bar = bars[-4]
        max_high = round(np.max(bars['high']), 2)
        min_low = round(np.min(bars[1:]['low']), 2)

        pre_close = round(pre_bar['close'], 2)
        pre_open = round(pre_bar['open'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)

        pre_two_close = round(pre_two_bar['close'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)

        pre_three_close = round(pre_three_bar['close'], 2)
        pre_three_low = round(pre_three_bar['low'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)

        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        pre_two_high_rate = 100 * (pre_two_high - pre_three_close) / pre_three_close
        pre_two_close_rate = 100 * (pre_two_close - pre_three_close) / pre_three_close

        pre_four_close = round(pre_four_bar['close'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        if pre_two_close == pre_two_limit:
            if pre_close < pre_limit:
                # and pre_close_rate < pre_open_rate + 3:
                # if max_high < pre_two_close * 1.01:
                if pre_three_close < pre_three_limit:
                    self.res_symbol.append(code)

        if pre_two_high == pre_two_limit and pre_two_close < pre_two_high:
            if pre_close < pre_limit:
                # and pre_close_rate < pre_open_rate + 3:
                # if max_high < pre_two_close * 1.01:
                # if pre_three_close < pre_three_limit:
                    self.res_break_symbol.append(code)

        if pre_three_close == pre_three_limit and pre_two_close < pre_two_limit:
            # and max_high < pre_three_close * 1.01:
            # print(f"N2字涨停标{current_day}-{code}")
            if pre_four_close < pre_four_limit and pre_close < pre_limit:
                if min_low > pre_three_low * 0.99:
                    self.res_two_symbol.append(code)

        # 前日冲高回落
        if pre_two_high_rate > 9 and pre_two_high_rate - pre_two_close_rate > 3:
            if pre_close < pre_limit and pre_two_high < pre_two_limit:
                if pre_three_close < pre_three_limit:
                    self.res_fall_symbol.append(code)



    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:

                self.symbol_list = []
                date = self.trading_date[-1]

                self.history_N_data = get_bars(end_time=date, count=250)
                code_list = np.unique(self.history_N_data['code'])
                print(code_list)

                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 5:
                        self.on_day_bar(bars[:-1])
                logger.info(f"日期{date}")
                if len(self.res_symbol) > 0:
                    logger.info(f"N字板:{self.res_symbol}")
                # if len(self.res_two_symbol) > 0:
                #     logger.info(f"两天N字板:{self.res_two_symbol}")
                # if len(self.res_break_symbol) > 0:
                #     logger.info(f"炸板N字板:{self.res_break_symbol}")
                # if len(self.res_fall_symbol) > 0:
                #     logger.info(f"冲高回落N字板:{self.res_fall_symbol}")

                next_date = self.trading_date[i + 1]
                double_limit_symbol = query_mongodb('QuadQuanta', 'daily_double_limit', sql={
                    '_id': next_date})[0]['symbol_list']
                break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': next_date})
                break_symbol = [symbol_data['code'] for symbol_data in break_dict]
                res_symbol = double_limit_symbol + break_symbol
                for symbol in res_symbol:
                    if symbol in self.res_symbol or symbol in self.res_break_symbol:
                        print(f"成功连板:{next_date} - {symbol}")
                self.res_symbol = []
                self.res_two_symbol = []
                self.res_break_symbol = []
                self.res_fall_symbol = []
            except Exception as e:
                logger.warning(e)
                continue


if __name__ == '__main__':
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-3]
    # test = NLimit(start_date=start_time,
    #               end_date=end_time,
    #               frequency='daily')
    test = LimitRate(start_date='2022-07-01',
                     end_date='2022-07-30',
                     frequency='daily')

    test.syn_backtest()
