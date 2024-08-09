# N_limit 次日走势分析 涨停后走势


import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
# from QuadQuanta.data.clickhouse_api import query_clickhouse
# from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_bars
import datetime
from QuadQuanta.data.update_data import update_day_bar
import talib


class N_limit_next(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(N_limit_next, self).__init__(code, start_date, end_date,
                                           frequency)
        self.pre_volume_dict = {}
        self.large_limit_symbol_list = []
        self.daiyl_symbol = []
        self.symbol = []

    def init(self):
        pass

    def on_day_bar(self, bars):
        today_bar = bars[-1]
        code = today_bar['code']
        open_ = round(today_bar['open'], 2)
        pre_close = round(today_bar['pre_close'], 2)
        # close = round(today_bar['close'], 2)
        high = round(today_bar['high'], 2)
        high_limit = round(today_bar['high_limit'], 2)
        high_rate = 100 *(high - pre_close)/pre_close
        if high_rate > 6:
            self.symbol.append(code)

    def syn_backtest(self):
        for i in range(2, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                all_N_limit_symbol = []

                N_limit_list = ['daily_TwoN_limit', 'daily_N_limit', 'daily_breakfall_limit']
                for N_limit in N_limit_list:
                    N_limit_symbol_list = query_mongodb('QuadQuanta', N_limit, sql={
                        '_id': last_date})
                    if len(N_limit_symbol_list) > 0:
                        all_N_limit_symbol += N_limit_symbol_list[-1]['symbol_list']

                for symbol in all_N_limit_symbol:
                    bars = self.today_data[self.today_data['code'] == symbol]
                    if len(bars) == 1:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                logger.info(f"N字半路模式{self.symbol}")

                self.daiyl_symbol = []
                self.symbol = []

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
    replay = N_limit_next(start_date='2023-03-01',
                          end_date='2023-04-11',
                          frequency='daily')
    # replay = EnlargeTrend(start_date=start_time,
    #                       end_date=end_time,
    #                       frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
