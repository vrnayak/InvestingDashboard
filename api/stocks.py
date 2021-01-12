# stocks.py
# An API for querying stock prices using IEX Cloud

import os
import requests
import pandas as pd
from urllib.parse import quote
from dotenv import load_dotenv

# When testing, set this to False
LIVE_MODE = False
load_dotenv()

######### HELPER FUNCTIONS #########

def api_token():
  """Returns env variable corresponding to correct IEX Cloud API token."""
  if LIVE_MODE: return os.getenv('LIVE_API_TOKEN')
  else: return os.getenv('TEST_API_TOKEN')


def base_url():
  """Returns the base URL for accessing IEX Cloud API."""
  if LIVE_MODE: return 'https://cloud.iexapis.com/'
  else: return 'https://sandbox.iexapis.com/'


def make_api_request(endpoint, params=dict(), version='stable/'):
  """Makes API request & returns dictionary with response body."""
  
  # Step 1: Construct base url, version, endpoint, & token
  path = base_url() + version + endpoint

  # Step 2: Add API token to params
  params['token'] = api_token()

  # Step 3: Make API call
  response = requests.get(path, params)
  return response

######### END OF HELPER FUNCTIONS #########

def latest_price(symbol):
  """
  Gets latest price of stock with given symbol. The free plan
  uses latest data from Investors Exchange, not 15-min delayed NASDAQ
  data from NASDAQ.

  API Usage: 1 message / call
  """

  response = make_api_request(
    endpoint='stock/{}/quote/latestPrice'.format(symbol)
  )
  return float(response.text)




if __name__ == '__main__':

  print(latest_price('AAPL'))
  print(latest_price('TSLA'))