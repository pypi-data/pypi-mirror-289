# -*-coding:utf-8-*-
# 涨停 上两个交易日有一日大跌-5%,

import sys
import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
import datetime
import talib

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
        self.daiyl_symbol = []

    def init(self):
        pass

    def pick_symbol(self,bar):
        """
        初选标，当日最大涨幅大于5%
        Returns
        -------

        """
        code = bar['code']
        high = round(bar['high'],2)
        pre_close = round(bar['pre_close'],2)
        high_rate = 100 *(high- pre_close)/ pre_close
        if high_rate > 6:
            self.daiyl_symbol.append(code)

    def on_day_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']
        MA5 = talib.SMA(bars['close'], 5)[-1]
        MA10 = talib.SMA(bars['close'], 10)[-1]
        if MA5 > MA10:
            self.symbol_list.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(2, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                last_day = self.trading_date[i - 1]
                last_two_day = self.trading_date[i - 2]

                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code'])
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.last_day_plummete_dict = []

                self.last_day_plummete_dict = query_mongodb('QuadQuanta', 'daily_plummete', sql={
                    'date': last_day})

                self.last_day_plummete_symbol = [symbol_data['code'] for symbol_data in self.last_day_plummete_dict]
                for symbol in self.last_day_plummete_symbol:
                    bar = self.today_data[self.today_data['code'] == symbol][0]
                    self.pick_symbol(bar)
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=11)

                for symbol in self.daiyl_symbol:

                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 11:
                        self.on_day_bar(bars[:-1])
                logger.info(f"日期{date}")
                logger.info(f"标{self.symbol_list}")
                self.symbol_list = []
                self.daiyl_symbol = []
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
    test = NLimit(start_date='2023-01-01',
                  end_date='2023-02-01',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
