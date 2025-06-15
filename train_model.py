import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# تحميل البيانات
df = pd.read_csv("market_data.csv")

# اختر الميزات (features) والهدف (target)
features = ['open', 'high', 'low', 'close', 'tick_volume', 'spread', 'has_fvg', 'has_ob', 'has_breaker', 'smt_bullish', 'smt_bearish']
target = 'bias'  # تأكد أن عمود التحيز موجود في CSV مع تصنيفات مناسبة

# تحويل التحيز النصي إلى أرقام (مثلاً: صعودي = 1، هبوطي = 0)
df[target] = df[target].map({'صعودي': 1, 'هبوطي': 0})

# إزالة الصفوف التي بها قيم مفقودة
df = df.dropna()

X = df[features]
y = df[target]

# تقسيم البيانات تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# إنشاء نموذج الغابة العشوائية وتدريبه
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# اختبار النموذج
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"دقة النموذج: {accuracy * 100:.2f}%")

# حفظ النموذج المدرب
joblib.dump(model, "trained_model.pkl")
print("✅ تم حفظ النموذج بنجاح في trained_model.pkl")
