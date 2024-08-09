# -*-coding:utf-8-*-
# 最原始的N字涨停模式

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
        self.res_symbol2 = []
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
        pre_bar = bars[-1]
        code = pre_bar['code']
        pre_two_bar = bars[-2]
        pre_three_bar = bars[-3]
        pre_four_bar = bars[-4]
        pre_close = round(pre_bar['close'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_close = round(pre_three_bar['close'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_high_rate = 100 * (pre_high - pre_two_close) / pre_two_close
        pre_four_close = round(pre_four_bar['close'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)
        # pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        if pre_two_close == pre_two_limit:
            if pre_close < pre_limit:
                if pre_three_close < pre_three_limit:
                    # 低开的股收盘需要大阴线
                    if pre_close_rate > 0:
                        self.res_symbol.append(code)
                    # 高开的股需要冲高大幅回落
                    if pre_high_rate > 5 and pre_high_rate - pre_close_rate > 5:
                        self.res_symbol2.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date) - 1):
            try:
                date = self.trading_date[i]
                next_day = self.trading_date[i + 1]
                until_trade_days = get_trade_days(start_time='2022-01-01', end_time=date)
                # last_trade_day = until_trade_days[-2]
                last_two_trade_day = until_trade_days[-3]

                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': date})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                self.daily_break_symbol = []
                self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                self.daiyl_symbol = self.daily_limit_symbol + self.daily_break_symbol
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=5)

                for symbol in np.unique(self.daiyl_symbol):
                    if str(symbol).startswith('688') or str(symbol).startswith('30'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 5:
                        self.on_day_bar(bars[:-1])

                # self.history_N_data = get_bars(self.res_symbol, end_time=next_day, count=1)
                # for symbol in np.unique(self.res_symbol):
                #     if str(symbol).startswith('688') or str(symbol).startswith('30'):
                #         continue
                #     bars = self.history_N_data[self.history_N_data['code'] == symbol]
                #     if len(bars) == 1:
                #         bar = bars[-1]
                #         high = round(bar['high'],2)
                #         close = round(bar['close'],2)
                #         high_limit = round(bar['high_limit'], 2)
                #         if high == high_limit:
                #             logger.info(f"N字板连扳:{symbol}")

                if len(self.res_symbol) > 0:
                    logger.info(f"日期{date}")
                    # logger.info(f"N字板:{self.res_symbol}")
                    yes_breakup_symbols = query_mongodb('QuadQuanta', 'daily_breakup', sql={
                        '_id': last_two_trade_day})[-1]['symbol_list']
                    breakup_N_limit = []
                    for symbol in np.unique(self.res_symbol):
                        if symbol in yes_breakup_symbols:
                            breakup_N_limit.append(symbol)
                    logger.info(f"N字板:{breakup_N_limit}")
                # if len(self.res_symbol2) > 0:
                #     logger.info(f"N字板昨日冲高回落:{self.res_symbol2}")

                self.res_symbol = []
                self.res_symbol2 = []

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
    test = NLimit(start_date=start_time,
                  end_date=end_time,
                  frequency='daily')
    test = NLimit(start_date='2023-01-01',
                  end_date='2023-09-28',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
