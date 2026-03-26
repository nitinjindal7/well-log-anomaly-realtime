import joblib
from sklearn.ensemble import IsolationForest
from src.preprocess import load_logs
import os
os.makedirs("models", exist_ok=True)
df = load_logs("data/volve_sample.csv")
model = IsolationForest(n_estimators=200, contamination=0.05, random_state=42)
model.fit(df)
joblib.dump(model, "models/isolation_forest.pkl")
print("done")
