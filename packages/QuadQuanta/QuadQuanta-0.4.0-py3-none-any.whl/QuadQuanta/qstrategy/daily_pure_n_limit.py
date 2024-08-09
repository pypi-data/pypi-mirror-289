# -*-coding:utf-8-*-
# 绝对N字涨停反转标, 走势有突破平台的势头。
# 要求开盘后不继续下探最高大于2%
# 目前观察成功率不高，只有扫板确定性强。

import sys
import os
import csv
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


class DailypureNLimit(BaseStrategy):
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
        self.start_date = start_date

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
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_three_close = round(pre_three_bar['close'], 2)
        pre_four_close = round(pre_four_bar['close'], 2)

        pre_open = round(pre_bar['open'], 2)

        pre_three_low = round(pre_three_bar['low'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        if pre_close < pre_limit:
            if pre_close_rate < -5 and (pre_open_rate - pre_close_rate) > 3:
                if pre_three_close < pre_three_limit:
                    self.res_symbol.append(code)

    def on_day_break_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        pre_two_bar = bars[-2]
        pre_three_bar = bars[-3]
        pre_four_bar = bars[-4]
        max_high = round(np.max(bars['high']), 2)
        min_low = round(np.min(bars[1:]['low']), 2)

        pre_close = round(pre_bar['close'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_three_close = round(pre_three_bar['close'], 2)
        pre_four_close = round(pre_four_bar['close'], 2)

        pre_open = round(pre_bar['open'], 2)

        pre_three_low = round(pre_three_bar['low'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        if pre_close < pre_limit:
            if pre_three_close < pre_three_limit:
                if pre_close_rate < -5 and (pre_open_rate - pre_close_rate) > 3:
                    self.res_break_symbol.append(code)


    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                until_trade_days = get_trade_days(start_time='2022-01-01', end_time=date)
                last_trade_day = until_trade_days[-2]
                last_two_trade_day = until_trade_days[-3]
                self.daily_limit_dict = []
                last_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_trade_day})

                last_limit_symbol = [symbol_data['code'] for symbol_data in last_limit_dict]

                last_break_limit_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': last_trade_day})

                last_break_limit_symbol = [symbol_data['code'] for symbol_data in last_break_limit_dict]

                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code']).tolist()

                history_N_data = get_bars(last_limit_symbol, end_time=date, count=4)

                for symbol in last_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 4:
                        self.on_day_bar(bars)

                history_N_data = get_bars(last_break_limit_symbol, end_time=date, count=4)
                for symbol in last_break_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 4:
                        self.on_day_break_bar(bars)

                # if len(self.res_symbol) > 0:
                #     save_mongodb('QuadQuanta', 'daily_N_limit',
                #                  {'_id': date, 'symbol_list': self.res_symbol})

                logger.info(f"潜在一日N字板{date}:{self.res_symbol}")


                logger.info(f"潜在炸板N字板{date}:{self.res_break_symbol}")
                # if len(self.res_break_symbol) > 0:
                #     save_mongodb('QuadQuanta', 'daily_breakfall_limit',
                #                  {'_id': date, 'symbol_list': self.res_break_symbol})

                self.res_symbol = []
                self.res_two_symbol = []
                self.res_break_symbol = []
            except Exception as e:
                logger.warning(e)
                continue


if __name__ == '__main__':
    import datetime
    from QuadQuanta.data.update_data import update_day_bar

    try:
        update_day_bar()
    except Exception as e:
        print(e)
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-3]
    # test = DailypureNLimit(start_date=start_time,
    #                        end_date=end_time,
    #                        frequency='daily', solid=True)
    test = DailypureNLimit(start_date='2022-04-10',
                           end_date='2022-04-25',
                           frequency='daily', solid=True)

    test.syn_backtest()
