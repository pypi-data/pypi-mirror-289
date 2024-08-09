# 连板一字回封股
# 做早盘炸板回封


import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse
from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from pymongo.errors import DuplicateKeyError
import talib


class OnlyDoubleLimit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(OnlyDoubleLimit, self).__init__(code, start_date, end_date,
                                              frequency)
        self.pre_volume_dict = {}
        self.limit_symbol_list = []
        self.fall_symbol_list = []
        self.break_symbol_list = []
        self.double_symbol_list = []
        self.pre_data_dict = {}
        self.pre_two_data_dict = {}
        self.res_symbol = []
        self.break_symbol = []
        self.double_count = 0
        self.break_double_count = 0
        self.init()

    def init(self):
        self.all_securities_info = get_securities_info(format='pandas')

    @staticmethod
    def is_limit(bar):
        close = round(bar['close'], 2)
        high_limit = round(bar['high_limit'], 2)
        if close == high_limit:
            return True
        else:
            return False

    def on_day_bar(self, bars):
        today_data = bars[-1]

        pre_data = bars[-2]
        pre_two_data = bars[-3]
        pre_three_data = bars[-4]
        pre_four_data = bars[-5]
        symbol = pre_data['code']

        today_open = round(today_data['open'], 2)
        today_limit = round(today_data['high_limit'], 2)
        today_low = round(today_data['low'], 2)
        pre_amount = pre_data['amount']
        amount = today_data['amount']

        # 昨日涨停
        if self.is_limit(pre_data) and amount > 3 * pow(10, 8) and pre_amount > 5 * pow(10, 8):
            # if not self.is_limit(pre_two_data):
                if today_limit == today_open and today_low < today_open:
                    if self.is_limit(today_data):
                        self.res_symbol.append(symbol)
                        self.double_count += 1
                    else:
                        self.break_symbol.append(symbol)
                        self.break_double_count += 1

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                last_day = self.trading_date[i - 1]
                limit_symbol_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': date})
                break_limit_symbol_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                limit_symbol = [symbol_data['code'] for symbol_data in limit_symbol_dict]
                break_limit_symbol = [symbol_data['code'] for symbol_data in break_limit_symbol_dict]
                symbol_list = limit_symbol + break_limit_symbol

                history_n_data = get_bars(symbol_list, end_time=date, count=5)

                for symbol in symbol_list:
                    bars = history_n_data[history_n_data['code'] == symbol]

                    if len(bars) == 5:
                        self.on_day_bar(bars)

                if len(self.res_symbol) > 0 or len(self.break_symbol) > 0:
                    logger.info(date)
                    logger.info(f"连板：{self.res_symbol}")
                    logger.info(f"连板炸板：{self.break_symbol}")
                self.res_symbol = []
                self.break_symbol = []

            except Exception as e:
                print("exception:", e)
                continue
        logger.info(f"连板计数：{self.double_count}")
        logger.info(f"炸板计数：{self.break_double_count}")


if __name__ == '__main__':
    import datetime

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    # start_time = trade_days_until_today[-300]
    test = OnlyDoubleLimit(start_date="2021-01-01",
                           end_date="2022-11-01",
                           frequency='daily')
    # test = DailyDoubleReplay(start_date='2019-05-01',
    #                          end_date='2019-05-28',
    #                          frequency='daily')

    test.syn_backtest()
