# 一字板次日能否接盘
# 一字板次日没有一字开 是否可以接

# 连扳股再次涨停

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


class DoubleLimit(BaseStrategy):
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
        self.line_limit = []

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        pre_bar = bars[-2]
        code = pre_bar['code']
        today_bar = bars[-1]
        pre_high_limit = round(pre_bar['high_limit'], 2)
        pre_low = round(pre_bar['low'], 2)
        pre_close = round(pre_bar['close'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_amount = pre_bar['amount']
        today_high = round(today_bar['high'], 2)
        today_open = round(today_bar['open'], 2)
        today_low = round(today_bar['low'], 2)
        today_close = round(today_bar['close'], 2)
        today_high_limit = round(today_bar['high_limit'], 2)
        if pre_low == pre_high_limit:
            if today_high_limit == today_high:
                # if today_open < today_high_limit * 0.99:
                if today_open == today_high_limit and today_low < today_high_limit * 0.99:
                        self.line_limit.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                # date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                last_date = self.trading_date[i - 1]
                last_30_date = self.trading_date[i - 30]
                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_date})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]

                self.history_N_data = get_bars(self.daily_limit_symbol, end_time=date, count=2)

                for symbol in self.daily_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 2:
                        self.on_day_bar(bars)
                if len(self.line_limit) > 0 :
                    logger.info(f"日期{date}")
                    logger.info(f"{self.line_limit}")
                self.line_limit = []
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
    # test = DoubleLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily')
    test = DoubleLimit(start_date='2018-03-01',
                       end_date='2020-08-30',
                       frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
