# -*-coding:utf-8-*-
# 大成交炸板 次日拉红

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
        Parameters
        ----------
        bars

        Returns
        -------

        """
        today_bar = bars[-1]
        pre_bar = bars[-2]
        code = today_bar["code"]
        pre_close = round(today_bar['pre_close'], 2)
        pre_2_close = round(pre_bar['pre_close'], 2)
        close = round(today_bar['close'], 2)
        high = round(today_bar['high'], 2)
        pre_high = round(pre_bar['high'], 2)
        low = round(today_bar['low'], 2)
        open_ = round(today_bar['open'], 2)
        pre_amount = round(pre_bar['amount'])
        avg_price = round(today_bar['amount'] / today_bar['volume'], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        pre_high_rate = 100 * (pre_high - pre_2_close) / pre_2_close
        low_rate = 100 * (low - pre_close) / pre_close
        close_rate = 100 * (close - pre_close) / pre_close
        self.all_count += 1
        # 昨日大成交，且冲高
        if pre_amount > self.low_amount_limit * pow(10, 8) and pre_high_rate > 9 and pre_high > pre_close:
            self.res_symbol.append(code)

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                # 每日标的列表
                # 昨日大成交炸板，今日最高大于1%
                self.symbol_list = []
                self.res_symbol = []
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                for symbol in self.code_list:
                    if str(symbol).startswith("30") or str(symbol).startswith("688"):
                        continue
                    else:
                        bar = self.today_data[self.today_data['code'] == symbol][-1]
                        high = round(bar['high'], 2)
                        close = round(bar['close'], 2)
                        amount = bar['amount']
                        pre_close = round(bar['pre_close'], 2)
                        high_rate = 100 * (high - pre_close) / pre_close
                        # 今日最高大于1%，成交大于1亿
                        if high_rate > 9 and amount > pow(10,8) and close < high :
                            self.symbol_list.append(symbol)

                history_N_data = get_bars(self.symbol_list, end_time=date, count=2)
                for symbol in self.symbol_list:
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == 2:
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
    replay = LargeAmountBreak(start_date='2023-01-28',
                              end_date='2023-08-08',
                              frequency='daily')
    logger.info(f"成交量上限：{replay.high_amount_limit} 亿")
    logger.info(f"成交量下限：{replay.low_amount_limit} 亿")

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
