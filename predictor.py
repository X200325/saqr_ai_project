import pandas as pd
import joblib  # لتحميل النموذج المدرب
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List

# تحميل النموذج المدرب
model = joblib.load("trained_model.pkl")

# تهيئة نموذج البيانات
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

def predict_market_direction(new_data: pd.DataFrame):
    # تأكد أن new_data يحتوي على نفس الأعمدة التي استخدمناها في التدريب
    features = ["open", "high", "low", "close", "tick_volume", "spread", "has_fvg", "has_ob", "has_breaker", "smt_bullish", "smt_bearish"]
    
    # تأكد من أن كل الأعمدة موجودة في بيانات الإدخال
    missing_columns = set(features) - set(new_data.columns)
    if missing_columns:
        raise HTTPException(status_code=400, detail=f"المعلومات التالية مفقودة في البيانات: {', '.join(missing_columns)}")
    
    X = new_data[features]
    
    try:
        # التنبؤ
        predictions = model.predict(X)
        
        # تحويل التنبؤات إلى نصوص (صعودي / هبوطي)
        result = ["صعودي" if p == 1 else "هبوطي" for p in predictions]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"حدث خطأ أثناء التنبؤ: {str(e)}")

def get_predictions(market_data: List[MarketData]):
    # تحويل بيانات الطلب إلى DataFrame
    try:
        new_data = pd.DataFrame([data.dict() for data in market_data])
    except Exception as e:
        raise HTTPException(status_code=400, detail="فشل تحويل البيانات إلى تنسيق صالح")
    
    # إجراء التنبؤ
    try:
        predictions = predict_market_direction(new_data)
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
