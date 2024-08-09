# 每日待突破标
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


class DailyReadyBreakup(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(DailyReadyBreakup, self).__init__(code, start_date, end_date,
                                                frequency)
        self.pre_volume_dict = {}
        self.limit_symbol_list = []
        self.low_limit_symbol_list = []
        self.fall_symbol_list = []
        self.break_symbol_list = []
        self.down_symbol_list = []

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
        pre_bar = bars[-2]
        close = round(today_bar['close'], 2)
        # today_volume = today_bar["volume"]
        # pre_volume = pre_bar["volume"]
        # pre_high = round(pre_bar['high'])
        max_40_high = max(bars["high"])
        np.seterr(divide='ignore', invalid='ignore')
        average_price = np.divide(bars['amount'], bars['volume'])
        # average_price = bars['amount'] / bars['volume']

        # print(bars['close'][-11:])
        # last_10_close = np.mean(bars[-6:-1]['close'])
        # first_10_close = np.mean(bars[:6]['close'])
        MA30 = talib.SMA(bars['close'], 30)[-1]
        MA60 = talib.SMA(bars['close'], 60)[-1]
        MA5 = talib.SMA(bars['close'], 5)[-1]

        # 明日涨停突破
        if close * 1.1 >= max_40_high and MA5 > MA60 and MA5 > MA30:

            # 前N日未突破
            for i in range(-3, 0):
                close = round(bars[i]['close'], 2)
                pre_close = round(bars[i]['pre_close'], 2)
                high = round(bars[i]['high'], 2)
                high_rate = 100 * (high - pre_close) / pre_close
                # 用平均价作为最高点
                # max_high = round(max(average_price[:i - 1]), 2)
                max_high = round(max(bars['high'][:i - 1]), 2)

                if close > max_high and high_rate > 3:
                    break
                if i == -1:
                    self.res_symbol.append(code)

    def syn_backtest(self):
        for i in range(0, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                self.res_symbol = []
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                for symbol in self.code_list:
                    if str(symbol).startswith("30") or str(symbol).startswith("688"):
                        continue
                    else:
                        self.symbol_list.append(symbol)
                history_N_data = get_bars(self.symbol_list, end_time=date, count=60)

                for symbol in self.symbol_list:
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == 60:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                logger.info(f"{self.res_symbol}")

            except Exception as e:
                print(e)
                continue


def daily_replay():
    try:
        update_day_bar()
        # 每周一更新股票基本信息
        today = datetime.date.today()
    except Exception as e:
        print(e)

    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    # replay = DailyReplay(start_date='2018-01-01',
    #                    end_date='2021-01-01',
    #                    frequency='daily')
    replay = DailyReadyBreakup(start_date=start_time,
                               end_date=end_time,
                               frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
