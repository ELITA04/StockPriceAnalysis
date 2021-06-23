import datetime
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import pandas_datareader.data as web



def main():
    st.title('📈 Financial Analysis')
    start_date = datetime.datetime(2021, 1, 1)
    end_date = datetime.datetime.now()


    google = pd.DataFrame(web.DataReader('GOOGL', 'yahoo', start_date, end_date))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=google.index.get_level_values('Date'), y = google['High'], mode = 'lines + markers', name = 'High Price'))
    fig.add_trace(go.Scatter(x=google.index.get_level_values('Date'), y = google['Low'], mode = 'lines + markers', name = 'Low Price'))
    fig.update_layout(title = 'Google Daily Stock Prices', yaxis_title = 'Stock Prices', xaxis_title = 'Date')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()