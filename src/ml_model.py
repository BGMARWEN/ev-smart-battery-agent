import numpy as np
from sklearn.ensemble import RandomForestRegressor

class BatteryMLModel:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=50, random_state=42)
        self._train_dummy_model()

    def _train_dummy_model(self):
        X = np.random.uniform(low=[5, -10, 20], high=[100, 45, 130], size=(1000, 3))
        y = X[:, 0] * 4.0 * (1 - np.abs(X[:, 1] - 20) * 0.008) * (1 - (X[:, 2] - 60)**2 * 0.00003)
        self.model.fit(X, y)

    def predict_range(self, soc, temp, speed):
        features = np.array([[soc, temp, speed]])
        predicted_range = self.model.predict(features)[0]
        return max(0, round(predicted_range, 1))