# -*-coding:utf-8-*-
# 昨日跌停，今日触及涨停,昨日成交量大于5亿
# 昨日收盘小于10日线
# TODO 均线上升趋势排列？？
#

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


class LowLimit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(LowLimit, self).__init__(code, start_date, end_date,
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

    def on_day_bar(self, bars):
        today_data = bars[-1]
        pre_data = bars[-2]
        pre_two_data = bars[-3]
        symbol = pre_data['code']

        today_open = round(today_data['open'], 2)
        today_low = round(today_data['low'], 2)
        tooday_high = round(today_data['high'], 2)
        today_limit = round(today_data['high_limit'], 2)


        pre_close = round(pre_data['close'], 2)
        pre_low = round(pre_data['low'], 2)
        pre_low_limit = round(pre_data['low_limit'], 2)
        pre_two_close = round(pre_two_data['close'], 2)
        pre_two_limit = round(pre_two_data['high_limit'], 2)

        today_high_rate = 100 * (tooday_high - pre_close) /pre_close
        # MA10 = talib.SMA(bars['close'], 10)
        # today_MA10 = MA10[-1]
        # 昨日收盘跌停
        if pre_low == pre_low_limit and pre_close == pre_low:
            if pre_two_close < pre_two_limit:
                # if tooday_high == today_limit:
                if today_high_rate > 9:
                    self.res_symbol.append(symbol)

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                last_day = self.trading_date[i-1]
                low_limit_symbol_dict = query_mongodb('QuadQuanta', 'daily_low_limit', sql={
                    'date': last_day})
                # break_limit_symbol_dict = query_mongodb('QuadQuanta', 'daily_break_limit', sql={
                #     'date': date})
                low_limit_symbol = [symbol_data['code'] for symbol_data in low_limit_symbol_dict]
                # break_limit_symbol = [symbol_data['code'] for symbol_data in break_limit_symbol_dict]
                symbol_list = low_limit_symbol

                history_N_data = get_bars(symbol_list, end_time=date, count=3)

                for symbol in symbol_list:
                    bars = history_N_data[history_N_data['code'] == symbol]

                    if len(bars) == 3:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                if len(self.res_symbol) > 0:
                    logger.info(f"昨日跌停，今日涨停：{self.res_symbol}")
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
    test = LowLimit(start_date="2020-01-01",
                    end_date="2021-01-01",
                    frequency='daily')
    # test = DailyDoubleReplay(start_date='2019-05-01',
    #                          end_date='2019-05-28',
    #                          frequency='daily')

    test.syn_backtest()
