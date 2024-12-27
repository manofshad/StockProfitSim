import pandas as pd
from backtesting import Backtest, Strategy

from data.read_csv import read_csv


class BuyOnFirstDay(Strategy):
    def init(self):
        self.bought_once = False

    def next(self):
        if not self.bought_once:
            self.buy()
            self.bought_once = True


def buy_on_first(ticker, time_period):
    data = read_csv(ticker, time_period)

    bt = Backtest(data, BuyOnFirstDay, cash=10_000, commission=0.0)
    stats = bt.run()
    print(stats)
    bt.plot(filename=f'/Users/manofshad/PycharmProjects/Trading/strategies/charts/{ticker}_buy_on_first_{time_period}year.html', open_browser=False)
