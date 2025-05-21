import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Market Correlation Heatmap")

files = [f for f in os.listdir("data") if f.endswith(".csv")]
dfs = []
symbols = []

for file in files:
    df = pd.read_csv(f"data/{file}", index_col="Date", parse_dates=True)
    if "Close" in df.columns:
        dfs.append(df["Close"].rename(file.replace(".csv", "")))

if dfs:
    combined = pd.concat(dfs, axis=1).dropna()
    corr = combined.pct_change().corr()

    st.subheader("Correlation Heatmap of Daily Returns")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.warning("No valid price data found.")
