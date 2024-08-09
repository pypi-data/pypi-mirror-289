# 当日突破涨停标


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


class BreakLimit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(BreakLimit, self).__init__(code, start_date, end_date,
                                         frequency)
        self.pre_volume_dict = {}
        self.large_limit_symbol_list = []
        self.daiyl_symbol = []
        self.symbol = []
        self.break_symbol = []


    def init(self):
        pass

    def on_day_bar(self, bars):
        bar = bars[-1]
        code = bar['code']
        open_ = round(bar['open'], 2)
        close = round(bar['close'], 2)

        high = round(bar['high'], 2)
        high_limit = round(bar['high_limit'], 2)
        high_rate = 100 * (high - open_) / open_
        if high == high_limit and high_rate > 5:
            if close == high_limit:
                self.symbol.append(code)
            else:
                self.break_symbol.append(code)

    def syn_backtest(self):
        for i in range(2, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                last_two_date = self.trading_date[i - 2]
                last_date = self.trading_date[i - 1]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])

                breakup_symbol = []

                N_limit_list = ['daily_breakup']
                # 取突破标
                for N_limit in N_limit_list:
                    N_limit_symbol_list = query_mongodb('QuadQuanta', N_limit, sql={'_id': date})
                    if len(N_limit_symbol_list) > 0:
                        breakup_symbol += N_limit_symbol_list[-1]['symbol_list']
                for symbol in breakup_symbol:
                    if str(symbol).startswith("30"):
                        continue
                    bars = self.today_data[self.today_data["code"] == symbol]
                    if len(bars) == 1:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                logger.info(f"涨停{self.symbol}")
                logger.info(f"炸板{self.break_symbol}")
                logger.info(f"封板率{len(self.symbol)/(len(self.break_symbol) + len(self.symbol))}")

                self.daiyl_symbol = []
                self.symbol = []
                self.break_symbol = []

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
    replay = BreakLimit(start_date='2023-05-29',
                        end_date='2023-06-15',
                        frequency='daily')
    # replay = EnlargeTrend(start_date=start_time,
    #                       end_date=end_time,
    #                       frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
