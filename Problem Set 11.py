import streamlit as st
import pandas as pd
import yfinance as yf

"""Stock_Ticker= input("What is the Ticker of the stock you would like to get data for?").upper()
Stock_Ticker2= yf.Ticker(Stock_Ticker)
hist = Stock_Ticker2.history(period="max")

print(Stock_Ticker2.info)
print(hist)"""

ticker = yf.Ticker('TSLA')

tsla_df = ticker.history(period="max")

tsla_df['Close'].plot(title="TSLA's stock price")

