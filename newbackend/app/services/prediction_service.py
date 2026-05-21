from typing import Any

from app.repositories.prediction_repository import save_prediction
from app.repositories.prediction_repository import get_prediction_history
from app.schemas.history_schema import serialize_prediction_history
from app.schemas.prediction_schema import serialize_prediction_response
from app.services.logging_service import log_prediction
from app.validators.prediction_validator import validate_prediction_input

from ml.inference.ensemble_predictor import (
    generate_ensemble_output
)

from ml.preprocessing.feature_mapper import map_features
from ml.preprocessing.normalizer import normalize_features


DEFAULT_FEATURE_SET = "x3"
DEFAULT_TEST_TYPE = "phq9"
DEFAULT_MODEL_TYPES = [
    "svm",
    "logistic_regression",
    "random_forest"
]


def generate_prediction(
    input_data: dict,
    user_id: str | None = None,
    persist_history: bool = False,
    validate_input: bool = False
) -> dict[str, Any]:
    """
    Main prediction orchestration pipeline.
    """

    input_data = input_data or {}

    if validate_input:
        validation_errors = validate_prediction_input(
            input_data
        )

        if validation_errors:
            return {
                "success": False,
                "message": "Prediction validation failed",
                "errors": validation_errors
            }

    feature_set = input_data.get(
        "feature_set",
        DEFAULT_FEATURE_SET
    )
    test_type = input_data.get(
        "test_type",
        DEFAULT_TEST_TYPE
    )
    model_types = input_data.get(
        "model_types",
        DEFAULT_MODEL_TYPES
    )

    feature_input = {
        key: value
        for key, value in input_data.items()
        if key not in {
            "feature_set",
            "test_type",
            "model_types"
        }
    }

    # Step 1: Map request features
    mapped_features = map_features(feature_input)

    # Step 2: Normalize features
    normalized_result = normalize_features(mapped_features)

    if isinstance(normalized_result, tuple):
        normalized_features = normalized_result[0]
    else:
        normalized_features = normalized_result

    if hasattr(normalized_features, "iloc"):
        inference_input = (
            normalized_features.iloc[0].to_dict()
        )
    else:
        inference_input = feature_input

    # CONTRACT ISSUE:
    # This service previously called run_all_models(),
    # generate_ensemble_output(), calculate_confidence(), and
    # calculate_agreement_strength() with argument shapes that did not
    # match the ML layer. That violated the service/ML boundary and
    # caused runtime TypeError failures.
    #
    # Legacy problematic calls:
    # model_results = run_all_models(normalized_features)
    # ensemble_output = generate_ensemble_output(model_results)
    # confidence_score = calculate_confidence(model_results)
    # agreement_strength = calculate_agreement_strength(model_results)
    ensemble_output = generate_ensemble_output(
        input_data=inference_input,
        feature_set=feature_set,
        test_type=test_type,
        model_types=model_types
    )

    model_results = ensemble_output.get(
        "individual_models",
        []
    )
    ensemble_result = ensemble_output.get(
        "ensemble_result",
        {}
    )

    prediction_response = process_prediction(
        ensemble_output=ensemble_result,
        confidence_score=ensemble_result.get(
            "average_confidence",
            0.0
        ),
        agreement_strength=ensemble_result.get(
            "agreement_strength"
        ),
        model_results=model_results
    )

    if persist_history and user_id:
        save_prediction_history(
            user_id=user_id,
            input_data=input_data,
            prediction_response=prediction_response
        )

    return prediction_response


def process_prediction(
    ensemble_output: dict,
    confidence_score: float,
    agreement_strength: str,
    model_results: dict
) -> dict[str, Any]:
    """
    Processes model outputs into API-ready structure.
    """

    return build_prediction_response(
        prediction=ensemble_output.get(
            "prediction",
            ensemble_output.get("final_prediction")
        ),
        severity=ensemble_output.get(
            "severity",
            "unknown"
        ),
        confidence_score=confidence_score,
        agreement_strength=agreement_strength,
        model_results=model_results
    )


def build_prediction_response(
    prediction: int,
    severity: str,
    confidence_score: float,
    agreement_strength: str,
    model_results: dict
) -> dict[str, Any]:
    """
    Standardized prediction response serializer.
    """

    # CONTRACT ISSUE:
    # prediction_schema.serialize_prediction_response() previously did
    # not accept agreement/model metadata, while this service supplied
    # that data. The schema now accepts these optional fields and keeps
    # response shaping in the schema layer.
    return serialize_prediction_response(
        prediction=prediction,
        severity=severity,
        confidence_score=confidence_score,
        agreement_strength=agreement_strength,
        model_results=model_results
    )


def save_prediction_history(
    user_id: str,
    input_data: dict,
    prediction_response: dict
) -> str:
    """
    Persists prediction history into database.
    """

    # CONTRACT ISSUE:
    # save_prediction() accepts one prediction_data dictionary. Passing
    # separate keyword arguments violated the repository contract and
    # coupled service internals to repository parameter names.
    #
    # Legacy problematic call:
    # prediction_id = save_prediction(
    #     user_id=user_id,
    #     input_data=input_data,
    #     prediction_data=prediction_response
    # )
    saved_prediction = save_prediction({
        "user_id": user_id,
        "input_data": input_data,
        "prediction_data": prediction_response
    })

    prediction_id = saved_prediction.get("id")

    log_prediction(
        user_id=user_id,
        prediction_data=prediction_response,
        prediction_id=prediction_id
    )

    return prediction_id


def get_user_prediction_history(
    user_id: str
) -> dict[str, Any]:
    """
    Retrieve and serialize prediction history for a user.
    """

    # ARCHITECTURAL VIOLATION:
    # history_controller previously imported the prediction repository
    # directly. That bypassed the service/use-case layer and coupled
    # HTTP controllers to persistence. This function keeps repository
    # access behind the service boundary.
    history_records = get_prediction_history(
        user_id
    )

    return serialize_prediction_history(
        history_records
    )
