# Stock Profit Simulator
The **Stock Profit Simulator** is a web application that allows users to simulate investment strategies for various stock tickers over specified time periods. It provides insights into two strategies: "Buy on First Day" and "Uptrend," enabling users to make informed decisions. More strategies coming soon.

## Features
- Select Stock Ticker: Input the stock ticker (e.g., AAPL).
- Choose Strategy: Choose between "Buy on First Day" and "Uptrend" strategies.
- Specify Time Period: Simulate over 3 years or 10 years.
- Display Results: View strategy outcomes and charts for easy analysis.

## Installation
### Prerequisites
- Python 3.x
- Required Python packages (specified in requirements.txt):
  - Flask
  - pandas
    
### Steps
1. Clone the repository:
  ```
  git clone <repository-url>
  cd <repository-folder>
  ```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the Flask application:
```
python app.py
```
4. Open a web browser and navigate to:
```
http://127.0.0.1:5000/
```

Usage
1. Launch the application using the steps above.
2. Enter a stock ticker (e.g., AAPL).
3. Select an investment strategy and time period.
4. Submit the form to view results
