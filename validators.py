def validate_order(order_type, price):
    if order_type == 'LIMIT' and (not price or price <= 0):
        return False, "Limit orders require a price > 0" #making sure if limit eached mean 60,000 if mroe it fail reject or
    return True, None #price not negative