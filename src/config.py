import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "crop_yield.csv")
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "crop_model.pkl")

FEATURES = [
    "crop_name",
    "soil_type",
    "rainfall",
    "temperature",
    "humidity",
    "fertilizer_used",
    "season",
]

NUMERIC_FEATURES = ["rainfall", "temperature", "humidity"]
CATEGORICAL_FEATURES = ["crop_name", "soil_type", "fertilizer_used", "season"]
TARGET = "yield"
