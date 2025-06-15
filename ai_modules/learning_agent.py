# نموذج بسيط لتعلم الآلة (مثال فقط)

from sklearn.ensemble import RandomForestClassifier
import numpy as np

class LearningAgent:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.trained = True

    def predict(self, X):
        if not self.trained:
            return None
        return self.model.predict(X)
