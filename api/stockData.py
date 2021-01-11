# stockTable.py
# Generate a table of stocks and their price info

import dash
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

def generate_table(df, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ), 
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[row][col]) for col in df.columns
            ]) for row in range(min(len(df), max_rows))
        ])
    ])

def render():
    """Render HTML table with stock prices."""
    stocks = pd.DataFrame(
        data = {
            'Name': ['TSLA', 'SQ', 'AAPL'], 
            'Buy Price': [627.33, 203.17, 127.15],
            'Current Price': [804.22, 237.89, 130.24]
        }
    )
    return html.Div([
        html.H3('Current Positions'),
        generate_table(stocks)
    ])
    
    
