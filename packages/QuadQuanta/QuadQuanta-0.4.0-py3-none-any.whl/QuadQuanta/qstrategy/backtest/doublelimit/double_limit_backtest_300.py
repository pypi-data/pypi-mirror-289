# -*-coding:utf-8-*-


# 创业板连扳标
import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
# from QuadQuanta.data.clickhouse_api import query_clickhouse
# from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_securities_info
from pymongo.errors import DuplicateKeyError
import datetime
from QuadQuanta.data.update_data import update_day_bar


class DailyDoubleReplay(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(DailyDoubleReplay, self).__init__(code, start_date, end_date,
                                                frequency)
        self.pre_volume_dict = {}
        self.limit_symbol_list = []
        self.fall_symbol_list = []
        self.break_symbol_list = []
        self.double_symbol_list = []
        self.pre_data_dict = {}

    def init(self):
        self.all_securities_info = get_securities_info(format='pandas')

    def on_day_bar(self, bar):
        code = bar['code']

        close = round(bar['close'], 2)
        high = round(bar['high'], 2)
        limit = round(bar['high_limit'], 2)
        low = round(bar['low'], 2)
        amount = bar['amount']
        volume = bar['volume']
        symbol_data = {}
        current_day = bar['date']
        current_date = datetime.date.fromisoformat(current_day)
        pre_close = bar['pre_close']
        high_rate = 100 * (high - pre_close) / pre_close
        try:
            pre_data = self.pre_data_dict[code]

            pre_high_limit = round(pre_data['high_limit'], 2)
            pre_high = round(pre_data['high'], 2)
            pre_close = round(pre_data['close'], 2)
            pre_close_rate = 100 * (pre_data['close'] - pre_data['pre_close']) / pre_data['pre_close']

            if close == limit and high_rate > 9:
                # if (amount > 1 * pow(10, 8)):
                if pre_close == pre_high_limit:
                    self.double_symbol_list.append(code)

            self.pre_data_dict[code] = bar
        except KeyError:
            self.pre_data_dict[code] = bar
        except DuplicateKeyError:
            pass
        except Exception as e:
            print("on_bar exception:", type(e))

    def syn_backtest(self):
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                last_date = self.trading_date[i - 1]
                self.today_data = self.day_data[self.day_data['date'] == date]
                today_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': date})
                daily_limit_symbol = [symbol_data['code'] for symbol_data in today_limit_dict]
                today_break_limit_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                daily_break_symbol = [symbol_data['code'] for symbol_data in today_break_limit_dict]
                yesterday_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': last_date})
                yesterday_limit_symbol = [symbol_data['code'] for symbol_data in yesterday_limit_dict]
                symbol_list = daily_limit_symbol + daily_break_symbol
                for symbol in symbol_list:
                    if str(symbol).startswith('30') and symbol in yesterday_limit_symbol:
                        self.double_symbol_list.append(symbol)
                logger.info(f"{date}")
                logger.info(f"300连板：{self.double_symbol_list}")

                self.double_symbol_list = []
            except Exception as e:
                print("exception:", e)
                continue


def daily_double_replay():
    today = datetime.date.today()
    end_time = str(today)

    # test = DailyDoubleReplay(start_date=start_time,
    #                          end_date=end_time,
    #                          frequency='daily')
    test = DailyDoubleReplay(start_date='2022-01-01',
                             end_date='2023-07-31',
                             frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    daily_double_replay()
