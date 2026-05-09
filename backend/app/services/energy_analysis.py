import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
from sqlalchemy.orm import Session

class EnergyAnalysisService:
    def __init__(self, db: Session):
        self.db = db

    def predict(self, building_id: int, timestamp: str) -> float:
        """Predict future consumption using linear regression on past data."""
        # Load historical data for the building
        df = pd.read_sql(
            f"SELECT timestamp, consumption_kwh FROM energy_consumption WHERE building_id = {building_id}",
            self.db.bind,
        )
        if df.empty:
            raise ValueError("No historical data for building")

        # Convert timestamp to numeric
        df["timestamp_num"] = pd.to_datetime(df["timestamp"]).astype(int) / 10**9
        X = df[["timestamp_num"]]
        y = df["consumption_kwh"]

        model = LinearRegression()
        model.fit(X, y)

        # Predict for requested timestamp
        ts_num = pd.to_datetime(timestamp).timestamp()
        pred = model.predict([[ts_num]])[0]
        return float(pred)
