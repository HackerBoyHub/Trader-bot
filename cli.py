import argparse
from bot.client import get_binance_client
from bot.logging_config import setup_logging
from bot.validators import validate_order
from bot.orders import place_order
logger = setup_logging()
def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--side', choices=['BUY', 'SELL'], required=True)
    parser.add_argument('--type', choices=['MARKET', 'LIMIT'], required=True)
    parser.add_argument('--quantity', type=float, required=True)
    parser.add_argument('--price', type=float)
    args = parser.parse_args()
    # 1. Validate
    valid, error = validate_order(args.type, args.price)
    if not valid:
        print(f" {error}")
        return
    # 2. Execute
    try:
        client = get_binance_client()
        logger.info(f"Sending {args.type} {args.side} for {args.symbol}")
        
        res, err = place_order(client, args.symbol, args.side, args.type, args.quantity, args.price)
        if err:
            print(f" API Error: {err}")
        else:
            print(f"Success! Order ID: {res['orderId']} | Status: {res['status']}")  
    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    main()