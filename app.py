import datetime
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import pandas_datareader.data as web

def plot_high_low(options, start_date, end_date):
    """
    Plotting the high and low prices

    Parameters:
        option (list): List containing the names of the company
        start_date : Date from which you want 
        end_date : Date uptil which you want 

    """
    d = {'Google' : 'GOOGL',  'Facebook' : 'FB', 'Tesla' : 'TSLA', 'Ford' : 'F', 'GM' : 'GM'}
    fig = go.Figure()
    for opt in options:
        df = pd.DataFrame(web.DataReader(d[opt], 'yahoo', start_date, end_date)) 
        fig.add_trace(go.Scatter(x=df.index.get_level_values('Date'), y = df['High'], mode = 'lines', name = f'{opt}'))
    fig.update_layout(title = f"Daily Stock Highest Prices ", yaxis_title = 'Stock Prices', xaxis_title = 'Date')
    st.plotly_chart(fig)

def plot_volume_traded(options, start_date, end_date):
    """
    Plotting the volume traded daily for the given timespan

    Parameters:
        option (list): List containing the name's of the company
        start_date : Date from which you want 
        end_date : Date uptil which you want 

    """
    d = {'Google' : 'GOOGL',  'Facebook' : 'FB', 'Tesla' : 'TSLA', 'Ford' : 'F', 'GM' : 'GM'}
    fig = go.Figure()

    for opt in options:
        df = pd.DataFrame(web.DataReader(d[opt], 'yahoo', start_date, end_date))
        fig.add_trace(go.Scatter(x=df.index.get_level_values('Date'), y = df['Volume'], mode = 'lines', name = f'{opt}'))
    fig.update_layout(title = f"Volume Traded", yaxis_title = 'Volume', xaxis_title = 'Date')
    st.plotly_chart(fig)

def plot_cumulative_return(options, start_date, end_date):
    """
    Plotting the cumulative return for the given span

    Parameters:
        option (list): List containing the name's of the company
        start_date : Date from which you want 
        end_date : Date uptil which you want 
    """
    d = {'Google' : 'GOOGL',  'Facebook' : 'FB', 'Tesla' : 'TSLA', 'Ford' : 'F', 'GM' : 'GM'}
    fig = go.Figure()
    for opt in options:
        df = pd.DataFrame(web.DataReader(d[opt], 'yahoo', start_date, end_date)) 
        df['returns'] = (df['Close']/df['Close'].shift(1)) - 1
        df['Cumulative Return'] = (1 + df['returns']).cumprod()
        fig.add_trace(go.Scatter(x=df.index.get_level_values('Date'), y = df['Cumulative Return'], mode = 'lines', name = f'{opt}'))
    fig.update_layout(title = 'Cumulative Return ', yaxis_title = 'Stock Prices', xaxis_title = 'Date')
    st.plotly_chart(fig)


def main():
    st.title('📈 Financial Analysis')
    start_date = st.sidebar.date_input('Start date', datetime.date(2021, 1, 1))
    end_date = st.sidebar.date_input('End date', datetime.datetime.now())
    option = st.multiselect(
        'Company Name',
        ['Google', 'Facebook', 'Tesla', 'Ford', 'GM']
    )

    if option is not None:
        plot_high_low(option, start_date, end_date)

        plot_volume_traded(option, start_date, end_date)

        plot_cumulative_return(option, start_date, end_date)
    

if __name__ == '__main__':
    main()