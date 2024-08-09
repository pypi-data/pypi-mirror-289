# -*-coding:utf-8-*-
# N 字涨停次日涨停

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
# 振幅
Amplitude = 6


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
        pre_bar = bars[-2]
        pre_two_bar = bars[-3]
        pre_three_bar = bars[-4]

        code = today_bar['code']
        high_limit = round(today_bar['high_limit'], 2)
        close = round(today_bar['close'], 2)
        open_price = round(today_bar['open'], 2)
        pre_close = round(today_bar['pre_close'], 2)
        high = round(today_bar['high'], 2)
        low = round(today_bar['low'], 2)
        today_close_rate = 100 * (close - pre_close) / pre_close
        today_high_rate = 100 * (high - pre_close) / pre_close
        today_low_rate = 100 * (low - pre_close) / pre_close
        avg = round(today_bar['amount'] / today_bar['volume'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_open = round(pre_bar['open'], 2)

        # 收益率
        earn_rate = 100 * (high - pre_high) / pre_high

        pre_two_open = round(pre_two_bar['open'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)
        pre_two_low = round(pre_two_bar['low'], 2)
        pre_two_close = round(pre_two_bar['close'], 2)
        pre_three_close = round(pre_two_bar['pre_close'], 2)
        pre_two_down_rate = 100 * (pre_two_close - pre_two_open) / pre_two_close

        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close

        pre_two_close_rate = 100 * (pre_two_close - pre_three_close) / pre_three_close

        pre_two_rate = 100 * (pre_two_high - pre_two_low) / pre_two_low
        # 下隐线长度
        pre_two_downline_rate = 100 * (pre_two_close - pre_two_low) / pre_two_low

        pre_three_bar = bars[-4]

        pre_three_close = round(pre_three_bar['close'], 2)
        pre_four_close = round(pre_three_bar['pre_close'], 2)
        pre_three_close_rate = 100 * (pre_three_close - pre_four_close) / pre_four_close

        if pre_two_close_rate < -1 and pre_open_rate > -5 and pre_two_downline_rate < 4:
            self.all_count += 1
            # if today_high_rate > 5:
            if earn_rate < 0:
                self.res_symbol.append(code)
                self.success_count += 1
            else:
                self.break_symbol.append(code)

            # if high == high_limit:
            #     # if pre_two_close * 1.1 > max(pre_three_close, pre_two_high) *1.05:
            #         if close == high_limit:
            #             self.res_symbol.append(code)
            #             self.success_count += 1
            # else:
            #     self.break_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(1, len(self.trading_date)):
            try:
                date = self.trading_date[i]

                last_trade_day = self.trading_date[i - 1]
                # 昨日的N字涨停
                daily_limit_dict = query_mongodb('QuadQuanta', 'N_limit', sql={
                    '_id': last_trade_day})
                if len(daily_limit_dict) > 0:
                    self.daiyl_N_limit = daily_limit_dict[0]['symbol_list']

                    self.history_N_data = get_bars(self.daiyl_N_limit, end_time=date, count=4)

                    for symbol in self.daiyl_N_limit:
                        if str(symbol).startswith('688') or str(symbol).startswith('30'):
                            continue
                        bars = self.history_N_data[self.history_N_data['code'] == symbol]
                        if len(bars) == 4:
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
        logger.info(f"总涨停{self.all_count}")


def n_limit():
    logger.info(f"filename:{FILENAME}.py   振幅{Amplitude}, N字板")

    test = NLimit(start_date='2022-01-01',
                  end_date='2023-01-30',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
