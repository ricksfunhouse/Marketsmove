import pandas as pd

def add_moving_averages(df, windows=[20, 50, 200]):
    for window in windows:
        df[f"SMA_{window}"] = df["Close"].rolling(window=window).mean()
    return df

def add_rsi(df, period=14):
    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df
