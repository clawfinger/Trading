import json
from binance.client import Client
from binance.enums import *
import dateparser

api = json.load(open(r"assets/data.json"))
client = Client(api["key"], api["secret"])

pair = 'ICXETH'
k_interval = KLINE_INTERVAL_15MINUTE

"""
get_klines answer
[
    [
        1499040000000,      # Open time
        "0.01634790",       # Open
        "0.80000000",       # High
        "0.01575800",       # Low
        "0.01577100",       # Close
        "148976.11427815",  # Volume
        1499644799999,      # Close time
        "2434.19055334",    # Quote asset volume
        308,                # Number of trades
        "1756.87402397",    # Taker buy base asset volume
        "28.46694368",      # Taker buy quote asset volume
        "17928899.62484339" # Can be ignored
    ]
]
"""

k_limit = 7

candles = client.get_klines(symbol=pair,
interval=k_interval, limit=k_limit)

"""
EMA = Price(t) * k + EMA(y) * (1 – k)
t = today, y = yesterday, N = number of days in EMA, k = 2/(N+1)
"""
EMA_k = 2 / (k_limit + 1)
EMA7 = 0

SMA7 = 0
for candle in candles:
    SMA7 += float(candle[4])

SMA7 /= len(candles)

print(SMA7)

k_limit = 25

candles = client.get_klines(symbol=pair,
interval=k_interval, limit=k_limit)


SMA25 = 0
for candle in candles:
    SMA25 += float(candle[4])
    print(candle[0])

SMA25 /= len(candles)

print(SMA25)
