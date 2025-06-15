import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump

# تحميل البيانات
data = pd.read_csv("market_data.csv")

# استخراج الميزات (features) والهدف (target)
X = data[["open", "high", "low", "close", "has_fvg", "has_ob", "has_breaker", "smt_bullish", "smt_bearish"]]
y = data["bias"]  # صعودي أو هبوطي

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تدريب النموذج
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# تقييم النموذج
predictions = model.predict(X_test)
print("📊 تقرير التقييم:\n", classification_report(y_test, predictions))

# حفظ النموذج
dump(model, "bias_model.joblib")
print("✅ تم حفظ النموذج بنجاح.")
