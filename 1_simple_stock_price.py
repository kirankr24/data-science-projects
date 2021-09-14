
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Apple INC!

""")

tickerSym = 'APPL'

tickerdata = yf.Ticker('tickerSym')

tickerdf = tickerdata.history(period='1d',start = '2021-01-01', end = '2021-09-11')

st.write(""""
#closing price
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)



#xcode-select --install
#pip install watchdog