# -*-coding:utf-8-*-
# 每日大于10亿以上成交的涨停，找出市场核心
import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
# from QuadQuanta.data.clickhouse_api import query_clickhouse
# from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb,save_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_bars
import datetime
from QuadQuanta.data.update_data import update_day_bar

class DailyReplay(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(DailyReplay, self).__init__(code, start_date, end_date,
                                          frequency)
        self.pre_volume_dict = {}
        self.limit_symbol_list = []
        self.low_limit_symbol_list = []
        self.fall_symbol_list=[]
        self.break_symbol_list=[]


    def init(self):
        pass

    def on_day_bar(self, bars):
        today_bar = bars[-1]
        last_bar = bars[-2]
        code = today_bar['code']
        today_close = round(today_bar['close'], 2)
        today_high = round(today_bar['high'], 2)
        today_limit = round(today_bar['high_limit'], 2)
        today_amount = today_bar['amount']

        last_close = round(last_bar['close'], 2)
        last_high = round(last_bar['high'], 2)
        last_limit = round(last_bar['high_limit'], 2)
        today_high_rate = 100 * (today_high - last_close) / last_close
        if (today_amount > 8 * pow(10, 8)):
                if today_high_rate > 7:
                    self.limit_symbol_list.append(code)


    def syn_backtest(self):
        for i in range(0, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                self.history_N_data = get_bars(end_time=date, count=2)

                for symbol in self.code_list:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 2:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                logger.info(f"大成交活跃股：{self.limit_symbol_list}")

                self.limit_symbol_list = []

            except Exception as e:
                print(e)
                continue

def daily_replay():

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    # replay = DailyReplay(start_date='2022-07-01',
    #                    end_date='2022-09-01',
    #                    frequency='daily')
    replay = DailyReplay(start_date=start_time,
                       end_date=end_time,
                       frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()

