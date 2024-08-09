#-*-coding:utf-8-*- 
# 成交量大于近20交易日最高交易量1.5倍



# 连续两天触及涨停
import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse
from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from pymongo.errors import DuplicateKeyError

class DailyEnlargeVolume(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(DailyEnlargeVolume, self).__init__(code, start_date, end_date,
                                                 frequency)
        self.pre_volume_dict = {}
        self.limit_symbol_list = []
        self.fall_symbol_list = []
        self.break_symbol_list = []
        self.enlarge_symbol_list = []
        self.pre_data_dict = {}

    def init(self):
        self.all_securities_info = get_securities_info(format='pandas')

    def on_day_bar(self, bar):
        code = bar['code']

        close = round(bar['close'], 2)
        date = bar['date']
        high = round(bar['high'], 2)
        _open = round(bar['open'], 2)
        limit = round(bar['high_limit'], 2)
        low = round(bar['low'], 2)
        amount = bar['amount']
        volume = bar['volume']
        symbol_data = {}
        current_day = bar['date']
        current_date = datetime.date.fromisoformat(current_day)
        pre_close = bar['pre_close']
        high_rate = 100 * (high - pre_close) / pre_close
        open_rate = 100 * (_open - pre_close) / pre_close
        try:
            pre_data = self.pre_data_dict[code]
            pre_volume = pre_data['volume']

            # pre_high_limit = round(pre_data['high_limit'], 2)
            # pre_high = round(pre_data['high'], 2)
            # pre_close = round(pre_data['close'], 2)
            # pre_close_rate = 100 * (pre_data['close'] - pre_data['pre_close']) / pre_data['pre_close']
            if high_rate > 5 and amount > 1 * pow(10, 8):

                if volume > 2 * pre_volume:
                    start_date = datetime.date.fromisoformat(self.all_securities_info.loc[code]['start_date'])
                    if current_date - start_date > datetime.timedelta(days=100):
                        history_30_data = get_bars(code, end_time=date, count=30) [:-1]

                        max_30_volume = np.max(history_30_data['volume'])
                        if volume > 1.5 * max_30_volume:
                            self.enlarge_symbol_list.append(code)

            self.pre_data_dict[code] = bar
        except KeyError:
            self.pre_data_dict[code] = bar
        except DuplicateKeyError:
            pass
        except Exception as e:
            print("on_bar exception:", type(e))

    def syn_backtest(self):
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])
                for bar in self.today_data:
                    if str(bar['code']).startswith('688'):
                        continue
                    self.on_day_bar(bar)
                logger.info(f"{date}")
                logger.info(f"放量超过近期20天：{self.enlarge_symbol_list}")
                # if len(self.enlarge_symbol_list) > 0:
                #     save_mongodb('QuadQuanta', 'daily_enlarge_volume_limit', {'_id': date, 'symbol_list': self.enlarge_symbol_list})
                self.enlarge_symbol_list = []
            except Exception as e:
                print("exception:", e)
                continue


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
    test = DailyEnlargeVolume(start_date=start_time,
                              end_date=end_time,
                              frequency='daily')
    # test = DailyDoubleReplay(start_date='2019-05-01',
    #                          end_date='2019-05-28',
    #                          frequency='daily')

    test.syn_backtest()
