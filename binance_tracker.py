import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"BTC Price: ${btc_price['price']}")

