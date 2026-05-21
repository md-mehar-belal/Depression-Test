from typing import Any

import joblib
from sklearn.base import BaseEstimator

from ml.models import (
    FEATURE_ORDERS_DIR,
    TRAINED_MODELS_DIR,
)

MODELS: dict[str, BaseEstimator] = {}
FEATURE_ORDERS: dict[str, list[str]] = {}


def _build_model_key(
    model_type: str,
    feature_set: str,
    test_type: str,
) -> str:
    return f"{model_type}:{feature_set}:{test_type}"


def _build_feature_key(
    feature_set: str,
    test_type: str,
) -> str:
    return f"{feature_set}:{test_type}"


def load_models() -> dict[str, BaseEstimator]:
    """
    Load all trained ML models into memory.
    """

    loaded_models: dict[str, BaseEstimator] = {}

    model_files = list(
        TRAINED_MODELS_DIR.glob("*.pkl")
    )

    if not model_files:
        raise RuntimeError(
            "No trained model files found."
        )

    for model_file in model_files:

        filename = model_file.stem

        try:
            model_type, feature_set, test_type = (
                _parse_model_filename(filename)
            )

        except ValueError as exc:
            raise RuntimeError(
                f"Invalid model filename: {filename}"
            ) from exc

        model_key = _build_model_key(
            model_type,
            feature_set,
            test_type,
        )

        if model_key in loaded_models:
            raise RuntimeError(
                f"Duplicate model key: {model_key}"
            )

        try:
            model = joblib.load(model_file)

        except Exception as exc:
            raise RuntimeError(
                f"Failed to load model "
                f"{model_file.name}: {exc}"
            ) from exc

        if not hasattr(model, "predict"):
            raise RuntimeError(
                f"Loaded object is not a valid model: "
                f"{model_file.name}"
            )

        loaded_models[model_key] = model

    return loaded_models


def load_feature_orders() -> dict[str, list[str]]:
    """
    Load all feature-order mappings.
    """

    loaded_features: dict[str, list[str]] = {}

    feature_files = list(
        FEATURE_ORDERS_DIR.glob("*.pkl")
    )

    if not feature_files:
        raise RuntimeError(
            "No feature-order files found."
        )

    for feature_file in feature_files:

        filename = feature_file.stem

        try:
            feature_set, test_type = (
                filename.rsplit("_", 1)
            )

        except ValueError as exc:
            raise RuntimeError(
                f"Invalid feature-order filename: "
                f"{filename}"
            ) from exc

        feature_key = _build_feature_key(
            feature_set,
            test_type,
        )

        if feature_key in loaded_features:
            raise RuntimeError(
                f"Duplicate feature key: "
                f"{feature_key}"
            )

        try:
            feature_order = joblib.load(feature_file)

        except Exception as exc:
            raise RuntimeError(
                f"Failed to load feature order "
                f"{feature_file.name}: {exc}"
            ) from exc

        if (
            not isinstance(feature_order, list)
            or not feature_order
        ):
            raise RuntimeError(
                f"Invalid feature order: "
                f"{feature_key}"
            )

        loaded_features[feature_key] = feature_order

    return loaded_features


def initialize_ml_models() -> None:
    """
    Initialize ML inference registry atomically.
    """

    global MODELS
    global FEATURE_ORDERS

    models = load_models()
    feature_orders = load_feature_orders()

    if not models:
        raise RuntimeError(
            "Model registry is empty."
        )

    if not feature_orders:
        raise RuntimeError(
            "Feature-order registry is empty."
        )

    MODELS = models
    FEATURE_ORDERS = feature_orders