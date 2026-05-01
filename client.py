import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    # Force testnet=True and set the URL explicitly
    client = Client(api_key, api_secret, testnet=True)
    client.FUTURES_URL = '[https://testnet.binancefuture.com/fapi](https://testnet.binancefuture.com/fapi)'
    
    return client