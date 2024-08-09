# -*-coding:utf-8-*-

import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
# from QuadQuanta.data.clickhouse_api import query_clickhouse
# from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb,save_mongodb
from QuadQuanta.data.get_data import get_trade_days
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

    def on_day_bar(self, bar):
        code = bar['code']
        close = round(bar['close'], 2)
        _open = round(bar['open'], 2)
        high = round(bar['high'], 2)
        limit = round(bar['high_limit'], 2)
        low_limit = round(bar['low_limit'], 2)
        low = round(bar['low'], 2)
        amount = bar['amount']
        volume = bar['volume']
        symbol_data = {}
        pre_close = bar['pre_close']
        high_rate = 100 * (high - pre_close) / pre_close
        low_rate = 100 * (low - pre_close) / pre_close
        try:
            #
            # pre_volume = self.pre_volume_dict[code]
            if (amount > 0.1 * pow(10, 8)):
                if high_rate < 6:
                    if close == limit and bar['volume']:
                        self.limit_symbol_list.append(code)
                        symbol_data['_id'] = bar['date'] + '-' + code
                        symbol_data['date'] = bar['date']
                        symbol_data['code'] = code
                        symbol_data['type'] = 'enlarge_limit'

                        save_mongodb('QuadQuanta', 'daily_limit_st', symbol_data)

                        # 炸板
                    if ((high == limit) and (close < limit)):
                        # if ((high == limit) and (100 * (limit - close) / close > 2)):
                        self.break_symbol_list.append(code)
                        symbol_data['_id'] = bar['date'] + '-' + code
                        symbol_data['date'] = bar['date']
                        symbol_data['code'] = code
                        symbol_data['type'] = 'break_limit'

                        save_mongodb('QuadQuanta', 'daily_break_st', symbol_data)
            self.pre_volume_dict[code] = bar['volume']
        except:
            self.pre_volume_dict[code] = bar['volume']

    def syn_backtest(self):
        for i in range(0, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])

                for bar in self.today_data:
                    if str(bar['code']).startswith('688'):
                        continue
                    self.on_day_bar(bar)
                logger.info(f"{date}")
                logger.info(f"涨停ST：{self.limit_symbol_list}")
                logger.info(f"炸板ST:{self.break_symbol_list}")
                self.limit_symbol_list = []
                self.fall_symbol_list = []
                self.break_symbol_list = []
                self.low_limit_symbol_list = []
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
    replay = DailyReplay(start_date='2023-02-01',
                       end_date='2023-03-01',
                       frequency='daily')
    # replay = DailyReplay(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()

