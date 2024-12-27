import requests

def get_current_price(ticker):
    symbol = ticker.upper()
    api_url = f'https://api.api-ninjas.com/v1/stockprice?ticker={symbol}'
    response = requests.get(api_url, headers={'X-Api-Key': '+JCWFiiWBy/xMQxIL9lXfA==jTuHPsykKDTL1ZUZ'})

    if response.status_code == 200:
        data = response.json()
        return data['price']
    else:
        print(f"Error: {response.status_code} {response.text}")
