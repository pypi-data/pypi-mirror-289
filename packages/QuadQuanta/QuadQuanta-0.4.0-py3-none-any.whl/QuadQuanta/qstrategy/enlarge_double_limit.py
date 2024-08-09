# -*-coding:utf-8-*-
# 放量二板，板上大烂板，次日竞价弱转强，成交量大于10亿




import sys
import os
import csv
import numpy as np
import pandas as pd


from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]


class EnlargeDoubleLimit(BaseStrategy):
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

        pre_close = round(pre_bar['close'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_three_close = round(pre_three_bar['close'], 2)

        pre_open = round(pre_bar['open'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_low = round(pre_bar['low'], 2)

        pre_three_low = round(pre_three_bar['low'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)


        pre_volume = pre_bar['volume']
        pre_two_volume = pre_two_bar['volume']

        pre_amount = pre_bar['amount']

        if pre_close == pre_limit and pre_volume > pre_two_volume:
            if pre_amount > 10 * pow(10, 8):
                # if pre_three_close < pre_three_limit:
                    self.res_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                until_trade_days = get_trade_days(start_time='2018-01-01', end_time=date)
                last_trade_day = until_trade_days[-2]
                self.daily_limit_dict = []
                last_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_trade_day})

                last_limit_symbol = [symbol_data['code'] for symbol_data in last_limit_dict]

                history_N_data = get_bars(last_limit_symbol, end_time=date, count=3)

                for symbol in last_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 3:
                        self.on_day_bar(bars)
                logger.info(f"放量二板{date}:{self.res_symbol}")

                self.res_symbol = []
                self.res_two_symbol = []
                self.res_break_symbol = []
            except Exception as e:
                logger.warning(e)
                continue


if __name__ == '__main__':
    import datetime
    from QuadQuanta.data.update_data import update_day_bar

    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-3]
    # test = EnlargeDoubleLimit(start_date=start_time,
    #                           end_date=end_time,
    #                           frequency='daily', solid=True)
    test = EnlargeDoubleLimit(start_date='2023-01-01',
                              end_date='2023-05-01',
                              frequency='daily', solid=True)
    test.syn_backtest()
