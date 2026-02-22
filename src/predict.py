import joblib
import pandas as pd

from config import FEATURES, MODEL_PATH


def load_model():
    return joblib.load(MODEL_PATH)


def predict(values):
    if not isinstance(values, dict):
        raise TypeError("predict() expects a dict with feature names as keys.")

    missing = [feature for feature in FEATURES if feature not in values]
    if missing:
        raise ValueError(f"Missing required input feature(s): {', '.join(missing)}")

    input_df = pd.DataFrame([values], columns=FEATURES)
    model = load_model()
    result = model.predict(input_df)
    return float(result[0])
