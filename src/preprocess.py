import pandas as pd

from config import DATA_PATH, FEATURES, TARGET


def load_data():
    data = pd.read_csv(DATA_PATH)

    required_columns = FEATURES + [TARGET]
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(
            "Dataset is missing required column(s): "
            + ", ".join(missing_columns)
            + ". Update data/crop_yield.csv to use the crop feature schema."
        )

    X = data[FEATURES]
    y = data[TARGET]
    return X, y
