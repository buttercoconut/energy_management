# Simple regression model for energy consumption prediction

import numpy as np
from sklearn.linear_model import LinearRegression
from typing import List

class EnergyPredictor:
    """A very simple linear regression model that predicts next hour energy usage based on past data."""

    def __init__(self):
        self.model = LinearRegression()
        self.is_trained = False

    def train(self, timestamps: List[float], values: List[float]):
        X = np.array(timestamps).reshape(-1, 1)
        y = np.array(values)
        self.model.fit(X, y)
        self.is_trained = True

    def predict_next(self, next_timestamp: float) -> float:
        if not self.is_trained:
            raise RuntimeError("Model has not been trained yet")
        return float(self.model.predict([[next_timestamp]])[0])
