import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import matplotlib.pyplot as plt


td=datetime.timedelta(days=365)

option=st.sidebar.selectbox("which index/stock?",('Nifty','Bank Nifty','Stock'))

st.header(option)

if option == 'Nifty':
    st.subheader("Nifty chart")
    start_date=st.date_input("start date",(datetime.date.today()-td))
    end_date=st.date_input("end date",datetime.date.today())
    ticker_nifty = pd.DataFrame(yf.download("^NSEI", start=start_date, end=end_date))
    fig = plt.figure() 
    plt.plot(ticker_nifty[['Close']]) 
    st.pyplot(fig)
    st.dataframe (ticker_nifty)


if option == 'Bank Nifty':
    st.subheader("Nifty chart")
    start_date=st.date_input("start date",(datetime.date.today()-td))
    end_date=st.date_input("end date",datetime.date.today())
    ticker_banknifty = pd.DataFrame(yf.download("^NSEBANK", start=start_date, end=end_date))
    fig = plt.figure() 
    plt.plot(ticker_banknifty[['Close']]) 
    st.pyplot(fig)
    st.dataframe (ticker_banknifty)

if option == 'Stock':
    stock_name=st.sidebar.text_input("Stock name",value='reliance',max_chars = 100 )
    st.subheader("%s"%(stock_name))
    start_date=st.date_input("start date",(datetime.date.today()-td))
    end_date=st.date_input("end date",datetime.date.today())
    ticker_stock = pd.DataFrame(yf.download("%s.NS"%(stock_name), start=start_date, end=end_date ))
    fig = plt.figure() 
    plt.plot(ticker_stock[['Close']]) 
    st.pyplot(fig)
    st.dataframe (ticker_stock)


