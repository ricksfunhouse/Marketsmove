import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(tickers, period="1y", interval="1d"):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, period=period, interval=interval)
        data[ticker] = df
    return data

if __name__ == "__main__":
    tickers = ["^GSPC", "^FTSE", "^N225", "AAPL", "GOOG"]
    os.makedirs("data", exist_ok=True)
    stock_data = fetch_stock_data(tickers)
    for symbol, df in stock_data.items():
        df.to_csv(f"data/{symbol}.csv")
