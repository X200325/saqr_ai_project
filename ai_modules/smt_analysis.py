def analyze_smt(symbol1_candles, symbol2_candles):
    # مقارنة حركات السعر بين رمزين لملاحظة الاختلافات (مثلاً EURUSD وGBPUSD)
    divergences = []
    for i in range(len(symbol1_candles)):
        if symbol1_candles[i]['close'] > symbol1_candles[i-1]['close'] and symbol2_candles[i]['close'] < symbol2_candles[i-1]['close']:
            divergences.append({'index': i, 'type': 'bearish divergence'})
        elif symbol1_candles[i]['close'] < symbol1_candles[i-1]['close'] and symbol2_candles[i]['close'] > symbol2_candles[i-1]['close']:
            divergences.append({'index': i, 'type': 'bullish divergence'})
    return divergences
