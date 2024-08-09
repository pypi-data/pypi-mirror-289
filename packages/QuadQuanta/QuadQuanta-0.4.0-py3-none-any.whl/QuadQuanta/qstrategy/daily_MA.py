# -*-coding:utf-8-*-
# 计算每日MA，并保存至clickhouse数据库

import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse
from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_bars


class DailyMA(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(DailyMA, self).__init__(code, start_date, end_date,
                                      frequency)

    def init(self):
        self.daily_MA = []
    @staticmethod
    def moving_average(x, w):
        # 求移动平均线
        return np.convolve(x, np.ones(w), 'valid') / w

    def on_day_bar(self, bars):
        close_np = bars['close']
        code = bars['code'][-1]

        MA_dict = {}
        MA5 = round(self.moving_average(close_np, 5)[-1], 2)
        MA10 = round(self.moving_average(close_np, 10)[-1], 2)
        MA20 = round(self.moving_average(close_np, 20)[-1], 2)
        MA60 = round(self.moving_average(close_np, 60)[-1], 2)
        MA_dict['MA5'] = MA5
        MA_dict['MA10'] = MA10
        MA_dict['MA20'] = MA20
        MA_dict['MA60'] = MA60
        MA_dict['_id'] = self.currentdate + '-' + code
        MA_dict['date'] = self.currentdate
        MA_dict['code'] = code
        self.daily_MA.append(MA_dict)

    def syn_backtest(self):
        for i in range(0, len(self.trading_date)):
            self.daily_MA = []
            self.currentdate = self.trading_date[i]
            history_N_data = get_bars(end_time=self.currentdate, count=60)
            code_list = list(set(history_N_data['code']))
            for code in code_list:
                bars = history_N_data[history_N_data['code'] == code]
                self.on_day_bar(bars)
            logger.info(f"{self.currentdate} - 保存数据")
            insert_mongodb('QuadQuanta', 'dayil_MA', self.daily_MA)


if __name__ == '__main__':

    import datetime
    from QuadQuanta.data.update_data import update_day_bar

    try:
        update_day_bar()
    except Exception as e:
        print(e)
    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    test = DailyMA(start_date='2021-01-01',
                       end_date='2022-01-01',
                       frequency='daily')
    # test = DailyMA(start_date=start_time,
    #                end_date=end_time,
    #                frequency='daily')

    test.syn_backtest()
