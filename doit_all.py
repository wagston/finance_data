import pandas as pd
import requests
import json
from pandas_datareader import data
import yahoo_finance as yf
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
 
tickers = ['CSNA3.SA', 'PETR4.SA', 'LAME4.SA', 'GOLL4.SA', 'AZUL4.SA', 'BBAS3.SA', 'SLCE3.SA', 'BRKM5.SA', 'SPXI11.SA']

def candlestick_us(quote,days):
    r = requests.get(f'https://financialmodelingprep.com/api/v3/historical-price-full/{quote}?timeseries={days}')
    r = r.json()

    stockdata = r['historical']
    stockdata_df = pd.DataFrame(stockdata)

    fig = go.Figure(data=[go.Candlestick(x=stockdata_df['date'],
        open=stockdata_df['open'],
        high=stockdata_df['high'],
        low=stockdata_df['low'],
        close=stockdata_df['close'])])
    fig.update_layout(
        title= {
         'text': quote,
         'y':0.9,
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top'},
        font=dict(
        family="Courier New, monospace",
        size=20,
        color="#7f7f7f"))
    fig.show()

def candlestick_br(quote, start_date, end_date):
    stockdata_df = data.get_data_yahoo(quote, start_date, end_date)
    fig = go.Figure(data=[go.Candlestick(x=stockdata_df.index,
        open=stockdata_df['Open'],
        high=stockdata_df['High'],
        low=stockdata_df['Low'],
        close=stockdata_df['Close'])])
    fig.update_layout(
    title= {
     'text': quote,
     'y':0.9,
     'x':0.5,
     'xanchor': 'center',
     'yanchor': 'top'},
    font=dict(
    family="Courier New, monospace",
    size=20,
    color="#7f7f7f"
    ))
    fig.show()
    

start_date = '2020-01-01'
end_date = date.today()
for quote in tickers:
    candlestick_br(quote, start_date, end_date)        
