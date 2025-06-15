import MetaTrader5 as mt5

# دالة لحساب منتصف الذيل لأي شمعة
def get_half_wick(candle):
    high = candle['high']
    low = candle['low']
    open_ = candle['open']
    close = candle['close']
    body_top = max(open_, close)
    body_bottom = min(open_, close)
    upper_wick = high - body_top
    lower_wick = body_bottom - low
    total_wick = upper_wick + lower_wick
    return low + total_wick / 2

# دالة لتحميل شموع فريم معين
def get_candles(symbol, timeframe, count=1):
    candles = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
    return candles

# دالة فحص وجود FVG بعد الكسر
def detect_fvg(candles):
    for i in range(2, len(candles)):
        prev = candles[i - 1]
        curr = candles[i]
        if curr['low'] > prev['high']:  # فجوة صعودية
            return True
        if curr['high'] < prev['low']:  # فجوة هبوطية
            return True
    return False

# دالة تحديد التحيز من الفريمات العليا
def determine_bias():
    symbol = "EURUSD"
    timeframes = [
        (mt5.TIMEFRAME_MN1, 12),
        (mt5.TIMEFRAME_MN1, 6),
        (mt5.TIMEFRAME_MN1, 3),
        (mt5.TIMEFRAME_MN1, 1),
        (mt5.TIMEFRAME_W1, 1),
        (mt5.TIMEFRAME_D1, 1),
    ]
    
    all_candles = []

    for tf, count in timeframes:
        candles = get_candles(symbol, tf, count)
        if candles is None or len(candles) == 0:
            return {"bias": "غير معروف", "reason": f"❌ لم يتم تحميل بيانات فريم {tf}"}
        all_candles.append(candles)

    # حساب نصف الذيل من الفريم الأكبر نزولاً
    for candles in all_candles[:-1]:  # بدون اليومية
        ref_candle = candles[-1]
        half_wick = get_half_wick(ref_candle)
        daily = all_candles[-1][-1]  # الشمعة اليومية
        if daily['close'] > half_wick:
            if detect_fvg(all_candles[-1]):
                return {
                    "bias": "صعودي",
                    "reason": f"✅ الشمعة اليومية أغلقت فوق 0.5 wick لشمعة فريم أكبر وتم تأكيد الكسر بـ FVG."
                }
        elif daily['close'] < half_wick:
            if detect_fvg(all_candles[-1]):
                return {
                    "bias": "هبوطي",
                    "reason": f"✅ الشمعة اليومية أغلقت تحت 0.5 wick لشمعة فريم أكبر وتم تأكيد الكسر بـ FVG."
                }

    return {
        "bias": "محايد",
        "reason": "🔍 لم يتم تأكيد كسر لأي ذيل من الفريمات العليا بظهور FVG."
    }
