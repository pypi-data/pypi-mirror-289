# -*-coding:utf-8-*-
# 每日突破前高，配合板块突破。买点在于情绪节点和回踩位置
# 突破40日高点, 昨日未突破

import sys
import os
import numpy as np
import datetime
from QuadQuanta.data.update_data import update_day_bar
from QuadQuanta.core.strategy import BaseStrategy

# from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
# from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb

# from QuadQuanta.portfolio import Account
from QuadQuanta.data.get_data import get_trade_days, get_securities_info, get_bars
from QuadQuanta.utils.logs import logger

FILENAME = os.path.basename(sys.argv[0]).split(".py")[0]
# 振幅
Amplitude = 6


class DailyNLimit(BaseStrategy):
    def __init__(
            self, code=None, start_date=None, end_date=None, frequency="day", **kwargs
    ):
        super().__init__(code, start_date, end_date, frequency, **kwargs)
        self.pre_volume_dict = {}
        self.symbol_list = []
        self.res_symbol = []
        self.success_symbol = []
        self.fail_symbol = []
        self.hold_symbol = []

        self.start_date = start_date

    def init(self):
        pass

    def pick_symbol(self, bar):
        """
        初选标，涨停，成交额大于1亿
        Parameters
        ----------
        bar

        Returns
        -------

        """
        code = bar["code"]
        high = round(bar["high"], 2)
        open_ = round(bar["open"], 2)
        high_limit = round(bar["high_limit"], 2)
        close = round(bar["close"], 2)
        pre_close = round(bar["pre_close"], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        close_rate = 100 * (close - pre_close) / pre_close
        # open_rate = 100 * (open_ - pre_close) / pre_close
        amount = bar["amount"]

        if amount > pow(10, 8):
            if high_rate > 8:
                # if high_rate - close_rate > 4.5:
                if high_limit == close:
                    self.symbol_list.append(code)

    def on_day_bar(self, bars: np.ndarray):
        """
        收盘突破30日最高点，再通过K线观测是否是横盘突破
        Parameters
        ----------
        bars

        Returns
        -------

        """
        today_bar = bars[-1]
        code = today_bar["code"]
        pre_bar = bars[-2]
        pre_high_limit = round(pre_bar["high_limit"], 2)
        # today_volume = today_bar["volume"]
        # pre_volume = pre_bar["volume"]
        # pre_high = round(pre_bar['high'])
        # max_20_high = max(bars[20:-1]["close"])
        # min_20_low = min(bars[20:-1]["close"])
        max_N_high = max(bars[:-1]["high"])

        today_high = round(today_bar["high"], 2)
        pre_close = round(today_bar["pre_close"], 2)
        pre_two_close = round(pre_bar["pre_close"], 2)
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        today_high_rate = 100 * (today_high - pre_close) / pre_close
        # print(bars['close'][-11:])
        # MA60 = talib.SMA(bars['close'], 60)[60:]
        # # 30收盘价价序列
        # close_60 = bars['close'][60:]

        if today_high > max_N_high and pre_close_rate < 9.8:
            self.res_symbol.append(code)

    def next_day_backtest(self, bars):
        """
        次N日回测
        Returns
        -------

        """
        final_bar = bars[-1]
        final_two_bar = bars[-2]
        symbol = final_bar['code']
        final_close = round(final_bar['close'], 2)
        final_pre_close = round(final_bar['pre_close'], 2)
        final_high = round(final_bar['high'], 2)
        final_open = round(final_bar['open'], 2)
        final_high_limit = round(final_bar['high_limit'], 2)

        final_two_high = round(final_two_bar['high'], 2)
        final_two_high_limit = round(final_two_bar['high_limit'], 2)

        # high_seq = bars['high']
        # # pre_close = round(bar['pre_close'], 2)
        start_bar = bars[0]
        start_close = round(start_bar['pre_close'], 2)
        final_high_rate = 100 * (final_high - final_pre_close) / final_pre_close
        high_rate = 100 * (final_high - start_close) / start_close
        # close_rate = 100 * (final_close - start_close) / start_close
        # high_rate_seq = [100 * (x - start_close) / start_close for x in high_seq]
        # if final_high_limit == final_high or
        # if final_two_high == final_two_high_limit:
        if final_high_rate > 5:
            # if high_rate > 1:
            self.success_symbol.append(symbol)

    def syn_backtest(self):
        self.total_assert = []
        next_N_day = 1
        for i in range(0, len(self.trading_date) - next_N_day):
            try:
                date = self.trading_date[i]

                next_date = self.trading_date[i + next_N_day]
                until_trade_days = get_trade_days(
                    start_time="2018-01-01", end_time=date
                )
                self.today_data = self.day_data[self.day_data["date"] == date]
                self.code_list = np.unique(self.today_data["code"])

                for bar in self.today_data:
                    if str(bar["code"]).startswith("688") or str(bar["code"]).startswith("30"):
                        continue
                    self.pick_symbol(bar)
                count_N = 31
                history_N_data = get_bars(self.symbol_list, end_time=date, count=count_N)

                for symbol in self.symbol_list:
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == count_N:
                        self.on_day_bar(bars)

                history_Next_data = get_bars(self.res_symbol, end_time=next_date)
                for symbol in self.res_symbol:
                    bar = history_Next_data[history_Next_data["code"] == symbol][-1]
                    high = round(bar['high'], 2)
                    high_limit = round(bar['high_limit'], 2)
                    if high_limit == high:
                        self.success_symbol.append(bar['code'])

                #     if len(bars) == next_N_day:
                #         self.next_day_backtest(bars)
                if len(self.res_symbol) > 0:
                    logger.info(f"日期{date}")
                    logger.info(f"{self.success_symbol}")
                    # logger.info(f"{self.success_symbol}")
                    logger.info(f"回测标数量 {len(self.success_symbol)}")
                    # logger.info(f"回测标数量 {len(self.success_symbol)/len(self.res_symbol)}")

                self.res_symbol = []
                self.success_symbol = []
                self.hold_symbol = []
                self.fail_symbol = []
                self.symbol_list = []

            except Exception as e:
                logger.warning(e)
                continue


def daiyl_n_limit():
    # try:
    #     update_day_bar()
    # except Exception as e:
    #     print(e)
    logger.info(f"filename:{FILENAME}.py, N字板")

    today = datetime.date.today()
    end_time = str(today)
    trade_days_until_today = get_trade_days(start_time="2014-01-01", end_time=end_time)
    start_time = trade_days_until_today[-2]
    # test = DailyNLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily', solid=True)
    test = DailyNLimit(
        start_date="2021-10-01", end_date="2022-11-01", frequency="daily", solid=True
    )
    test.syn_backtest()


if __name__ == "__main__":
    daiyl_n_limit()
