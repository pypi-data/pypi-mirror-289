# 连扳之后反弹
# 今日跌停，前两日是连扳
# -*-coding:utf-8-*-
# 触及涨停标
import sys
import os
import numpy as np

import datetime

from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]


class DoubleLimitRebound(BaseStrategy):
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
        self.res_two_break_symbol = []
        self.res_break_symbol = []
        self.res_fall_symbol = []
        self.res_test_two_symbol = []
        self.res_open_limit_symbol = []
        self.break_count = 0
        self.limit_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        pass

    def syn_backtest(self):
        self.total_assert = []
        for i in range(2, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                # print(date_date)
                last_two_date = self.trading_date[i - 2]
                last_date = self.trading_date[i - 1]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])

                recent_double_limit_dict = query_mongodb('QuadQuanta', 'daily_double_limit',
                                                         sql={'_id': {'$gte': last_two_date, '$lte': last_date}})
                recent_double_limit = np.unique([symbol for limit_dict in recent_double_limit_dict for symbol in
                                       limit_dict['symbol_list']])

                # self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=5)

                daily_down_limit = []
                for symbol in recent_double_limit:
                    if str(symbol).startswith('688'):
                        continue
                    today_bar = self.today_data[self.today_data['code'] == symbol][-1]
                    low_limit = round(today_bar['low_limit'], 2)
                    low = round(today_bar['low'], 2)
                    if low == low_limit:
                        self.res_symbol.append(symbol)

                logger.info(f"日期{date}")
                logger.info(f"触及跌停:{self.res_symbol}")

                #     logger.info(f"一字开盘两日N字板:{self.res_open_limit_symbol}")
                self.res_symbol = []

            except Exception as e:
                logger.warning(e)
                if self.res_symbol:
                    logger.info(f"日期{date}")
                    logger.info(f"触及跌停:{self.res_symbol}")
                    self.res_symbol = []
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
    test = DoubleLimitRebound(start_date='2023-04-25',
                              end_date='2023-07-01',
                              frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
