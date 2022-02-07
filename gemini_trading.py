# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:32:16 2021

@author: jarod
"""


#What this app needs to do

#Observe the current trend within the last 5 mins (up or down)

#Observe the daily high/low, 5 min high/low, max high/low

#



import requests, json

#Time sensitive price data
base_url = "https://api.gemini.com/v2"
response = requests.get(base_url + "/candles/shibusd/1m") #Last set of chars indicates time between datapoints
btc_candle_data = response.json()

print(btc_candle_data)

#Current order book
base_url = "https://api.gemini.com/v1"
response = requests.get(base_url + "/book/btcusd")
btc_book = response.json()

print(btc_book)