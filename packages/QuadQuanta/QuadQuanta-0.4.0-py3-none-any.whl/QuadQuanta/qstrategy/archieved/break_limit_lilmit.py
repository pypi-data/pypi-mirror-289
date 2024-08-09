# -*-coding:utf-8-*-
# 大成交炸板次日平开再次触及涨停

import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy

from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_bars
import datetime
from QuadQuanta.data.update_data import update_day_bar
from QuadQuanta.data.save_data import save_securities_info


class LargeAmountBreak(BaseStrategy):
    # 定义
    high_amount_limit = 9
    low_amount_limit = 6

    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(LargeAmountBreak, self).__init__(code, start_date, end_date,
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
        pre_bar = bars[-2]
        today_bar = bars[-1]
        code = today_bar["code"]

        high = round(today_bar['high'], 2)
        high_limit = round(today_bar['high_limit'], 2)
        close = round(today_bar['close'], 2)
        pre_close = round(pre_bar['close'], 2)
        pre_open = round(pre_bar['open'], 2)

        pre_amount = round(pre_bar['amount'])

        if self.low_amount_limit * pow(10, 8) < pre_amount < self.high_amount_limit * pow(10, 8):
            if pre_open < pre_close:

                if high == high_limit:
                    self.all_count += 1
                    self.res_symbol.append(code)
                    if close == high_limit:
                        self.res_count += 1

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                self.res_symbol = []
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]
                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code'])
                self.break_limit_dict = []
                self.break_limit_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': last_date})
                self.break_limit_symbols = [symbol_data['code'] for symbol_data in self.break_limit_dict]

                for symbol in self.break_limit_symbols:
                    if str(symbol).startswith("30") or str(symbol).startswith("688"):
                        continue
                    else:
                        self.symbol_list.append(symbol)
                self.history_N_data = get_bars(self.symbol_list, end_time=date, count=2)
                for symbol in self.symbol_list:
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 2:
                        self.on_day_bar(bars)
                logger.info(f"{date}")

                if len(self.res_symbol) > 0:
                    logger.info(f"触及涨停标：{self.res_symbol}")
                    logger.info(f"封板成功率：{self.res_count / self.all_count}")


            except Exception as e:
                print(e)
                continue


def daily_replay():
    today = datetime.date.today()

    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = LargeAmountBreak(start_date='2018-05-01',
                              end_date='2023-12-31',
                              frequency='daily')
    logger.info(f"成交量上限：{replay.high_amount_limit} 亿")
    logger.info(f"成交量下限：{replay.low_amount_limit} 亿")

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
