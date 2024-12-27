import pandas as pd
from backtesting import Backtest, Strategy
from data.read_csv import read_csv


def sma(series, n):
    # Convert to pandas Series, calculate rolling mean, then return as numpy array
    return pd.Series(series).rolling(n).mean().values


class UptrendStrategy(Strategy):
    def init(self):
        # Use self.I with a custom SMA function
        self.sma100 = self.I(sma, self.data.Close, 100)
        self.sma10 = self.I(sma, self.data.Close, 10)

    def next(self):
        close = self.data.Close[-1]
        sma100_val = self.sma100[-1]
        sma10_val = self.sma10[-1]

        if not self.position and sma10_val > sma100_val:
            self.buy()
        elif self.position and sma100_val > sma10_val:
            self.position.close()


def uptrend(ticker, time_period):
    data = read_csv(ticker, time_period)

    bt = Backtest(data, UptrendStrategy, cash=10_000, commission=0.0)
    stats = bt.run()
    print(stats)
    bt.plot(filename=f'/Users/manofshad/PycharmProjects/Trading/strategies/charts/{ticker}_uptrend_{time_period}year.html', open_browser=False)


# uptrend('NVDA')
