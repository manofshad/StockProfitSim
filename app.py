import os

from flask import Flask, render_template, request
from stock_data.current_price import get_current_price
from strategies.uptrend import uptrend, UptrendStrategy
from strategies.buy_on_first_day import buy_on_first


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    graph = None
    strategy = None
    html_file = None
    if request.method == 'POST':
        ticker = request.form['ticker'].upper()
        strategy = request.form['strategy']
        time_period = request.form['time_period']

        if strategy == "buy_first_day":
            buy_on_first(ticker, time_period)
            html_file = f'strategies/charts/{ticker}_buy_on_first_{time_period}year.html'
        elif strategy == "uptrend":
            uptrend(ticker, time_period)
            html_file = f'strategies/charts/{ticker}_uptrend_{time_period}year.html'

            # Read the generated HTML file
        if os.path.exists(html_file):
            with open(html_file, "r") as file:
                graph = file.read()

        price = get_current_price(ticker)
        message = f"The current price of {ticker} is {price}"
    return render_template('home.html', price=message, graph = graph, strategies = strategy)
