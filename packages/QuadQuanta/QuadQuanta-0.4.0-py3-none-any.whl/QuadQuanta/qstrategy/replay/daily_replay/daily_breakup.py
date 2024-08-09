# -*-coding:utf-8-*-
# 每日突破前高，配合板块突破。买点在于情绪节点和回踩位置
# 突破40日高点, 昨日未突破, 平台调整突破
# 要看钱两个交易日的走势，反转突破

import sys
import os
import numpy as np
import datetime
import talib
from QuadQuanta.data.update_data import update_day_bar
from QuadQuanta.core.strategy import BaseStrategy

# from QuadQuanta.data.clickhouse_api import query_clickhouse, query_limit_count, query_N_clickhouse
from QuadQuanta.data.mongodb_api import insert_mongodb, save_mongodb, query_mongodb

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
        初选标，最大涨幅大于6.5，成交额大于1亿
        Parameters
        ----------
        bar

        Returns
        -------

        """
        code = bar["code"]
        high = round(bar["high"], 2)
        low = round(bar["low"], 2)
        high_limit = round(bar["high_limit"], 2)
        close = round(bar["close"], 2)
        open_ = round(bar["open"], 2)
        pre_close = round(bar["pre_close"], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        close_rate = 100 * (close - pre_close) / pre_close
        low_rate = 100 * (low - pre_close) / pre_close
        amount = bar["amount"]
        if amount > 2 * pow(10, 8) and high_rate > 8:
            if high_limit == high:
            # if high_rate - close_rate > 4.5:
                self.symbol_list.append(code)


    def on_day_bar(self, bars: np.ndarray):
        """
        Parameters
        ----------
        bars

        Returns
        -------

        """
        today_bar = bars[-1]
        code = today_bar["code"]
        pre_bar = bars[-2]
        max_60_high = max(bars[:-1]["high"])
        today_high = round(today_bar["high"], 2)
        today_close = round(today_bar["close"], 2)
        today_high_limit = round(today_bar["high_limit"], 2)
        pre_close = round(today_bar["pre_close"], 2)
        pre_high_limit = round(pre_bar["high_limit"], 2)
        pre_two_close = round(pre_bar["pre_close"], 2)
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        if today_high > max_60_high * 0.97 and pre_close < pre_high_limit:
            self.res_symbol.append(code)
            # if today_close == today_high_limit:
            #     self.success_symbol.append(code)
            # else:
            #     self.fail_symbol.append(code)

    def syn_backtest(self):
        self.total_assert = []
        for i in range(0, len(self.trading_date)):
            try:
                date = self.trading_date[i]

                self.today_data = self.day_data[self.day_data["date"] == date]
                self.code_list = np.unique(self.today_data["code"])

                for bar in self.today_data:
                    if str(bar["code"]).startswith("688") or str(bar["code"]).startswith("30"):
                        continue
                    self.pick_symbol(bar)
                breakNdays = 51
                history_N_data = get_bars(self.symbol_list, end_time=date, count=breakNdays)

                for symbol in self.symbol_list:
                    if str(symbol).startswith('30'):
                        continue
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == breakNdays:
                        self.on_day_bar(bars)


                # save_mongodb('QuadQuanta', 'daily_breakup',
                #              {'_id': date, 'symbol_list': self.res_symbol})
                logger.info(f"日期{date}")
                logger.info(f"{self.res_symbol}")
                logger.info(f"回测标数量 {len(self.res_symbol)}")

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
    start_time = trade_days_until_today[-5]
    # test = DailyNLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily', solid=True)
    test = DailyNLimit(
        start_date="2023-01-01", end_date="2023-10-23", frequency="daily", solid=True
    )
    test.syn_backtest()


if __name__ == "__main__":
    daiyl_n_limit()
