import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime

# ✅ الاتصال بمنصة MT5
if not mt5.initialize():
    raise Exception("❌ فشل الاتصال بمنصة MT5")

# ✅ إعداد الزوج والفريمات
symbol = "EURUSD"
timeframes = {
    "MN1": mt5.TIMEFRAME_MN1,
    "W1": mt5.TIMEFRAME_W1,
    "D1": mt5.TIMEFRAME_D1,
    "H4": mt5.TIMEFRAME_H4,
    "H1": mt5.TIMEFRAME_H1,
    "M15": mt5.TIMEFRAME_M15
}
n_bars = 500

# ✅ جلب البيانات وتحويلها إلى DataFrame
all_data = []
for name, tf in timeframes.items():
    data = mt5.copy_rates_from_pos(symbol, tf, 0, n_bars)
    if data is not None:
        df = pd.DataFrame(data)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['timeframe'] = name
        all_data.append(df)

# ✅ دمج كل البيانات
combined_df = pd.concat(all_data, ignore_index=True)

# ✅ حفظها لمرحلة التعلم الآلي
combined_df.to_csv("market_data.csv", index=False)
print("✅ تم حفظ البيانات في market_data.csv")

mt5.shutdown()
