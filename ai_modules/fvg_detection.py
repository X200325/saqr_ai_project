def find_fair_value_gaps(candles):
    fvg_list = []
    for i in range(2, len(candles)):
        # فجوة قيمة عادلة صعودية
        if candles[i-2]['high'] < candles[i]['low']:
            fvg_list.append({'type': 'bullish', 'start': i-2, 'end': i})
        # فجوة قيمة عادلة هبوطية
        elif candles[i-2]['low'] > candles[i]['high']:
            fvg_list.append({'type': 'bearish', 'start': i-2, 'end': i})
    return fvg_list
