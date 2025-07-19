import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")
st.title("📈 Stock Market Live Tracker")

ticker_input = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT, RELIANCE.NS)", "AAPL")
ticker = yf.Ticker(ticker_input.upper())
data = ticker.history(period="1d", interval="1m")

st.write(f"### Live data for: {ticker_input.upper()}")
st.line_chart(data["Close"])

fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])
fig.update_layout(title="Candlestick Chart", xaxis_title="Time", yaxis_title="Price")
st.plotly_chart(fig, use_container_width=True)