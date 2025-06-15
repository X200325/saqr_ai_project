def detect_order_blocks(candles):
    # بسيط: نبحث عن شمعة كبيرة الحجم، ثم شمعة عكسها بقوة
    order_blocks = []
    for i in range(1, len(candles)-1):
        prev_candle = candles[i-1]
        candle = candles[i]
        next_candle = candles[i+1]

        if candle['close'] < candle['open'] and prev_candle['close'] > prev_candle['open']:
            # هبوط بعد صعود
            order_blocks.append({'index': i, 'type': 'bearish'})
        elif candle['close'] > candle['open'] and prev_candle['close'] < prev_candle['open']:
            order_blocks.append({'index': i, 'type': 'bullish'})
    return order_blocks

def detect_fvg(candles):
    fvgs = []
    for i in range(2, len(candles)):
        if candles[i-2]['high'] < candles[i]['low']:
            fvgs.append({'start': i-2, 'end': i, 'type': 'bullish'})
        elif candles[i-2]['low'] > candles[i]['high']:
            fvgs.append({'start': i-2, 'end': i, 'type': 'bearish'})
    return fvgs

# يمكن إضافة المزيد من مفاهيم ICT وSMC هنا
