from binance.exceptions import BinanceAPIException

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }#specify here parameter of waht ur buying
        
        if order_type == 'LIMIT':
            params['price'] = price #price
            params['timeInForce'] = 'GTC' #gtc

        # This sends the signed request to Binance
        response = client.futures_create_order(**params)
        return response, None
    except BinanceAPIException as e:#excpetion if there is error hadnling
        return None, e.message