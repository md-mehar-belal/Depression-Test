from pathlib import Path

TRAINED_MODELS_DIR = (
    Path(__file__).resolve().parents[2]
    / "ml"
    / "models"
    / "trained_models"
)

MODEL_PATHS = {
    "bdi": TRAINED_MODELS_DIR / "logistic_regression_x1_bdi-ii.pkl",
    "phq9": TRAINED_MODELS_DIR / "random_forest_x4_phq9.pkl",
    "cesd": TRAINED_MODELS_DIR / "svm_x3_ces-d.pkl",
}