# 昨日炸板 今日涨停，前日未涨停


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


class Break2Limit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(Break2Limit, self).__init__(code, start_date, end_date,
                                          frequency)
        self.pre_volume_dict = {}
        self.large_limit_symbol_list = []
        self.daiyl_symbol = []
        self.all_count = 0
        self.suc_count = 0
        self.symbol = []
        self.enlarge_symbol = []

    def init(self):
        pass

    def on_day_bar(self, bars):
        today_bar = bars[-1]
        code = today_bar['code']
        close = round(today_bar['close'], 2)
        open_ = round(today_bar['open'], 2)
        pre_close = round(today_bar['pre_close'], 2)
        high = round(today_bar['high'], 2)
        high_limit = round(today_bar['high_limit'], 2)
        open_rate = 100 * (open_ - pre_close) / pre_close
        # 今日触及涨停标
        if high == high_limit:
            self.symbol.append(code)

    def pre_day_bar(self, bars):
        next_bar = bars[-1]
        pre_two_bar =bars[-4]
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_two_high_limit = round(pre_two_bar['high_limit'], 2)
        amount = round(pre_two_bar['amount'], 2)
        today_bar = bars[-2]
        code = today_bar['code']
        close = round(today_bar['close'], 2)
        high_limit = round(today_bar['high_limit'], 2)
        amount = round(today_bar['amount'], 2)
        next_high = round(next_bar['high'], 2)
        next_high_rate = 100 * (next_high - close) / close

        if pre_two_close < pre_two_high_limit:
            if next_high_rate > 5:
                self.enlarge_symbol.append(code)
                self.all_count += 1
                if close == high_limit:
                    self.suc_count += 1


    def syn_backtest(self):
        for i in range(3, len(self.trading_date) - 1):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]
                last_two_date = self.trading_date[i - 2]
                next_date = self.trading_date[i + 1]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])

                # 昨日炸板
                break_limit_symbol_dict = query_mongodb('QuadQuanta', 'daily_break',
                                                        sql={'date': last_date})
                if len(break_limit_symbol_dict) > 0:
                    break_limit_symbol = [symbol_data['code'] for symbol_data in
                                                   break_limit_symbol_dict]
                # if len(last_limit_symbol_data) > 0:
                #     limit_symbol_list = [symboldata['code'] for symboldata in last_limit_symbol_data]
                #     # self.history_N_data = get_bars(limit_symbol_list, end_time=date, count=2)

                    for symbol in break_limit_symbol:
                        if str(symbol).startswith("688") or str(symbol).startswith("30"):
                            continue
                        bars = self.today_data[self.today_data['code'] == symbol]
                        if len(bars) == 1:
                            self.on_day_bar(bars)

                    count_N = 4
                    history_N_data = get_bars(self.symbol, end_time=next_date, count=count_N)

                    for symbol in self.symbol:
                        bars = history_N_data[history_N_data["code"] == symbol]
                        if len(bars) == count_N:
                            self.pre_day_bar(bars)

                logger.info(f"{date}")
                if len(self.enlarge_symbol) > 0:
                    logger.info(f"{self.enlarge_symbol}")

                self.daiyl_symbol = []
                self.symbol = []
                self.enlarge_symbol = []

            except Exception as e:
                print(e)
                continue


def daily_replay():
    # try:
    #     update_day_bar()
    # except Exception as e:
    #     print(e)
    logger.info("炸板反包")
    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = Break2Limit(start_date='2020-01-01',
                         end_date='2023-01-18',
                         frequency='daily')
    # replay = EnlargeTrend(start_date=start_time,
    #                       end_date=end_time,
    #                       frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
