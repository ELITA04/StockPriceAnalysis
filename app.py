import datetime
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import pandas_datareader.data as web

def plot_high_low(option, start_date, end_date):
    """
    Plotting the high and low prices

    Parameters:
        option (str): String containing the name of the company
        start_date : Date from which you want 
        end_date : Date uptil which you want 

    """
    d = {'Google' : 'GOOGL',  'Facebook' : 'FB', 'Tesla' : 'TSLA', 'Ford' : 'F', 'GM' : 'GM'}
    df = pd.DataFrame(web.DataReader(d[option], 'yahoo', start_date, end_date))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index.get_level_values('Date'), y = df['High'], mode = 'lines + markers', name = 'High Price'))
    fig.add_trace(go.Scatter(x=df.index.get_level_values('Date'), y = df['Low'], mode = 'lines + markers', name = 'Low Price'))
    fig.update_layout(title = f"{option}'s Daily Stock Prices ", yaxis_title = 'Stock Prices', xaxis_title = 'Date')
    st.plotly_chart(fig)

def main():
    st.title('📈 Financial Analysis')
    start_date = st.sidebar.date_input('Start date', datetime.date(2021, 1, 1))
    end_date = st.sidebar.date_input('End date', datetime.datetime.now())
    option = st.selectbox(
        'Company Name',
        ('Google', 'Facebook', 'Tesla', 'Ford', 'GM')
    )

    plot_high_low(option, start_date, end_date)
    

if __name__ == '__main__':
    main()