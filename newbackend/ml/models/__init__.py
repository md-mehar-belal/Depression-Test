from pathlib import Path


BASE_MODELS_DIR = Path(__file__).resolve().parent

TRAINED_MODELS_DIR = (
    BASE_MODELS_DIR / "trained_models"
)

FEATURE_ORDERS_DIR = (
    BASE_MODELS_DIR / "feature_orders"
)