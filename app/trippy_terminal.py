import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import datetime
import random
import requests

# --------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Trippy Terminal",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------- CUSTOM STYLES ----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Orbitron', monospace;
        background: url('https://media.giphy.com/media/3oKIPwoeGErMmaI43C/giphy.gif');
        background-size: cover;
        color: #00ffcc;
    }

    .ticker {
        animation: wave 3s infinite;
        font-size: 24px;
        color: #ff00ff;
        padding: 10px;
    }

    @keyframes wave {
        0% { transform: translateX(0px); }
        50% { transform: translateX(10px); }
        100% { transform: translateX(0px); }
    }
    </style>
""", unsafe_allow_html=True)

# --------------- SIDEBAR ----------------
st.sidebar.header("Trippy Terminal")
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")

# --------------- LIVE TICKER ----------------
def show_ticker(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    price = todays_data['Close'].iloc[-1] if not todays_data.empty else 0
    st.markdown(f'<div class="ticker">${ticker.upper()} - ${price:.2f}</div>', unsafe_allow_html=True)

# --------------- CHART PANEL ----------------
def plot_chart(ticker):
    data = yf.download(ticker, period="1mo", interval="1h")
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Market Data'))

    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='lime'),
        xaxis_rangeslider_visible=False,
        title=f"{ticker.upper()} - Last Month"
    )
    st.plotly_chart(fig, use_container_width=True)

# --------------- FAKE SENTIMENT ANALYZER ----------------
def fake_sentiment():
    sentiment = random.choice(["bullish", "bearish", "trippy"])
    colors = {"bullish": "green", "bearish": "red", "trippy": "purple"}
    st.markdown(f'<h3 style="color:{colors[sentiment]}">Market Sentiment: {sentiment}</h3>', unsafe_allow_html=True)

# --------------- MEME OR CRYSTAL BALL ----------------
def meme_or_fortune():
    if random.random() > 0.5:
        st.image("https://i.imgur.com/Bz3fQTI.jpeg", caption="Meme of the Day")
    else:
        st.markdown(f'<h4 style="color:#cc00ff">🔮 Your fortune: {random.choice(["Buy the dip", "Sell the news", "HODL like a wizard", "Rebalance your karma"])}</h4>', unsafe_allow_html=True)

# --------------- MUSHROOM CLOCK ----------------
def mushroom_clock():
    ny_time = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
    st.markdown(f'<h4 style="color:#ffcc00">🍄 Market Time (NY): {ny_time.strftime("%H:%M:%S")}</h4>', unsafe_allow_html=True)

# --------------- MAIN DISPLAY ----------------
st.title("🌈 Trippy Terminal")
show_ticker(ticker)
plot_chart(ticker)
fake_sentiment()
mushroom_clock()
meme_or_fortune()

st.markdown("---")
st.markdown("**Trip Mode, Audio Visuals & Mood Rings Coming Soon...** 🎧💫")
