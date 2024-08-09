# 涨停标次日止损

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

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        code = bars['code'][0]
        low = round(bars['low'][0], 2)
        pre_close = round(bars['pre_close'][0], 2)
        pre_low_rate = 100 * (low - pre_close) / pre_close
        if pre_low_rate < -5:
            self.res_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]

                last_N_list = []
                type_list = ['N_limit', 'TwoN_limit', 'breakN_limit']
                for N_type in type_list:
                    last_N_limit_dict = query_mongodb('QuadQuanta', N_type,
                                                          sql={'_id': last_date})
                    last_ten_N_limit_symbol_tmp = [symbol_data['symbol_list'] for symbol_data in
                                                   last_N_limit_dict]

                    last_N_limit_symbol = [symbol for symbol_list in last_ten_N_limit_symbol_tmp for symbol in
                                               symbol_list]
                    last_N_list += last_N_limit_symbol

                # self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                #     'date': last_date})
                # self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                #
                # self.daily_break_symbol = []
                # self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                #     'date': date})
                # self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                # self.daiyl_symbol = self.daily_break_symbol + self.daily_limit_symbol

                self.today_data = self.day_data[self.day_data['date'] == date]

                for symbol in last_N_list:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.today_data[self.today_data['code'] == symbol]
                    self.on_day_bar(bars)
                logger.info(f"日期{date}")
                logger.info(f"{self.res_symbol}")

                self.res_symbol = []


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

    test = NLimit(start_date='2022-09-01',
                  end_date='2022-11-10',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
