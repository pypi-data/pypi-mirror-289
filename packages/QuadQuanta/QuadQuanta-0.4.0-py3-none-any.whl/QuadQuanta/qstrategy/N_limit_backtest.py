# -*-coding:utf-8-*-
# N字涨停潜在标的
# 一日N字涨停和炸板一日涨停: 成功率高的在于前一日大跌，反转。

import sys
import os
import csv
import numpy as np
import pandas as pd
import time
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
        self.res_symbol_all = []
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
        pre_high = round(pre_bar['high'], 2)
        pre_low = round(pre_bar['low'], 2)

        pre_three_low = round(pre_three_bar['low'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        pre_high_rate = 100 * (pre_high - pre_two_close) / pre_two_close
        pre_low_rate = 100 * (pre_low - pre_two_close) / pre_two_close

        if pre_two_close < pre_two_limit:
            if pre_open_rate < 2:
                if pre_high_rate > 6:
                    self.res_symbol_all.append(code)
                    if pre_close == pre_limit:
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
                self.res_break_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                until_trade_days = get_trade_days(start_time='2018-01-01', end_time=date)
                last_trade_day = until_trade_days[-2]
                last_two_trade_day = until_trade_days[-3]
                last_ten_trade_day = until_trade_days[-11]
                self.daily_limit_dict = []
                # last_ten_double_limit_dict = query_mongodb('QuadQuanta', 'daily_double_limit',
                #                                            sql={'_id': {'$gte': last_ten_trade_day,
                #                                                         '$lte': last_trade_day}})
                # last_ten_double_limit_symbol_tmp = [symbol_data['symbol_list'] for symbol_data in
                #                                     last_ten_double_limit_dict]
                # last_ten_double_limit_symbol = [symbol for symbol_list in last_ten_double_limit_symbol_tmp for symbol in
                #                                 symbol_list]
                # last_ten_double_limit_symbol = list(set(last_ten_double_limit_symbol))
                # logger.info(f"近期连扳{date}:{last_ten_double_limit_symbol}")

                last_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_two_trade_day})

                last_limit_symbol = [symbol_data['code'] for symbol_data in last_limit_dict]

                last_break_limit_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': last_two_trade_day})

                last_break_limit_symbol = [symbol_data['code'] for symbol_data in last_break_limit_dict]


                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code']).tolist()
                symbol_list = last_break_limit_symbol + last_limit_symbol
                history_N_data = get_bars(symbol_list, end_time=date, count=4)

                for symbol in symbol_list:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 4:
                        self.on_day_bar(bars)

                logger.info(f"{date} 涨幅大于6:{self.res_symbol_all}")
                logger.info(f"{date}:{self.res_symbol}")
                logger.info(f"{date}:{len(self.res_symbol)/len(self.res_symbol_all)}")

                self.res_symbol = []
                self.res_symbol_all = []

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
    # test = DailyNLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily', solid=True)
    test = NLimit(start_date='2022-07-21',
                  end_date='2022-08-01',
                  frequency='daily', solid=True)
    test.syn_backtest()
