# 炸板大幅回落，收盘小于4%
# 涨停股次日收盘上涨的概率

# -*-coding:utf-8-*-

import numpy as np
import talib
import time
from QuadQuanta.core.strategy import BaseStrategy

from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_bars
import datetime
from QuadQuanta.data.update_data import update_day_bar
from QuadQuanta.data.save_data import save_securities_info


class LargeBreak(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(LargeBreak, self).__init__(code, start_date, end_date,
                                         frequency)
        self.pre_volume_dict = {}
        self.limit_symbol_list = []
        self.low_limit_symbol_list = []
        self.fall_symbol_list = []
        self.break_symbol_list = []
        self.down_symbol_list = []
        self.res_count = 0
        self.all_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        """
        今日没有突破，明天的涨停突破40个交易日高点
        Parameters
        ----------
        bars

        Returns
        -------

        """
        today_bar = bars[-1]
        code = today_bar["code"]
        pre_close = round(today_bar['pre_close'], 2)
        close = round(today_bar['close'], 2)
        high = round(today_bar['high'], 2)
        low = round(today_bar['low'], 2)
        open_ = round(today_bar['open'], 2)
        avg_price = round(today_bar['amount'] / today_bar['volume'], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        low_rate = 100 * (low - pre_close) / pre_close
        close_rate = 100 * (close - pre_close) / pre_close
        self.all_count += 1
        if close_rate < 4:
            self.res_symbol.append(code)

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                self.res_symbol = []
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]

                for symbol in self.daily_limit_symbol:
                    if str(symbol).startswith("30") or str(symbol).startswith("688"):
                        continue
                    else:
                        self.symbol_list.append(symbol)

                for symbol in self.symbol_list:
                    bars = self.today_data[self.today_data["code"] == symbol]
                    self.on_day_bar(bars)
                logger.info(f"{date}")

                logger.info(f"{self.res_symbol}")


            except Exception as e:
                print(e)
                continue


def daily_replay():

    today = datetime.date.today()


    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = LargeBreak(start_date='2023-01-01',
                        end_date='2023-04-01',
                        frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
