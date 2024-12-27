import pandas as pd

######################################
#     Cleans up Nasdaq CSV Files     #
#    to be accepted by backtesting   #
######################################


data = pd.read_csv('../stock_data/GOOG_2014_data.csv')

data.rename(columns={
    'Close/Last': 'Close',
    'Volume': 'Volume',
    'Open': 'Open',
    'High': 'High',
    'Low': 'Low'
}, inplace=True)

data['Close'] = data['Close'].str.replace('$', '').astype(float)
data['Open'] = data['Open'].str.replace('$', '').astype(float)
data['High'] = data['High'].str.replace('$', '').astype(float)
data['Low'] = data['Low'].str.replace('$', '').astype(float)

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

data.sort_index(inplace=True)

data.to_csv('GOOG_cleaned.csv')

data.head()
