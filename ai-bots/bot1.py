import yfinance as yf
import pandas as pd
import numpy as np

# Fetch historical stock data
stock = yf.download("AAPL", start="2020-01-01", end="2024-01-01")