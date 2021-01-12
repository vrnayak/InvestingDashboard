# stockTable.py
# Generate a table of stocks and their price info

import dash
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

# Import API
import api.stocks as st

def generate_table(df, max_rows=10):
  """Generates HTML table with data in Pandas dataframe."""
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

  positions = ['AAPL', 'AYRO', 'CCL', 'CORR', 'OKTA', 'OXY', 'PFE', 'PYPL', 'SNOW', 'SQ', 'TELL']
  buyPrices = [127.85, 9.20, 17.62, 9.23, 233.32, 23.50, 41.83, 214.98, 358.23, 203.19, 1.45]

  stocks = pd.DataFrame(
      data = {
          'Name': positions, 
          'Buy Price': buyPrices,
          'Current Price': [st.latest_price(symbol) for symbol in positions]
      }
  )
  return html.Div([
      html.H3('Current Positions', id='current-positions'),
      generate_table(stocks)
  ])
