def analyze_price_action(candles):
    signals = []
    for i in range(1, len(candles)):
        if candles[i]['close'] > candles[i-1]['high']:
            signals.append({'index': i, 'signal': 'Bullish breakout'})
        elif candles[i]['close'] < candles[i-1]['low']:
            signals.append({'index': i, 'signal': 'Bearish breakout'})
    return signals
