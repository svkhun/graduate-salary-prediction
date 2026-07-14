"""Train the salary-prediction model from an authorised CSV dataset."""

from __future__ import annotations

import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


RAW_FEATURES = [
    "aptitude_score",
    "coding_skill_score",
    "communication_skill_score",
    "logical_reasoning_score",
]
MODEL_FEATURES = [*RAW_FEATURES, "total_skill", "avg_skill"]
TARGET = "salary_package_lpa"


def prepare_features(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Validate required fields and build the engineered model features."""
    required_columns = [*RAW_FEATURES, TARGET]
    missing_columns = sorted(set(required_columns) - set(dataframe.columns))
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing_columns)}")

    prepared = dataframe.copy()
    prepared["total_skill"] = prepared[RAW_FEATURES].sum(axis=1)
    prepared["avg_skill"] = prepared[RAW_FEATURES].mean(axis=1)
    prepared = prepared.dropna(subset=[*MODEL_FEATURES, TARGET])
    if prepared.empty:
        raise ValueError("No complete rows are available after removing missing values.")
    return prepared


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the graduate salary-prediction model.")
    parser.add_argument("--data", type=Path, required=True, help="Path to an authorised CSV dataset")
    parser.add_argument("--output", type=Path, default=Path("model.pkl"), help="Output model path")
    args = parser.parse_args()

    dataframe = prepare_features(pd.read_csv(args.data))
    features = dataframe[MODEL_FEATURES]
    target = dataframe[TARGET]
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = make_pipeline(StandardScaler(), LinearRegression())
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, args.output)

    rmse = mean_squared_error(y_test, predictions) ** 0.5
    print(f"Saved model: {args.output}")
    print(f"Rows used: {len(dataframe)}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2: {r2_score(y_test, predictions):.4f}")


if __name__ == "__main__":
    main()
