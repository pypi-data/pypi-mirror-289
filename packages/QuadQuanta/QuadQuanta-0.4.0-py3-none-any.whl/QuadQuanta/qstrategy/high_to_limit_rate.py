# 冲高涨停的概率
# 比如当日最高点+7，涨停的概率


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
        self.up_count = 0
        self.down_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        today_bar = bars[-1]
        code = today_bar['code']


        today_close = round(today_bar['close'], 2)
        today_open = round(today_bar['open'], 2)
        today_limit = round(today_bar['high_limit'], 2)
        today_high = round(today_bar['high'], 2)
        pre_close = round(today_bar['pre_close'], 2)
        amount = today_bar['amount']
        today_high_rate = 100 * (today_high - pre_close) / pre_close
        today_open_rate = 100 * (today_open - pre_close) / pre_close
        if today_high_rate > 8 and amount> pow(10,8) and today_open_rate < 4:
            if today_close == today_limit:
                self.up_count += 1
            else:
                self.down_count += 1
                self.res_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                for symbol in self.subscribe_code:
                    if str(symbol).startswith('688') or str(symbol).startswith('30'):
                        continue
                    bars = self.today_data[self.today_data['code'] == symbol]
                    if len(bars) == 1:
                        self.on_day_bar(bars)
                logger.info(f"日期{date}")
                if len(self.res_symbol) > 0:
                    logger.info(f"涨停{self.res_symbol}")
                logger.info(self.up_count/(self.up_count+self.down_count))
                self.res_symbol = []
                # self.up_count = 0
                # self.down_count = 0
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
    test = NLimit(start_date='2022-06-01',
                  end_date='2022-09-30',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
