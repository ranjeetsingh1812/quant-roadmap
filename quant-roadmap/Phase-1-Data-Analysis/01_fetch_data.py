import yfinance as yf
import pandas as pd

def fetch_data(tickers, start="2018-01-01", end="2023-12-31"):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    data.to_csv("raw_prices.csv")
    return data

if __name__ == "__main__":
    tickers = ["SPY", "AAPL", "TLT", "GLD"]
    data = fetch_data(tickers)
    print(data.head())