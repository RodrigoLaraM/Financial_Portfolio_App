import pandas as pd
import yfinance as yf
import Interface
import Portfolio

p_file = Portfolio.extractor()
action = Interface.user_interface()

Ticker = input("Input Asset's Ticker:")
USD = "-USD"
BTC = yf.download(Ticker + USD)
print(BTC)
