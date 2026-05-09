# Simple linear regression model for energy prediction
import numpy as np
from sklearn.linear_model import LinearRegression

class EnergyPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.trained = False

    def train(self, X: np.ndarray, y: np.ndarray):
        self.model.fit(X, y)
        self.trained = True

    def predict(self, X: np.ndarray) -> np.ndarray:
        if not self.trained:
            raise RuntimeError("Model not trained")
        return self.model.predict(X)
