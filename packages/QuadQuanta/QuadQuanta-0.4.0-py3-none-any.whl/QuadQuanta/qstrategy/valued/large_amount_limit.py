# 大成交量烂板涨停
# -*-coding:utf-8-*-
# 尾盘封板，次日平开或者低开，稳住红盘

import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
# from QuadQuanta.data.clickhouse_api import query_clickhouse
# from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.data.get_data import get_trade_days,get_bars
import datetime
from QuadQuanta.data.update_data import update_day_bar


class LargeLimit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(LargeLimit, self).__init__(code, start_date, end_date,
                                         frequency)
        self.pre_volume_dict = {}
        self.large_limit_symbol_list = []

        self.break_symbol_list = []

    def init(self):
        pass

    def on_day_bar(self, bars):
        today_bar = bars[-1]
        pre_bar = bars[-2]
        code = today_bar['code']
        close = round(today_bar['close'], 2)
        _open = round(today_bar['open'], 2)
        high = round(today_bar['high'], 2)
        limit = round(today_bar['high_limit'], 2)
        low = round(today_bar['low'], 2)
        amount = today_bar['amount']
        volume = today_bar['volume']
        symbol_data = {}
        pre_close = round(today_bar['pre_close'],2)
        high_rate = 100 * (high - pre_close) / pre_close
        low_rate = 100 * (low - pre_close) / pre_close
        pre_limit = round(pre_bar['high_limit'], 2)
        if amount > 8 * pow(10, 8) and pre_close < pre_limit:
            if high == limit:
                if close == limit:
                    self.large_limit_symbol_list.append(code)
                else:
                    self.break_symbol_list.append(code)


    def syn_backtest(self):
        for i in range(0, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])

                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': date})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                self.daily_break_symbol = []
                self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                self.daiyl_symbol = self.daily_limit_symbol + self.daily_break_symbol
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=2)
                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688') or str(symbol).startswith('30'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 2:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                logger.info(f"首板大成交涨停：{self.large_limit_symbol_list}")
                # logger.info(f"首板大成交炸板：{self.break_symbol_list}")

                self.large_limit_symbol_list = []
                self.break_symbol_list = []

            except Exception as e:
                print(e)
                continue


def daily_replay():
    # try:
    #     update_day_bar()
    # except Exception as e:
    #     print(e)
    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = LargeLimit(start_date='2022-03-01',
                       end_date='2022-07-01',
                       frequency='daily')
    # replay = LargeLimit(start_date=start_time,
    #                     end_date=end_time,
    #                     frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
