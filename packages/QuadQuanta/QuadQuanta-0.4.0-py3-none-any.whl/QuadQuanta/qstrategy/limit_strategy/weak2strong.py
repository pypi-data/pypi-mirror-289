# 弱转强标的 次日走势分析 涨停后走势


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
        amount = round(today_bar['amount'], 2)
        open_rate = 100 * (open_ - pre_close) / pre_close
        # 今日触及涨停标
        if high == high_limit and open_rate > 3 and amount > 1 * pow(10, 8):
            self.symbol.append(code)
            self.all_count += 1
            if close == high_limit:
                self.suc_count += 1

    def pre_day_bar(self, bars):
        today_bar = bars[-2]
        code = today_bar['code']
        close = round(today_bar['close'], 2)
        open_ = round(today_bar['open'], 2)
        pre_close = round(today_bar['pre_close'], 2)
        high = round(today_bar['high'], 2)
        high_limit = round(today_bar['high_limit'], 2)
        amount = round(today_bar['amount'], 2)
        open_rate = 100 * (open_ - pre_close) / pre_close
        if close < high_limit:
            self.enlarge_symbol.append(code)

    def syn_backtest(self):
        for i in range(3, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]
                last_two_date = self.trading_date[i - 2]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])

                all_N_limit_symbol = []
                limit_type = ['daily_limit']
                # 昨日涨停标数据
                last_limit_symbol_data = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_date})
                if len(last_limit_symbol_data) > 0:
                    limit_symbol_list = [symboldata['code'] for symboldata in last_limit_symbol_data]
                    # self.history_N_data = get_bars(limit_symbol_list, end_time=date, count=2)
                    # 昨日炸板
                    # break_limit_symbol_dict = query_mongodb('QuadQuanta', 'daily_break',
                    #                                      sql={'date': last_date})
                    # break_limit_symbol = [symbol_data['code'] for symbol_data in
                    #                                break_limit_symbol_dict]

                    for symbol in limit_symbol_list:
                        # if symbol in breakup_symbol :
                        #         self.symbol.append(symbol)
                        if str(symbol).startswith("688") or str(symbol).startswith("30"):
                            continue
                        bars = self.today_data[self.today_data['code'] == symbol]
                        if len(bars) == 1:
                            self.on_day_bar(bars)

                    count_N = 3
                    history_N_data = get_bars(self.symbol, end_time=date, count=count_N)

                    for symbol in self.symbol:
                        bars = history_N_data[history_N_data["code"] == symbol]
                        if len(bars) == count_N:
                            self.pre_day_bar(bars[:-1])

                logger.info(f"{date}")
                logger.info(f"{self.enlarge_symbol}")
                logger.info(f"封板成功率{self.suc_count / self.all_count}")

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
    logger.info("二板涨停")
    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = N_limit_next(start_date='2018-01-01',
                          end_date='2019-11-18',
                          frequency='daily')
    # replay = EnlargeTrend(start_date=start_time,
    #                       end_date=end_time,
    #                       frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
