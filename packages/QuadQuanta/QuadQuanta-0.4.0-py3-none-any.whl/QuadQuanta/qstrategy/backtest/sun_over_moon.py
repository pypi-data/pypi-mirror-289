# 阳包阴战法
# 昨日收盘大阴线，今天盘中最高点大于昨日阴线。做反转
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
# from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
# from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]


class SunOverMoon(BaseStrategy):
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
        today_bar = bars[-1]
        pre_bar = bars[-2]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        today_high = round(today_bar['high'], 2)
        today_open = round(today_bar['open'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_close = round(pre_bar['close'], 2)
        pre_two_close = round(pre_bar['pre_close'], 2)
        pre_open = round(pre_bar['open'], 2)

        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        today_high_rate = 100 * (today_high - pre_close) / pre_close
        today_open_rate = 100 * (today_open - pre_close) / pre_close

        sun_rate = today_high_rate - today_open_rate
        moon_rate = pre_open_rate - pre_close_rate
        if pre_close_rate < -4 and sun_rate > moon_rate > 0:
            self.res_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                until_trade_days = get_trade_days(start_time='2022-01-01', end_time=date)

                self.daily_limit_dict = []
                self.today_data = self.day_data[self.day_data['date'] == date]
                today_symbols = np.unique(self.today_data['code']).tolist()
                sun_symbol = []
                for symbol in today_symbols:
                    bar = self.today_data[self.today_data['code'] == symbol][-1]
                    high = round(bar['high'], 2)
                    pre_close = round(bar['pre_close'], 2)
                    high_rate = 100 * (high - pre_close) / pre_close
                    if high_rate > 4.9:
                        sun_symbol.append(symbol)

                history_N_data = get_bars(sun_symbol, end_time=date, count=2)

                for symbol in sun_symbol:
                    if str(symbol).startswith('688') or str(symbol).startswith('300'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 2:
                        self.on_day_bar(bars)
                logger.info(f"阴包阳标{date}:{self.res_symbol}")
                self.res_symbol = []


            except Exception as e:
                logger.warning(e)
                continue


def sun_over_moon():
    try:
        update_day_bar()
    except Exception as e:
        print(e)
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)

    test = SunOverMoon(start_date='2023-01-01',
                       end_date='2023-08-25',
                       frequency='daily', solid=True)
    test.syn_backtest()


if __name__ == '__main__':
    sun_over_moon()
