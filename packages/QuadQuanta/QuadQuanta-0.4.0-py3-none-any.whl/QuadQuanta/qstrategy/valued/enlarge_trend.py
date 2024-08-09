# 大成交放量趋势策略
# 突然放量股 成交量大于昨日2倍 涨幅大于5 成交量大于8亿
# MA5 > MA10 趋势向上

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


class EnlargeTrend(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(EnlargeTrend, self).__init__(code, start_date, end_date,
                                           frequency)
        self.pre_volume_dict = {}
        self.large_limit_symbol_list = []
        self.daiyl_symbol = []
        self.symbol = []

    def init(self):
        pass

    def select_symbol(self, bar):
        code = bar['code']
        amount = bar['amount']
        close = round(bar['close'], 2)
        pre_close = round(bar['pre_close'], 2)
        close_rate = 100 * (close - pre_close) / pre_close
        if amount > 8 * pow(10, 8) and close_rate > 5:
            self.daiyl_symbol.append(code)

    def on_day_bar(self, bars):
        today_bar = bars[-1]
        pre_bar = bars[-2]
        code = today_bar['code']
        # close = round(today_bar['close'], 2)
        # high = round(today_bar['high'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)
        amount = today_bar['amount']
        pre_amount = pre_bar['amount']
        pre_close = round(today_bar['pre_close'], 2)
        MA5 = talib.SMA(bars['close'], 5)[-1]
        MA10 = talib.SMA(bars['close'], 10)[-1]
        if MA5 >= MA10 and amount > 1.8 * pre_amount:
            # 昨日未涨停
            if pre_close < pre_limit:

                self.symbol.append(code)


    def syn_backtest(self):
        for i in range(0, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                for bar in self.today_data:
                    self.select_symbol(bar)

                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=10)
                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688') or str(symbol).startswith('30'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 10:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                logger.info(f"{self.symbol}")

                self.daiyl_symbol = []
                self.symbol = []

            except Exception as e:
                print(e)
                continue


def daily_replay():
    try:
        update_day_bar()
    except Exception as e:
        print(e)
    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = EnlargeTrend(start_date='2018-07-01',
                       end_date='2018-10-01',
                       frequency='daily')
    # replay = EnlargeTrend(start_date=start_time,
    #                       end_date=end_time,
    #                       frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
