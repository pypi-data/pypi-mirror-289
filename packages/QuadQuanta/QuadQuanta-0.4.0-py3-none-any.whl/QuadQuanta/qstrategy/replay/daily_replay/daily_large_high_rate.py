# 每日大成交冲高标 最高到大于9%
# -*-coding:utf-8-*-
# 大成交冲高到+9以上次日平开再次触及涨停

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
        pass

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
                        bar = self.today_data[self.today_data['code'] == symbol][-1]
                        high = round(bar['high'], 2)
                        high_limit = round(bar['high_limit'], 2)
                        pre_close = round(bar['pre_close'], 2)
                        close = round(bar['close'], 2)
                        open_ = round(bar['open'], 2)
                        amount = bar['amount']
                        if amount > self.low_amount_limit * pow(10, 8):
                            high_rate = 100 * (high - pre_close) / pre_close
                            if high_rate > 9:
                                self.symbol_list.append(symbol)

                logger.info(f"{date}")

                if len(self.symbol_list) > 0:
                    logger.info(f"冲高到+9 大成交标：{self.symbol_list}")


            except Exception as e:
                print(e)
                continue


def daily_replay():
    today = datetime.date.today()

    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = LargeAmountBreak(start_date=start_time,
                              end_date=end_time,
                              frequency='daily')
    # logger.info(f"成交量上限：{replay.high_amount_limit} 亿")
    logger.info(f"成交量下限：{replay.low_amount_limit} 亿")

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
