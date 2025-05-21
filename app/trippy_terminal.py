# --- IMPORTS ---
import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- PAGE SETUP ---
st.set_page_config(layout="wide")

# Load custom CSS
with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HEADER WITH TICKER ---
st.markdown("""
<div style='text-align:center; font-size:30px; color:#ffcc00; text-shadow:0 0 10px #00ffff;'>
  🌐 Trippy Markets Terminal 💫
</div>
<div style='text-align:center; font-size:20px; margin-top:-10px;'>
  <marquee scrollamount="10" direction="left" style="color:#ff69b4;">
    🧠 BTC 64320 ▲ 2.3% &nbsp;&nbsp;&nbsp; 🎸 ETH 3450 ▼ 1.1% &nbsp;&nbsp;&nbsp; 💎 TSLA 182.5 ▲ 0.7% &nbsp;&nbsp;&nbsp; 📈 SPY 520.9 ▼ 0.3%
  </marquee>
</div>
""", unsafe_allow_html=True)

# --- MUSIC VISUALIZER PLACEHOLDER ---
st.markdown("""
<div style='text-align:center; margin:20px;'>
  <img src='https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif' width='200'/>
  <p style='color:#ccc;'>Live Vibe Visualizer (connect to the jam 🌀)</p>
</div>
""", unsafe_allow_html=True)

# --- FAKE HEATMAP / TICKER DATA ---
st.subheader("Heatmap: Market Movements")
assets = ['BTC', 'ETH', 'SPY', 'QQQ', 'TSLA', 'AAPL', 'GOOG']
data = np.random.normal(0, 1, len(assets))

cols = st.columns(len(assets))
for i, col in enumerate(cols):
    change = data[i]
    color = '#00ff00' if change > 0 else '#ff0066'
    col.markdown(f"""
        <div style='text-align:center; background:{color}; padding:10px; border-radius:12px;'>
        <b>{assets[i]}</b><br>{change:+.2f}%
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<hr style="border-top: 1px solid #ccc;"/>
<div style='text-align:center; font-size:12px; color:#888;'>
  Made with 💜 in the Market Matrix.
</div>
""", unsafe_allow_html=True)
