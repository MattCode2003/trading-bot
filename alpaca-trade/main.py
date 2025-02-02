#================================== Imports ===================================


import json
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime


#=============================== Config Settings ==============================


def config_settings():
	global trade
	global symbol
	global API_KEY
	global SECRET_KEY
	global ENDPOINT

	with open("config.json", "r") as f:
		config = json.load(f)

	trade = bool(config["trade"])
	symbol = config["symbol"]
	API_KEY = config["api_key"]
	SECRET_KEY = config["secret_key"]
	ENDPOINT = config["endpoint"]


def main():
	config_settings()

	if trade:
		trading_client = TradingClient(API_KEY, SECRET_KEY)
	else:
		pass

	

if __name__ == "__main__":
	main()