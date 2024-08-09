# 优化后标N字模式
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


class OpNLimit(BaseStrategy):
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

    def on_day_bar(self, bar):
        code = bar['code']
        high_price = round(bar['high'], 2)
        pre_close = round(bar['pre_close'], 2)
        high_rate = 100 * (high_price - pre_close) / pre_close
        if high_rate > 5:
            self.res_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                logger.info(f"日期{date}")
                self.today_data = self.day_data[self.day_data['date'] == date]
                # print(date_date)

                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code'])

                # 查询前10日N字是否涨停模式
                until_trade_days = get_trade_days(start_time='2022-01-01', end_time=date)
                last_trade_day = until_trade_days[-2]

                op_N_limit_symbol_list = []
                type_list = ['daily_op_N_limit', 'daily_op_TwoN_limit', 'daily_op_breakfall_limit']
                for N_type in type_list:
                    op_N_limit_symboldict = query_mongodb('QuadQuanta', N_type,
                                                          sql={'_id': last_trade_day})
                    op_N_limit_symbol_list_tmp = [symbol_data['symbol_list'] for symbol_data in
                                                  op_N_limit_symboldict]

                    last_ten_N_limit_symbol = [symbol for symbol_list in op_N_limit_symbol_list_tmp for symbol in
                                               symbol_list]
                    op_N_limit_symbol_list += last_ten_N_limit_symbol


                for symbol in op_N_limit_symbol_list:
                    if str(symbol).startswith('688'):
                        continue
                    bar = self.today_data[self.today_data['code'] == symbol]
                    self.on_day_bar(bar[-1])

                logger.info(f"涨幅大于5%标 {date}:{self.res_symbol}")
                self.res_symbol = []

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
    test = OpNLimit(start_date='2022-05-21',
                    end_date='2022-09-01',
                    frequency='daily')

    test.syn_backtest()
