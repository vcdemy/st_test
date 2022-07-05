import streamlit as st
import yfinance as yf
import pandas as pd
pd.options.plotting.backend = "plotly"


stock = st.sidebar.text_input("請輸入股票代號")

try:
    df = yf.download(stock)

    st.write(f"# {stock}")
    st.write(df.tail(50))

    st.plotly_chart(df.Close.tail(50).plot(title=f"{stock}"))
except:
    st.write("請輸入股票代號！")
