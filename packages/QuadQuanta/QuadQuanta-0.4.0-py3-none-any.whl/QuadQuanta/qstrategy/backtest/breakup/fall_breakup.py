# 横盘突破失败冲高回落，再次突破。注意，要求突破之前在高位

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
        pre_close = round(bar["pre_close"], 2)
        high_rate = 100 * (high - pre_close) / pre_close
        close_rate = 100 * (close - pre_close) / pre_close
        low_rate = 100 * (low - pre_close) / pre_close
        amount = bar["amount"]

        if high_rate > 5  and amount > pow(10, 8) and high_rate - close_rate > 3:
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
        pre_close = round(today_bar["pre_close"], 2)
        pre_two_close = round(pre_bar["pre_close"], 2)
        pre_close_rate = 100 * (pre_close - pre_two_close) / pre_two_close
        if today_high > max_60_high and pre_close_rate < 9.9:
            self.res_symbol.append(code)

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
                breakNdays = 61
                history_N_data = get_bars(self.symbol_list, end_time=date, count=breakNdays)

                for symbol in self.symbol_list:
                    if str(symbol).startswith('30'):
                        continue
                    bars = history_N_data[history_N_data["code"] == symbol]
                    if len(bars) == breakNdays:
                        self.on_day_bar(bars)

                # self.history_N_data = get_bars(self.res_symbol, end_time=next_day, count=1)
                # for symbol in np.unique(self.res_symbol):
                #     if str(symbol).startswith('688') or str(symbol).startswith('30'):
                #         continue
                #     bars = self.history_N_data[self.history_N_data['code'] == symbol]
                #     if len(bars) == 1:
                #         bar = bars[-1]
                #         high = round(bar['high'], 2)
                #         pre_close = round(bar['pre_close'], 2)
                #         high_limit = round(bar['high_limit'], 2)
                #         high_rate = 100 * (high - pre_close) / pre_close
                #         if high_rate > 1:
                #             self.success_symbol.append(symbol)
                #             # logger.info(f"N字板连扳:{symbol}")

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
    start_time = trade_days_until_today[-10]
    # test = DailyNLimit(start_date=start_time,
    #                    end_date=end_time,
    #                    frequency='daily', solid=True)
    test = DailyNLimit(
        start_date="2023-01-11", end_date="2023-12-31", frequency="daily", solid=True
    )
    test.syn_backtest()


if __name__ == "__main__":
    daiyl_n_limit()
