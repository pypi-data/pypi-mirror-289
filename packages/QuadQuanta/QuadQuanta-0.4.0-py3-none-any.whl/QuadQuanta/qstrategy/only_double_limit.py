# 二板股


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
        # 前日涨停涨停
        if self.is_limit(pre_two_data):
            # 今日未涨停
            if not self.is_limit(today_data):
                #
                if not self.is_limit(pre_three_data):
                    self.res_symbol.append(symbol)

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                last_day = self.trading_date[i - 1]
                limit_symbol_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_day})

                limit_symbol = [symbol_data['code'] for symbol_data in limit_symbol_dict]
                symbol_list = limit_symbol

                history_N_data = get_bars(symbol_list, end_time=date, count=5)

                for symbol in symbol_list:
                    bars = history_N_data[history_N_data['code'] == symbol]

                    if len(bars) == 5:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                if len(self.res_symbol) > 0:
                    logger.info(f"二板：{self.res_symbol}")
                self.res_symbol = []

            except Exception as e:
                print("exception:", e)
                continue


if __name__ == '__main__':
    import datetime

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    # start_time = trade_days_until_today[-300]
    test = OnlyDoubleLimit(start_date="2022-01-01",
                           end_date="2022-05-01",
                           frequency='daily')
    # test = DailyDoubleReplay(start_date='2019-05-01',
    #                          end_date='2019-05-28',
    #                          frequency='daily')

    test.syn_backtest()
