# 两日N字涨停回测
# 突破前高的两日N字和未突破的

import sys
import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
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
        self.res_two_symbol = []
        self.res_break_symbol = []
        self.res_fall_symbol = []
        self.res_test_two_symbol = []
        self.res_open_limit_symbol = []
        self.up_count = 0
        self.down_count = 0

    def init(self):
        pass

    def on_day_bar(self, bars: np.ndarray):
        today_bar = bars[-1]
        pre_bar = bars[-2]
        code = pre_bar['code']
        current_day = bars[-1]['date']
        pre_two_bar = bars[-3]
        pre_three_bar = bars[-4]
        pre_four_bar = bars[-5]
        max_high = round(np.max(bars['high']), 2)
        min_low = round(np.min(bars[1:]['low']), 2)

        today_close = round(today_bar['close'], 2)
        today_limit = round(today_bar['high_limit'], 2)

        pre_close = round(pre_bar['close'], 2)
        pre_open = round(pre_bar['open'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_low = round(pre_bar['low'], 2)
        pre_limit = round(pre_bar['high_limit'], 2)
        pre_volume = pre_bar['volume']

        pre_two_close = round(pre_two_bar['close'], 2)
        pre_two_high = round(pre_two_bar['high'], 2)
        pre_two_limit = round(pre_two_bar['high_limit'], 2)
        pre_two_open = round(pre_two_bar['open'], 2)
        pre_two_volume = pre_two_bar['volume']

        pre_three_close = round(pre_three_bar['close'], 2)
        pre_three_low = round(pre_three_bar['low'], 2)
        pre_three_limit = round(pre_three_bar['high_limit'], 2)
        pre_three_high = round(pre_three_bar['high'], 2)

        pre_high_rate = 100 * (pre_high - pre_two_close) / pre_two_close
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        pre_open_rate = 100 * (pre_open - pre_two_close) / pre_two_close
        pre_two_high_rate = 100 * (pre_two_high - pre_three_close) / pre_three_close
        pre_two_close_rate = 100 * (pre_two_close - pre_three_close) / pre_three_close

        pre_four_close = round(pre_four_bar['close'], 2)
        pre_four_limit = round(pre_four_bar['high_limit'], 2)
        # 昨日振幅
        pre_alp_rate = 100 * (pre_high - pre_low) / pre_low

        if pre_three_close == pre_three_limit and pre_two_close < pre_two_limit:
            if pre_four_close < pre_four_limit and pre_close < pre_limit:
                # 涨停价格未突破高点
                if pre_close * 1.1 < max(pre_two_high,pre_three_high) * 1.02:
                    if today_close == today_limit:
                        self.up_count+= 1
                    else:
                        self.down_count += 1
                    self.res_two_symbol.append(code)




    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]
                date_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                # print(date_date)

                # self.today_data = self.day_data[self.day_data['date'] == date]
                # self.code_list = np.unique(self.today_data['code'])
                self.daily_limit_dict = []
                self.daily_limit_dict = query_mongodb('QuadQuanta', 'daily_limit', sql={
                    'date': date})
                self.daily_limit_symbol = [symbol_data['code'] for symbol_data in self.daily_limit_dict]
                self.daily_break_symbol = []
                self.daily_break_dict = query_mongodb('QuadQuanta', 'daily_break', sql={
                    'date': date})
                self.daily_break_symbol = [symbol_data['code'] for symbol_data in self.daily_break_dict]
                self.daiyl_symbol = self.daily_limit_symbol + self.daily_break_symbol
                self.history_N_data = get_bars(self.daiyl_symbol, end_time=date, count=5)

                for symbol in self.daiyl_symbol:
                    if str(symbol).startswith('688'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 5:
                        self.on_day_bar(bars)
                logger.info(f"日期{date}")

                # 查询前10日N字是否涨停模式
                # logger.info(f"测试两天N字板:{self.res_test_two_symbol}")
                if len(self.res_two_symbol) > 0:
                    logger.info(f"未突破前高两天N字板:{self.res_two_symbol}")
                    logger.info(f"涨停个数{self.up_count}，炸板个数{self.down_count}")

                    # logger.info(f"两天N字板:{res_symbol}")
                self.res_symbol = []
                self.res_two_symbol = []
                self.res_test_two_symbol = []
                self.res_break_symbol = []
                self.res_fall_symbol = []
                self.res_open_limit_symbol = []

                # print(f"N字成功连板:{next_date} - {N_type_limit}")
                # print(f"炸板N字成功连板:{next_date} - {break_limit}")
                # print(f"两日N字成功连板:{next_date} - {two_limit}")

            except Exception as e:
                logger.warning(e)
                continue


def n_limit():
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-3]
    # test = NLimit(start_date=start_time,
    #               end_date=end_time,
    #               frequency='daily')
    test = NLimit(start_date='2021-02-01',
                  end_date='2021-04-30',
                  frequency='daily')

    test.syn_backtest()


if __name__ == '__main__':
    n_limit()
