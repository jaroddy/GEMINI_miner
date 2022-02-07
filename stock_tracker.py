# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:56:22 2021

@author: jarod
"""


#Stock Data Compiler

#Gathers all available stock data and identifies trends such as what behavior leads to increases
#Overall goal is to match a specific behavior to an increase/decrease in stock price

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=MP61AFF9D7IU67QX'
r = requests.get(url)
data = r.json()

print(data)