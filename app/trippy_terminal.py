# --- IMPORTS ---
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import time
from datetime import datetime

# --- PAGE SETUP ---
st.set_page_config(layout="wide")

# Load custom CSS
with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HEADER WITH LIVE TICKER MARQUEE ---
st.markdown("""
<div style='text-align:center; font-size:30px; color:#ffcc00; text-shadow:0 0 10px #00ffff;'>
  🌐 Trippy Markets Terminal 💫
</div>
""", unsafe_allow_html=True)

# --- LIVE MARKET DATA FUNCTION ---
@st.cache_data(ttl=300)
def get_live_data(tickers):
    data = {}
    for ticker in tickers:
        info = yf.Ticker(ticker).history(period="1d", interval="1m")
        if not info.empty:
            last_close = info["Close"].iloc[-1]
            prev_close = info["Close"].iloc[-2]
            pct_change = ((last_close - prev_close) / prev_close) * 100
            data[ticker] = round(pct_change, 2)
        else:
            data[ticker] = 0.0
    return data

# --- LIVE DATA ---
tickers = ['BTC-USD', 'ETH-USD', 'SPY', 'QQQ', 'TSLA', 'AAPL', 'GOOG']
live_data = get_live_data(tickers)

# --- LIVE MARQUEE ---
st.markdown(f"""
<marquee scrollamount="10" direction="left" style="color:#39ff14; font-size:18px; font-family:monospace; text-shadow: 0 0 10px #00ffcc;">
🧠 Live: {' • '.join([f'{t} {live_data[t]}%' for t in tickers])}
</marquee>
""", unsafe_allow_html=True)

# --- MUSIC VISUALIZER PLACEHOLDER ---
st.markdown("""
<div style='text-align:center; margin:20px;'>
  <img src='https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif' width='200'/>
  <p style='color:#ccc;'>Live Vibe Visualizer (connect to the jam 🌀)</p>
</div>
""", unsafe_allow_html=True)

# --- HEATMAP ---
st.subheader("Heatmap: Market Movements")
cols = st.columns(len(tickers))
for i, col in enumerate(cols):
    ticker = tickers[i]
    change = live_data[ticker]
    color = '#00ff00' if change > 0 else '#ff0066'
    col.markdown(f"""
        <div style='text-align:center; background:{color}; padding:10px; border-radius:12px;'>
        <b>{ticker}</b><br>{change:+.2f}%
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<hr style="border-top: 1px solid #ccc;"/>
<div style='text-align:center; font-size:12px; color:#888;'>
  Made with 💜 in the Market Matrix.
</div>
""", unsafe_allow_html=True)
