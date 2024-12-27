import os
import pandas as pd
import requests

def get_info():
    ticker = input("Enter ticker symbol: ")

    while True:
        try:
            time_period = int(input("How many years before? (1 - 10 years): "))
            if 1 <= time_period <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return ticker, time_period

# ticker, time_period = get_info()

def create_data(ticker, time_period):
    year = 2024 - time_period

    url = f"https://api.nasdaq.com/api/quote/{ticker}/historical?assetclass=stocks&fromdate={year}-12-08&limit=9999&todate=2024-12-08"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        rows = data['data']['tradesTable']['rows']
        headers = ["Date", "Close", "Volume", "Open", "High", "Low"]

        df = pd.DataFrame(rows)

        df.rename(columns={
            'close': 'Close',
            'volume': 'Volume',
            'open': 'Open',
            'high': 'High',
            'low': 'Low',
            'date': 'Date'
        }, inplace=True)

        for col in ['Close', 'Open', 'High', 'Low']:
            df[col] = df[col].str.replace('$', '').str.replace(',', '').astype(float)

        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        df.sort_index(inplace=True)

        folder_name = ticker.upper()
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        cleaned_file_name = os.path.join(folder_name, f'{ticker.upper()}_{time_period}year.csv')
        df.to_csv(cleaned_file_name)
        print(f"Cleaned CSV file created successfully at {cleaned_file_name}!")

    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

