import MetaTrader5 as mt5

# دالة جلب الشموع لفريم معين
def get_candles(symbol, timeframe, count=50):
    return mt5.copy_rates_from_pos(symbol, timeframe, 0, count)

# دالة فحص الحركة السعرية
def analyze_price_action():
    symbol = "EURUSD"
    confirmations = []

    timeframes = [
        (mt5.TIMEFRAME_H4, "فريم 4 ساعات"),
        (mt5.TIMEFRAME_H1, "فريم ساعة"),
        (mt5.TIMEFRAME_M15, "فريم 15 دقيقة")
    ]

    for tf, name in timeframes:
        candles = get_candles(symbol, tf, 20)
        if not candles or len(candles) < 3:
            confirmations.append(f"❌ لا توجد بيانات كافية على {name}")
            continue

        last = candles[-1]
        prev = candles[-2]

        if last['close'] > last['open'] and last['close'] > prev['high']:
            confirmations.append(f"✅ شمعة اندفاعية صعودية على {name} تؤكد التحيز الصعودي.")
        elif last['close'] < last['open'] and last['close'] < prev['low']:
            confirmations.append(f"✅ شمعة اندفاعية هبوطية على {name} تؤكد التحيز الهبوطي.")
        else:
            confirmations.append(f"🔍 لا يوجد تأكيد واضح على {name}.")

    return confirmations
