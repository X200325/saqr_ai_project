import MetaTrader5 as mt5

def get_data(symbol, timeframe, n=1):
    return mt5.copy_rates_from_pos(symbol, timeframe, 0, n)

def get_wick_half(candle):
    high = candle['high']
    low = candle['low']
    body_top = max(candle['open'], candle['close'])
    body_bottom = min(candle['open'], candle['close'])
    upper_wick = high - body_top
    lower_wick = body_bottom - low
    return low + (upper_wick + lower_wick) / 2

def analyze_bias(symbol="EURUSD"):
    yearly = get_data(symbol, mt5.TIMEFRAME_MN1, 12)
    monthly = get_data(symbol, mt5.TIMEFRAME_MN1, 1)
    weekly = get_data(symbol, mt5.TIMEFRAME_W1, 1)
    daily = get_data(symbol, mt5.TIMEFRAME_D1, 1)

    if any(data is None or len(data) == 0 for data in [yearly, monthly, weekly, daily]):
        return {"bias": "غير معروف", "reason": "⚠️ لم يتم تحميل بيانات الفريمات المطلوبة"}

    daily_close = daily[0]['close']
    monthly_half_wick = get_wick_half(monthly[0])

    if daily_close > monthly_half_wick:
        bias = "صعودي"
        reason = "الشمعة اليومية أغلقت فوق منتصف الذيل الشهري (0.5 wick)."
    else:
        bias = "هبوطي"
        reason = "الشمعة اليومية أغلقت تحت منتصف الذيل الشهري (0.5 wick)."

    return {"bias": bias, "reason": reason}
