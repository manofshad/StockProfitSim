import pandas as pd

def read_csv(ticker, time_period):
    data = pd.read_csv(f'/Users/manofshad/PycharmProjects/Trading/stock_data/{ticker}/{ticker}_{time_period}year.csv', index_col='Date',parse_dates=True)
    return data.sort_index()