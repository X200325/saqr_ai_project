import MetaTrader5 as mt5
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# تأكد من الاتصال بـ MetaTrader 5
if not mt5.initialize():
    print("فشل الاتصال بـ MT5")
    mt5.shutdown()

# نموذج بيانات السوق
class MarketData(BaseModel):
    open: float
    high: float
    low: float
    close: float
    tick_volume: int
    spread: int
    has_fvg: bool
    has_ob: bool
    has_breaker: bool
    smt_bullish: bool
    smt_bearish: bool

@app.get("/get_market_data")
async def get_market_data(symbol: str, timeframe: str = 'M1', num_bars: int = 1000):
    try:
        timeframe_map = {
            'M1': mt5.TIMEFRAME_M1,
            'M5': mt5.TIMEFRAME_M5,
            'M15': mt5.TIMEFRAME_M15,
            'H1': mt5.TIMEFRAME_H1
        }
        
        if timeframe not in timeframe_map:
            raise HTTPException(status_code=400, detail="الفريم الزمني غير صالح")
        
        # سحب بيانات السوق من MT5
        rates = mt5.copy_rates_from_pos(symbol, timeframe_map[timeframe], 0, num_bars)

        if rates is None or len(rates) == 0:
            raise HTTPException(status_code=404, detail="لا توجد بيانات للسوق")
        
        # تحويل البيانات إلى DataFrame
        rates_frame = pd.DataFrame(rates)
        return rates_frame.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"حدث خطأ: {str(e)}")
