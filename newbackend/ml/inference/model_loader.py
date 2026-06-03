# ml/inference/model_loader.py

import joblib
from app.constants.model_paths import MODEL_PATHS

_MODELS = {}

def initialize_ml_models() -> None:
    _MODELS["bdi"] = joblib.load(
        MODEL_PATHS["bdi"]
    )

    _MODELS["phq9"] = joblib.load(
        MODEL_PATHS["phq9"]
    )

    _MODELS["cesd"] = joblib.load(
        MODEL_PATHS["cesd"]
    )


def get_model(model_name: str):

    try:
        return _MODELS[model_name]

    except KeyError:
        raise RuntimeError(
            f"{model_name} model not initialized."
        )


def get_bdi_model():
    return get_model("bdi")

def get_phq9_model():
    return get_model("phq9")

def get_cesd_model():
    return get_model("cesd")
