def detect_breaker_blocks(candles):
    breaker_blocks = []
    for i in range(1, len(candles)-1):
        if candles[i]['high'] > candles[i-1]['high'] and candles[i]['low'] > candles[i-1]['low']:
            # مثال بسيط: شمعة تخلق قمة جديدة
            breaker_blocks.append({'index': i, 'type': 'bullish'})
        elif candles[i]['low'] < candles[i-1]['low'] and candles[i]['high'] < candles[i-1]['high']:
            breaker_blocks.append({'index': i, 'type': 'bearish'})
    return breaker_blocks
