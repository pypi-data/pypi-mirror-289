# 近10日连扳股
import sys
import os
import numpy as np

import talib
from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb

from QuadQuanta.data.get_data import get_trade_days, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]


class DailyTenDoubleLimit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day',
                 **kwargs):
        super().__init__(code, start_date, end_date, frequency, **kwargs)
        self.pre_volume_dict = {}
        self.limit_symbol_list = []
        self.ever_limit_symbol_list = []
        self.res_symbol = []
        self.res_two_symbol = []
        self.res_break_symbol = []
        self.start_date = start_date

    def init(self):
        pass

    def on_day_bar(self, bars):
        bar = bars[-1]
        pre_bar = bars[-2]
        code = bar['code']

        close = round(bar['close'], 2)
        pre_close = round(pre_bar['close'], 2)
        pre_two_close = round(pre_bar['pre_close'], 2)
        _open = round(bar['open'], 2)
        high = round(bar['high'], 2)

        limit = round(bar['high_limit'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)

        low = round(bar['low'], 2)
        amount = bar['amount']
        high_rate = 100 * (high - pre_close) / pre_close
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close

        if high == limit and bar['volume'] and high_rate > 6:
            max_high = round(np.max(bars[:-1]['high']), 2)
            if (amount > 0.2 * pow(10, 8)) and high < max_high:
                MA10 = round(talib.SMA(bars['close'], 10)[-1], 2)
                if close > MA10 and pre_close < pre_limit:
                    if close == limit:
                        self.limit_symbol_list.append(code)
                    else:
                        self.ever_limit_symbol_list.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                until_trade_days = get_trade_days(start_time='2018-01-01', end_time=date)
                last_trade_day = until_trade_days[-2]
                last_two_trade_day = until_trade_days[-3]
                last_ten_trade_day = until_trade_days[-7]
                last_ten_double_limit_dict = query_mongodb('QuadQuanta', 'daily_double_limit',
                                                           sql={'_id': {'$gte': last_ten_trade_day,
                                                                        '$lte': last_two_trade_day}})
                last_ten_double_limit_symbol_tmp = [symbol_data['symbol_list'] for symbol_data in
                                                    last_ten_double_limit_dict]
                last_ten_double_limit_symbol = [symbol for symbol_list in last_ten_double_limit_symbol_tmp for symbol in
                                                symbol_list]
                last_ten_double_limit_symbol = list(set(last_ten_double_limit_symbol))
                history_N_data = get_bars(last_ten_double_limit_symbol, end_time=date, count=10)

                for symbol in last_ten_double_limit_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = history_N_data[history_N_data['code'] == symbol]
                    if len(bars) == 10:
                        self.on_day_bar(bars)
                logger.info(f"近10日连板股{date}:{self.limit_symbol_list}")
                logger.info(f"未上板近10日连板股{date}:{self.ever_limit_symbol_list}")
                rate = 100 * len(self.limit_symbol_list) / (len(self.ever_limit_symbol_list) + len(self.limit_symbol_list))
                logger.info(f"上板比例{date}:{rate}")

                self.res_symbol = []
                self.limit_symbol_list = []
                self.ever_limit_symbol_list = []
            except Exception as e:
                logger.warning(e)
                continue


if __name__ == '__main__':
    import datetime

    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-3]
    # test = DailyTenDoubleLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily', solid=True)
    test = DailyTenDoubleLimit(start_date='2022-04-01',
                               end_date='2022-04-30',
                               frequency='daily', solid=True)
    test.syn_backtest()
