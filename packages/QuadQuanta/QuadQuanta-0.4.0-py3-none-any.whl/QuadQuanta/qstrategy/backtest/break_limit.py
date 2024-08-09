# 炸板股卖点分析


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
        self.break_rate = []
        self.next_open_rate = []
        self.next_close_rate = []
        self.next_high_rate = []
        self.next_avg_rate = []
        self.high_open_rate = []

    def init(self):
        pass

    def on_day_bar(self, bars):
        today_bar = bars[-2]
        next_bar = bars[-1]
        code = today_bar['code']
        open_ = round(today_bar['open'], 2)
        close = round(today_bar['close'], 2)
        amount = round(today_bar['amount'], 2)

        pre_close = round(today_bar['pre_close'], 2)
        close_rate = round(100 * (close - pre_close) / pre_close, 2)

        next_open = round(next_bar['open'], 2)
        next_close = round(next_bar['close'], 2)
        next_high = round(next_bar['high'], 2)
        # next_low = round(next_bar['open'], 2)
        next_avg = round(next_bar['amount'] / next_bar['volume'], 2)
        next_open_rate = round(100 * (next_open - close) / close, 2)
        next_close_rate = round(100 * (next_close - close) / close, 2)
        next_high_rate = round(100 * (next_high - close) / close, 2)
        next_avg_rate = round(100 * (next_avg - close) / close, 2)

        if amount > 2 * pow(10, 8) and next_high_rate > next_open_rate + 4:
            self.symbol.append(code)
            self.break_rate.append(close_rate)
            self.next_open_rate.append(next_open_rate)
            self.next_high_rate.append(next_high_rate)
            self.next_close_rate.append(next_close_rate)
            self.next_avg_rate.append(next_avg_rate)
            self.high_open_rate.append(next_high_rate - next_open_rate)

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                last_date = self.trading_date[i - 1]

                break_limit_symbol_list = query_mongodb('QuadQuanta', 'daily_break', sql={'date': last_date})
                daily_break_symbol = [symbol_data['code'] for symbol_data in break_limit_symbol_list]
                history_N_data = get_bars(daily_break_symbol, end_time=date, count=2)
                for symbol in daily_break_symbol:
                    if str(symbol).startswith("30") or str(symbol).startswith("688"):
                        continue
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == 2:
                        self.on_day_bar(bars)
                logger.info(f"{last_date}")
                logger.info(f"标{self.symbol}")
                # logger.info(f"炸板收盘涨幅{self.break_rate}")
                logger.info(f"次日开盘涨幅{np.average(self.next_open_rate)}")
                logger.info(f"次日最高涨幅{np.average(self.next_high_rate)}")
                logger.info(f"次日收盘涨幅{np.average(self.next_close_rate)}")
                logger.info(f"次日开盘-最高涨幅差{np.average(self.high_open_rate)}")

                self.daiyl_symbol = []
                self.symbol = []
                # self.break_rate = []
                # self.next_open_rate = []
                # self.next_close_rate = []
                # self.next_high_rate = []
                # self.next_avg_rate = []
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
    replay = BreakLimit(start_date='2022-01-29',
                        end_date='2022-04-15',
                        frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
