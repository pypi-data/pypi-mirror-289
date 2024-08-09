# 缩量反包
# 取三日数据，昨日阴线，前日阳线，今日收盘大于昨日开盘价。缩量


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


class ShrinkOver(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(ShrinkOver, self).__init__(code, start_date, end_date,
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
        open_ = round(bar['open'], 2)
        pre_close = round(bar['pre_close'], 2)
        close_rate = 100 * (close - pre_close) / pre_close
        # 选股成交量大于1，阳线
        if amount > 1 * pow(10, 8) and close_rate > 0 and close > open_:
            self.daiyl_symbol.append(code)

    def on_day_bar(self, bars):
        today_bar = bars[-1]
        pre_bar = bars[-2]
        pre_two_bar = bars[-3]
        code = today_bar['code']
        # close = round(today_bar['close'], 2)
        # high = round(today_bar['high'], 2)
        today_close = round(today_bar['close'], 2)
        today_volume = today_bar['volume']
        pre_volume = pre_bar['volume']
        pre_close = round(today_bar['pre_close'], 2)
        pre_open = round(pre_bar['open'], 2)
        pre_two_open = round(pre_two_bar['open'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_two_low = round(pre_two_bar['low'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)
        pre_two_amount = pre_two_bar['amount']
        # 振幅
        pre_two_rate = 100 * (pre_two_high - pre_two_low) / pre_two_low

        if pre_two_close > pre_two_open and pre_two_rate > 5 and pre_two_amount > 2 * pow(10,8):
            if pre_close < pre_open:
                if today_volume < pre_volume and today_close > pre_open:
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

                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=3)
                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688') or str(symbol).startswith('30'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 3:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                if len(self.symbol) > 0:
                    save_mongodb('QuadQuanta', 'enlarge_trend',
                                 {'_id': date, 'symbol_list': self.symbol})
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
    replay = ShrinkOver(start_date='2023-03-01',
                        end_date='2023-03-05',
                        frequency='daily')
    # replay = ShrinkOver(start_date=start_time,
    #                     end_date=end_time,
    #                     frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
