# -*-coding:utf-8-*-
# N字涨停潜在标的
# 一日N字涨停和炸板一日涨停: 成功率高的在于前一日大跌，反转。

import sys
import os

import numpy as np

import datetime

from QuadQuanta.data.update_data import update_day_bar
from QuadQuanta.core.strategy import BaseStrategy
# from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
# from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]
# 振幅
Amplitude = 6


class DailyNLimit(BaseStrategy):
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
        self.res_break_two_symbol = []
        self.res_three_symbol = []
        self.opt_two_symbol = []
        self.res_break_symbol = []
        self.res_break_up_symbol = []
        self.res_fall_symbol = []
        self.start_date = start_date

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        pre_two_bar = bars[-2]
        pre_three_bar = bars[-3]
        pre_four_bar = bars[-4]
        max_high = round(np.max(bars['high']), 2)
        min_low = round(np.min(bars[1:]['low']), 2)

        pre_close = round(pre_bar['close'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_three_close = round(pre_three_bar['close'], 2)
        pre_four_close = round(pre_four_bar['close'], 2)

        pre_open = round(pre_bar['open'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_low = round(pre_bar['low'], 2)

        pre_three_low = round(pre_three_bar['low'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        pre_high_rate = 100 * (pre_high - pre_two_close) / pre_two_close
        pre_low_rate = 100 * (pre_low - pre_two_close) / pre_two_close
        # 昨日振幅
        pre_amplitude = 100 * (pre_high - pre_low) / pre_low

        if pre_close < pre_limit and pre_close_rate < -1:
            if pre_three_close < pre_three_limit:
                self.res_symbol.append(code)

    def on_day_break_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        pre_two_bar = bars[-2]
        pre_three_bar = bars[-3]
        pre_four_bar = bars[-4]
        max_high = round(np.max(bars['high']), 2)
        min_low = round(np.min(bars[1:]['low']), 2)

        pre_close = round(pre_bar['close'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_three_close = round(pre_three_bar['close'], 2)
        pre_four_close = round(pre_four_bar['close'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_open = round(pre_bar['open'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)

        pre_high_rate = 100 * (pre_high - pre_two_close) / pre_two_close
        pre_fall_rate = 100 * (pre_high - pre_close) / pre_close
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close

        pre_two_close_rate = 100 * (pre_two_close - pre_three_close) / pre_three_close
        if pre_close < pre_limit and pre_two_close_rate < 8:
            # if pre_high_rate > 5 and pre_fall_rate > 3:
            #     self.res_break_up_symbol.append(code)
            if pre_three_close < pre_three_limit:
                self.res_break_symbol.append(code)


    def on_two_day_bar(self, bars: np.ndarray):
        pre_bar = bars[-1]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        pre_two_bar = bars[-2]
        pre_three_bar = bars[-3]
        pre_four_bar = bars[-4]
        max_high = round(np.max(bars['high']), 2)
        min_low = round(np.min(bars[1:]['low']), 2)

        pre_close = round(pre_bar['close'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)

        pre_three_close = round(pre_three_bar['close'], 2)
        pre_four_close = round(pre_four_bar['close'], 2)

        pre_open = round(pre_bar['open'], 2)
        pre_two_open = round(pre_two_bar['open'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)

        pre_three_high = round(pre_three_bar['high'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        if pre_close < pre_limit:
            if pre_close * 1.1 < 1.025 * max(pre_two_high, pre_three_high):
                if pre_three_close == pre_three_limit:
                    self.res_two_symbol.append(code)
                else:
                    self.res_break_two_symbol.append(code)



    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                until_trade_days = get_trade_days(start_time='2022-01-01', end_time=date)
                last_trade_day = until_trade_days[-2]
                last_two_trade_day = until_trade_days[-3]
                last_three_trade_day = until_trade_days[-4]


                last_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_trade_day})

                last_limit_symbol = [symbol_data['code'] for symbol_data in last_limit_dict]

                last_break_limit_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': last_trade_day})

                last_break_limit_symbol = [symbol_data['code'] for symbol_data in last_break_limit_dict]


                last_two_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_two_trade_day})

                last_two_break_limit_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': last_two_trade_day})
                last_two_limit_symbol = [symbol_data['code'] for symbol_data in last_two_limit_dict]
                # last_two_break_limit_symbol = []
                last_two_break_limit_symbol = [symbol_data['code'] for symbol_data in last_two_break_limit_dict]
                last_two_limit_symbol += last_two_break_limit_symbol
                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code']).tolist()
                # 三日N字涨停
                last_three_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_three_trade_day})
                last_three_limit_symbol = [symbol_data['code'] for symbol_data in last_three_limit_dict]

                history_N_data = get_bars(last_limit_symbol, end_time=date, count=4)

                for symbol in last_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 4:
                        self.on_day_bar(bars)

                history_N_data = get_bars(last_break_limit_symbol, end_time=date, count=4)
                for symbol in last_break_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 4:
                        self.on_day_break_bar(bars)


                history_N_data = get_bars(last_two_limit_symbol, end_time=date, count=4)
                for symbol in last_two_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 4:
                        self.on_two_day_bar(bars)




                if len(self.res_symbol) > 0:
                    logger.info(f"N字板:{res_symbol}")
                    # 保存优化后的标

                    save_mongodb('QuadQuanta', 'daily_N_limit',
                                 {'_id': date, 'symbol_list': self.res_symbol})

                if len(self.res_break_symbol) > 0:
                    # 保存优化后的标

                    save_mongodb('QuadQuanta', 'daily_breakfall_limit',
                                 {'_id': date, 'symbol_list': self.res_break_symbol})

                logger.info(f"潜在一日N字板{date}:{self.res_symbol}")
                logger.info(f"潜在炸板N字板{date}:{self.res_break_symbol}")
                logger.info(f"潜在两日N字板{date}:{self.res_two_symbol}")
                logger.info(f"潜在炸板两日N字板{date}:{self.res_break_two_symbol}")
                logger.info(f"潜在三日N字板{date}:{self.res_three_symbol}")

                self.res_symbol = []
                self.res_two_symbol = []
                self.res_break_two_symbol = []
                self.res_three_symbol = []
                self.res_break_symbol = []
                self.res_break_up_symbol = []
                self.res_fall_symbol = []
                self.opt_two_symbol = []

            except Exception as e:
                logger.warning(e)
                continue


def daiyl_n_limit():
    try:
        update_day_bar()
    except Exception as e:
        print(e)
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    test = DailyNLimit(start_date=start_time,
                       end_date=end_time,
                       frequency='daily', solid=True)
    # test = DailyNLimit(start_date='2022-10-13',
    #                    end_date='2022-10-21',
    #                    frequency='daily', solid=True)
    test.syn_backtest()


if __name__ == '__main__':
    daiyl_n_limit()
