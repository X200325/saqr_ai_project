def flatten(lst):
    return [item for sublist in lst for item in sublist]

def normalize_prices(candles):
    # مثال: تطبيع الأسعار بين 0 و1
    highs = [c['high'] for c in candles]
    lows = [c['low'] for c in candles]
    max_price = max(highs)
    min_price = min(lows)
    for c in candles:
        c['high'] = (c['high'] - min_price) / (max_price - min_price)
        c['low'] = (c['low'] - min_price) / (max_price - min_price)
    return candles
