# 大成交放量趋势策略
# 突然放量股 成交量大于昨日2倍 涨幅大于5 成交量大于8亿
# MA5 > MA10 趋势向上
# 第一类买点，开盘买点：
# 1、要保证开盘拉升成交额逐步放大，不能拉升第一分钟的成交最大，拉升有量，下砸缩量
# 2、拉升的量要大于前一段下砸的量
# 第二类买点午后买点，保证今日是阳线 收盘大于昨日收盘价

import numpy as np
import time
from QuadQuanta.core.strategy import BaseStrategy
# from QuadQuanta.data.clickhouse_api import query_clickhouse
# from QuadQuanta.portfolio import Account
from QuadQuanta.utils.logs import logger
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb
from QuadQuanta.data.get_data import get_trade_days, get_bars
import datetime
from QuadQuanta.data.update_data import update_day_bar
import talib


class EnlargeTrend(BaseStrategy):
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        super(EnlargeTrend, self).__init__(code, start_date, end_date,
                                           frequency)
        self.pre_volume_dict = {}
        self.large_limit_symbol_list = []
        self.daiyl_symbol = []
        self.symbol = []

    def init(self):
        pass


    def on_day_bar(self, bars):
        today_bar = bars[-1]
        pre_bar = bars[-2]
        code = today_bar['code']
        close = round(today_bar['close'], 2)
        pre_close = round(pre_bar['close'], 2)
        pre_high = round(pre_bar['high'], 2)
        pre_two_close = round(pre_bar['pre_close'], 2)
        high = round(today_bar['high'], 2)
        pre_high_limit = round(pre_bar['high_limit'], 2)
        high_rate = 100 * (high - pre_two_close)/pre_two_close
        pre_close_rate = 100 * (pre_close - pre_two_close)/pre_two_close
        pre_high_rate = 100 * (pre_high - pre_two_close)/pre_two_close

        if pre_high_rate > 1:
            self.symbol.append(code)
        # if pre_high == pre_high_limit:
        #     self.symbol.append(code)



    def syn_backtest(self):
        for i in range(2, len(self.trading_date)):
            try:
                # 每日标的列表
                self.symbol_list = []
                date = self.trading_date[i]
                last_two_date = self.trading_date[i-2]
                self.today_data = self.day_data[self.day_data['date'] == date]
                self.code_list = np.unique(self.today_data['code'])

                enlarge_trend_symbol_dict = query_mongodb('QuadQuanta', 'enlarge_trend', sql={
                    '_id': last_two_date})[-1]
                enlarge_trend_symbol = enlarge_trend_symbol_dict['symbol_list']
                self.history_N_data = get_bars(enlarge_trend_symbol, end_time=date, count=3)
                for symbol in enlarge_trend_symbol:
                    if str(symbol).startswith('688') or str(symbol).startswith('30'):
                        continue
                    bars = self.history_N_data[self.history_N_data['code'] == symbol]
                    if len(bars) == 3:
                        self.on_day_bar(bars)
                logger.info(f"{date}")
                logger.info(f"{self.symbol}")
                logger.info(f"{len(self.symbol)/len(enlarge_trend_symbol)}")

                self.daiyl_symbol = []
                self.symbol = []

            except Exception as e:
                print(e)
                continue


def daily_replay():
    # try:
    #     update_day_bar()
    # except Exception as e:
    #     print(e)
    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time='2014-01-01',
                                            end_time=end_time)
    start_time = trade_days_until_today[-2]
    replay = EnlargeTrend(start_date='2022-04-01',
                       end_date='2022-10-11',
                       frequency='daily')
    # replay = EnlargeTrend(start_date=start_time,
    #                       end_date=end_time,
    #                       frequency='daily')

    replay.syn_backtest()


if __name__ == '__main__':
    daily_replay()
