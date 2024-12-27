from nasdaq import create_data

spy_top50 = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "GOOG", "META", "TSLA", "BRK.B",
    "UNH", "JNJ", "V", "XOM", "JPM", "PG", "MA", "HD", "CVX", "PFE", "KO",
    "PEP", "ABBV", "MRK", "TMO", "AVGO", "COST", "CSCO", "ACN", "ABT", "DHR",
    "DIS", "MCD", "NKE", "LLY", "WMT", "VZ", "ADBE", "INTC", "CMCSA", "TXN",
    "NFLX", "MDT", "PM", "HON", "UNP", "NEE", "QCOM", "LIN", "LOW", "GS"
]

for i in spy_top50:
    create_data(i, 3)