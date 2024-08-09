# -*-coding:utf-8-*-
# 炸板两日N字涨停次日涨停


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
        self.success_count = 0
        self.all_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        today_bar = bars[-1]
        code = today_bar['code']
        high_limit = round(today_bar['high_limit'], 2)
        close = round(today_bar['close'], 2)
        high = round(today_bar['high'], 2)
        self.all_count += 1
        if high == high_limit:
            self.res_symbol.append(code)
            self.success_count += 1
        else:
            self.break_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]

                last_trade_day = self.trading_date[i - 1]
                # 昨日的N字涨停
                daily_limit_dict = query_mongodb('QuadQuanta', 'break_TwoN_limit', sql={
                    '_id': last_trade_day})
                if len(daily_limit_dict) > 0:
                    self.daiyl_N_limit = daily_limit_dict[0]['symbol_list']

                    self.history_N_data = get_bars(self.daiyl_N_limit, end_time=date, count=1)

                    for symbol in self.daiyl_N_limit:
                        if str(symbol).startswith('688') or str(symbol).startswith('30'):
                            continue
                        bars = self.history_N_data[self.history_N_data['code'] == symbol]
                        if len(bars) == 1:
                            self.on_day_bar(bars)
                    logger.info(f"日期{date}")
                    all_limit = len(self.res_symbol) + len(self.break_symbol)
                    if all_limit > 0:
                        logger.info(f"涨停{self.res_symbol}")
                        logger.info(f"未涨停{self.break_symbol}")
                        logger.info(f"涨停比例{self.success_count / self.all_count}")
                    # logger.info(f"炸板{self.break_symbol}")
                else:
                    continue

                self.res_symbol = []
                self.break_symbol = []
            except Exception as e:
                logger.warning(f"{date}:{e}")
                continue
        logger.info(f"总涨停{self.success_count}")

def n_limit():
    logger.info(f"filename:{FILENAME}.py, N字板")

    test = NLimit(start_date='2022-01-01',
                  end_date='2022-05-23',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
