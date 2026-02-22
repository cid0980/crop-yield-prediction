from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import joblib

from config import CATEGORICAL_FEATURES, MODEL_PATH, NUMERIC_FEATURES
from preprocess import load_data


def train():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, NUMERIC_FEATURES),
        ("cat", categorical_pipeline, CATEGORICAL_FEATURES),
    ])

    model = Pipeline([
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(n_estimators=300, random_state=42),
        ),
    ])

    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    joblib.dump(model, MODEL_PATH)
    print(f"Model trained and saved successfully. R^2 score: {score:.4f}")


if __name__ == "__main__":
    train()
