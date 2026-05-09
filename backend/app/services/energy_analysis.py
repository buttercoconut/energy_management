import numpy as np
from sklearn.linear_model import LinearRegression
from sqlalchemy.orm import Session
from .. import models

class EnergyAnalysisService:
    def __init__(self, db: Session):
        self.db = db

    def get_consumption_series(self, building_id: int):
        data = self.db.query(models.EnergyConsumption).filter(models.EnergyConsumption.building_id == building_id).order_by(models.EnergyConsumption.timestamp).all()
        timestamps = [d.timestamp.timestamp() for d in data]
        values = [d.value for d in data]
        return np.array(timestamps).reshape(-1, 1), np.array(values)

    def predict_next(self, building_id: int, days_ahead: int = 1):
        X, y = self.get_consumption_series(building_id)
        if len(X) < 2:
            return None
        model = LinearRegression()
        model.fit(X, y)
        future_ts = np.array([(X[-1][0] + 86400 * i) for i in range(1, days_ahead + 1)]).reshape(-1, 1)
        preds = model.predict(future_ts)
        return preds.tolist()
