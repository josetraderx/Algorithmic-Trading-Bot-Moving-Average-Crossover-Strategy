# 1. Data Acquisition
# The first step in building an algorithmic trading bot is acquiring the necessary data,
# which includes historical or live price data, volume, and other market metrics.
# This data is essential to develop and test trading strategies, ensuring that they perform well
# before live deployment.
# To fetch this data, several APIs are available, such as:
# • Yahoo Finance via the yfinance library,
# • Alpha Vantage for both equity and forex data,
# • Interactive Brokers for trading execution and live data.
# For this example, we will use the yfinance library to acquire historical data for a specific stock.


import pandas as pd
import yfinance as yf


def load_data():
    '''
    Download historical daily stock data for Apple (AAPL) from Yahoo Finance.

    '''
    ticker = 'AAPL' # Apple Stock
    start_date = '2021-01-01'
    end_date = '2022-01-01'

    data = yf.download(ticker, start=start_date, end=end_date)
    print(data.head())

    return data
