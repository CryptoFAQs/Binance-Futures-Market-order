
# pip install python-binance

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

symbol = "DOGEUSDT"
contract_size = 100
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)

def market_buy(symbol, contract_size):
    try:
        market_buy = client.futures_create_order(
        symbol = symbol,
        side = Client.SIDE_BUY,
        type = Client.ORDER_TYPE_MARKET,
        quantity = contract_size)

        print(str(market_buy))

    except BinanceAPIException as e:
        print(e)
    except BinanceOrderException as e:
        print(e)

def market_sell(symbol, contract_size):
    try:
        market_sell = client.futures_create_order(
        symbol = symbol,
        side = Client.SIDE_SELL,
        type = Client.ORDER_TYPE_MARKET,
        quantity = contract_size)

        print(str(market_sell))

    except BinanceAPIException as e:
        print(e)
    except BinanceOrderException as e:
        print(e)


market_buy(symbol, contract_size)

