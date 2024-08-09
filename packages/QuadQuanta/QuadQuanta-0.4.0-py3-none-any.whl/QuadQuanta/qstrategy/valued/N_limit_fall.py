# N字涨停成功，次日收盘均价小于0


import sys
import os
import numpy as np
import datetime

from QuadQuanta.core.strategy import BaseStrategy
from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]


class NLimit(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day',
                 **kwargs):
        super().__init__(code, start_date, end_date, frequency, **kwargs)
        self.pre_volume_dict = {}
        self.symbol_list = []
        self.res_symbol = []
        self.break_symbol = []
        self.all_limit = 0
        self.fall_limit = 0


    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        today_bar = bars[-1]
        last_bar= bars[-2]
        code = today_bar['code']
        high_limit = round(today_bar['high_limit'],2)
        close = round(today_bar['close'],2)
        high = round(today_bar['high'],2)
        today_avg = round(today_bar['amount']/today_bar['volume'],2)
        last_high_limit = round(last_bar['high_limit'],2)
        last_high = round(last_bar['high'],2)
        last_close  = round(last_bar['close'],2)
        if last_high_limit == last_close:
            self.all_limit += 1
            if last_close > today_avg:
                self.fall_limit +=1
                self.res_symbol.append(code)



    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]

                last_trade_day = self.trading_date[i-1]
                # 昨日N字
                daily_limit_dict = query_mongodb('QuadQuanta', 'N_limit', sql={
                    '_id': last_trade_day})
                if len(daily_limit_dict) > 0:
                    self.daiyl_N_limit = daily_limit_dict[0]['symbol_list']

                    self.history_N_data = get_bars(self.daiyl_N_limit, end_time=date, count=2)

                    for symbol in self.daiyl_N_limit:
                        if str(symbol).startswith('688') or str(symbol).startswith('30'):
                            continue
                        bars = self.history_N_data[self.history_N_data['code'] == symbol]
                        if len(bars) == 2:
                            self.on_day_bar(bars)
                    logger.info(f"日期{date}")
                    if len(self.res_symbol) > 0:
                        logger.info(f"N字涨停亏损{self.res_symbol}")
                    logger.info(f"总涨停{self.all_limit}亏损总数:{self.fall_limit}")
                else:
                    continue

                self.res_symbol = []
                self.break_symbol = []
            except Exception as e:
                logger.warning(f"{date}:{e}")
                continue


def n_limit():
    logger.info(f"filename:{FILENAME}.py, N字板")

    test = NLimit(start_date='2022-01-01',
                  end_date='2022-09-01',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
