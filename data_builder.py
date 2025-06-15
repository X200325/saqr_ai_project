import MetaTrader5 as mt5
import pandas as pd
import numpy as np

# ✅ الاتصال بـ MT5
if not mt5.initialize():
    raise Exception("❌ فشل الاتصال بـ MetaTrader 5")

# ✅ تحميل بيانات 100 شمعة من فريم الساعة
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_H1, 0, 100)

# ✅ تحويل إلى DataFrame
data = pd.DataFrame(rates)
data['time'] = pd.to_datetime(data['time'], unit='s')

# ✅ إشارات FVG (بسيطة)
def detect_fvg(df):
    fvg_list = []
    for i in range(len(df) - 2):
        if df['low'][i+2] > df['high'][i]:
            fvg_list.append(1)
        else:
            fvg_list.append(0)
    fvg_list += [0, 0]
    return fvg_list

# ✅ إشارات OB (تقريبية)
def detect_order_blocks(df):
    ob_list = []
    for i in range(len(df)):
        if df['close'][i] < df['open'][i]:
            ob_list.append(1)  # Bearish OB
        elif df['close'][i] > df['open'][i]:
            ob_list.append(1)  # Bullish OB
        else:
            ob_list.append(0)
    return ob_list

# ✅ Breaker (بسيطة)
def detect_breaker(df):
    return [1 if i % 10 == 0 else 0 for i in range(len(df))]

# ✅ إشارات SMT
def detect_smt(df):
    smt_bullish = [1 if i % 7 == 0 else 0 for i in range(len(df))]
    smt_bearish = [1 if i % 11 == 0 else 0 for i in range(len(df))]
    return smt_bullish, smt_bearish

# ✅ استخراج الإشارات
data["has_fvg"] = detect_fvg(data)
data["has_ob"] = detect_order_blocks(data)
data["has_breaker"] = detect_breaker(data)
data["smt_bullish"], data["smt_bearish"] = detect_smt(data)

# ✅ توليد عمود التحيز (بسيط لتجريب الذكاء الاصطناعي)
def calc_bias(row):
    if row["close"] > row["open"]:
        return "صعودي"
    else:
        return "هبوطي"

data["bias"] = data.apply(calc_bias, axis=1)

# ✅ حفظ البيانات
data.to_csv("market_data.csv", index=False)
print("✅ تم إنشاء market_data.csv بنجاح.")
