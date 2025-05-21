import streamlit as st
import pandas as pd
import os
import sys

# 🔧 Add this block to fix the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.indicators import add_moving_averages, add_rsi
from scripts.news import fetch_market_news

st.set_page_config(layout="wide")
st.title("World Markets Performance Dashboard")

with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


refresh = st.button("Refresh Data")

available_files = [f for f in os.listdir("data") if f.endswith(".csv")]
if not available_files:
    st.warning("No data files found. Please run the fetch script first.")
else:
    selected = st.selectbox("Choose a market", available_files)
    df = pd.read_csv(f"data/{selected}", index_col="Date", parse_dates=True)

    # Technical indicators
    df = add_moving_averages(df)
    df = add_rsi(df)

    st.subheader(f"Price and Moving Averages for {selected}")
    st.line_chart(df[["Close", "SMA_20", "SMA_50", "SMA_200"]].dropna())

    st.subheader("RSI Indicator")
    st.line_chart(df["RSI"].dropna())

    latest_rsi = df["RSI"].iloc[-1]
    st.subheader("Alerts")
    if latest_rsi > 70:
        st.error(f"RSI is {latest_rsi:.2f}: Overbought!")
    elif latest_rsi < 30:
        st.success(f"RSI is {latest_rsi:.2f}: Oversold!")
    else:
        st.info(f"RSI is {latest_rsi:.2f}: Neutral")

    # Global market news
    st.subheader("Global Market News")
    news_items = fetch_market_news()
    for item in news_items:
        st.markdown(f"- [{item['title']}]({item['url']})")
