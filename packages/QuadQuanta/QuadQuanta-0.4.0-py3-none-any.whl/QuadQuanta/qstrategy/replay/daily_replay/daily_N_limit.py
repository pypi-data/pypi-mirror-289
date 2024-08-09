# -*-coding:utf-8-*-
# N字涨停潜在标的
# 一日N字涨停和炸板一日涨停: 成功率高的在于前一日大跌，反转。
# 次日波动和开盘后的活跃度

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
        self.res_symbol2 = []
        self.res_two_symbol = []
        self.res_break_two_symbol = []
        self.res_three_symbol = []
        self.opt_two_symbol = []
        self.res_break_symbol = []
        self.res_breakup_symbol = []
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


        if pre_close < pre_limit and pre_amplitude > 5:
            if pre_three_close < pre_three_limit:
                # 收盘大跌 或者冲高回落
                # if pre_close_rate < -3:
                self.res_symbol.append(code)
                if pre_high_rate > 5 and pre_high_rate - pre_close_rate > 5:
                    self.res_symbol2.append(code)

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
        pre_high = round(pre_bar['high'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)

        pre_three_high = round(pre_three_bar['high'], 2)

        pre_limit = round(pre_bar['high_limit'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)

        if pre_close < pre_limit and pre_four_close < pre_four_limit and pre_two_close < pre_two_limit:
            if pre_close * 1.1 < 1.05 * max(max(pre_two_high, pre_high), pre_three_high):
                if pre_three_close == pre_three_limit and pre_close < pre_open:
                    self.res_two_symbol.append(code)
                else:
                    self.res_break_two_symbol.append(code)


    def on_breakup_bar(self, bars: np.ndarray):
        """
        Parameters
        ----------
        bars

        Returns
        -------

        """
        today_bar = bars[-1]
        code = today_bar["code"]
        pre_bar = bars[-2]
        max_60_high = max(bars[:-1]["high"])
        today_high = round(today_bar["high"], 2)
        close = round(today_bar["close"], 2)
        pre_close = round(today_bar["pre_close"], 2)
        close_rate = 100 * (close - pre_close) / pre_close
        if close * 1.1 > max_60_high * 0.97 and close_rate < 9.9:
            self.res_breakup_symbol.append(code)


    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                logger.info(f"日期{date}")
                until_trade_days = get_trade_days(start_time='2022-01-01', end_time=date)
                last_trade_day = until_trade_days[-2]
                last_two_trade_day = until_trade_days[-3]

                last_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_trade_day})
                last_limit_symbol = [symbol_data['code'] for symbol_data in last_limit_dict]
                last_two_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_two_trade_day})
                last_two_limit_symbol = [symbol_data['code'] for symbol_data in last_two_limit_dict]

                history_N_data = get_bars(last_limit_symbol, end_time=date, count=4)

                for symbol in last_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 4:
                        self.on_day_bar(bars)

                # history_N_data = get_bars(last_two_limit_symbol, end_time=date, count=4)
                # for symbol in last_two_limit_symbol:
                #     if str(symbol).startswith('688'):
                #         continue
                #     bars = history_N_data[history_N_data['code'] == symbol]
                #     if len(bars) == 4:
                #         self.on_two_day_bar(bars)

                # 从昨日的突破股中找
                # yes_breakup_symbols = query_mongodb('QuadQuanta', 'daily_breakup', sql={
                #     '_id': last_trade_day})[-1]['symbol_list']
                #
                # breakup_N_limit = []
                # for symbol in np.unique(self.res_symbol):
                #     if symbol in yes_breakup_symbols:
                #         breakup_N_limit.append(symbol)

                # 明日涨停突破
                history_N_data = get_bars(self.res_symbol, end_time=date, count=51)
                for symbol in self.res_symbol:
                    if str(symbol).startswith('30'):
                        continue

                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == 51:
                        self.on_breakup_bar(bars)

                # if len(self.res_two_symbol) > 0:
                #
                #     # logger.info(f"两天N字板:{self.res_two_symbol}")
                #     save_mongodb('QuadQuanta', 'daily_TwoN_limit',
                #                  {'_id': date, 'symbol_list': self.res_two_symbol})
                #
                # if len(self.res_symbol) > 0:
                #
                #     # logger.info(f"N字板:{self.res_symbol}")
                #     save_mongodb('QuadQuanta', 'daily_N_limit',
                #                  {'_id': date, 'symbol_list': self.res_symbol})

                #
                # logger.info(f"潜在一日N字板{date}:{self.res_symbol}")
                logger.info(f"潜在突破N字板{date}:{self.res_breakup_symbol}")

                # logger.info(f"昨日冲高回落N字板{date}:{self.res_symbol2}")
                # logger.info(f"潜在两日N字板{date}:{self.res_two_symbol}")

                self.res_symbol = []
                self.res_breakup_symbol = []
                self.res_symbol2 = []
                self.res_two_symbol = []

            except Exception as e:
                logger.warning(e)
                continue


def daiyl_n_limit():
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    # test = DailyNLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily', solid=True)
    test = DailyNLimit(start_date='2023-01-11',
                       end_date='2023-07-30',
                       frequency='daily', solid=True)
    test.syn_backtest()


if __name__ == '__main__':
    daiyl_n_limit()
