from unittest.mock import patch

from app.services.prediction_service import (
    generate_prediction,
    process_prediction,
    build_prediction_response,
    save_prediction_history
)


# =========================================================
# GENERATE PREDICTION TESTS
# =========================================================

@patch("app.services.prediction_service.process_prediction")
@patch("app.services.prediction_service.calculate_agreement_strength")
@patch("app.services.prediction_service.calculate_confidence")
@patch("app.services.prediction_service.generate_ensemble_output")
@patch("app.services.prediction_service.run_all_models")
@patch("app.services.prediction_service.normalize_features")
@patch("app.services.prediction_service.map_features")
def test_generate_prediction_success(
    mock_map_features,
    mock_normalize_features,
    mock_run_all_models,
    mock_generate_ensemble_output,
    mock_calculate_confidence,
    mock_calculate_agreement_strength,
    mock_process_prediction
):

    input_data = {
        "sleep_hours": 5,
        "stress_level": 8
    }

    mapped_features = {
        "sleep_hours": 5,
        "stress_level": 8
    }

    normalized_features = {
        "sleep_hours": 0.5,
        "stress_level": 0.8
    }

    model_results = {
        "svm": {
            "prediction": 1,
            "probability": 0.84
        },
        "logistic": {
            "prediction": 1,
            "probability": 0.81
        }
    }

    ensemble_output = {
        "prediction": 1,
        "severity": "moderate"
    }

    final_response = {
        "prediction": 1,
        "severity": "moderate",
        "confidence_score": 0.82
    }

    mock_map_features.return_value = mapped_features

    mock_normalize_features.return_value = normalized_features

    mock_run_all_models.return_value = model_results

    mock_generate_ensemble_output.return_value = ensemble_output

    mock_calculate_confidence.return_value = 0.82

    mock_calculate_agreement_strength.return_value = "strong"

    mock_process_prediction.return_value = final_response

    result = generate_prediction(input_data)

    assert result == final_response

    mock_map_features.assert_called_once_with(input_data)

    mock_normalize_features.assert_called_once_with(
        mapped_features
    )

    mock_run_all_models.assert_called_once_with(
        normalized_features
    )

    mock_generate_ensemble_output.assert_called_once_with(
        model_results
    )

    mock_calculate_confidence.assert_called_once_with(
        model_results
    )

    mock_calculate_agreement_strength.assert_called_once_with(
        model_results
    )

    mock_process_prediction.assert_called_once()


# =========================================================
# PROCESS PREDICTION TESTS
# =========================================================

@patch("app.services.prediction_service.build_prediction_response")
def test_process_prediction_success(
    mock_build_prediction_response
):

    ensemble_output = {
        "prediction": 1,
        "severity": "high"
    }

    model_results = {
        "svm": {
            "prediction": 1
        }
    }

    mock_build_prediction_response.return_value = {
        "prediction": 1,
        "severity": "high"
    }

    result = process_prediction(
        ensemble_output=ensemble_output,
        confidence_score=0.91,
        agreement_strength="strong",
        model_results=model_results
    )

    assert result["prediction"] == 1

    mock_build_prediction_response.assert_called_once()


# =========================================================
# BUILD RESPONSE TESTS
# =========================================================

@patch("app.services.prediction_service.serialize_prediction_response")
def test_build_prediction_response_success(
    mock_serialize_prediction_response
):

    mock_serialize_prediction_response.return_value = {
        "prediction": 0,
        "severity": "low"
    }

    result = build_prediction_response(
        prediction=0,
        severity="low",
        confidence_score=0.25,
        agreement_strength="weak",
        model_results={}
    )

    assert result["severity"] == "low"

    mock_serialize_prediction_response.assert_called_once()


# =========================================================
# SAVE PREDICTION HISTORY TESTS
# =========================================================

@patch("app.services.prediction_service.log_prediction")
@patch("app.services.prediction_service.save_prediction")
def test_save_prediction_history_success(
    mock_save_prediction,
    mock_log_prediction
):

    mock_save_prediction.return_value = "prediction-id"

    prediction_response = {
        "prediction": 1,
        "severity": "moderate"
    }

    result = save_prediction_history(
        user_id="user-123",
        input_data={
            "stress": 8
        },
        prediction_response=prediction_response
    )

    assert result == "prediction-id"

    mock_save_prediction.assert_called_once_with(
        user_id="user-123",
        input_data={
            "stress": 8
        },
        prediction_data=prediction_response
    )

    mock_log_prediction.assert_called_once()


# =========================================================
# FAILURE PROPAGATION TESTS
# =========================================================

@patch("app.services.prediction_service.map_features")
def test_generate_prediction_mapping_failure(
    mock_map_features
):

    mock_map_features.side_effect = ValueError(
        "Invalid features"
    )

    try:
        generate_prediction({
            "bad": "data"
        })

    except ValueError as error:
        assert str(error) == "Invalid features"


@patch("app.services.prediction_service.run_all_models")
@patch("app.services.prediction_service.normalize_features")
@patch("app.services.prediction_service.map_features")
def test_generate_prediction_model_failure(
    mock_map_features,
    mock_normalize_features,
    mock_run_all_models
):

    mock_map_features.return_value = {}

    mock_normalize_features.return_value = {}

    mock_run_all_models.side_effect = RuntimeError(
        "Model crashed"
    )

    try:
        generate_prediction({})

    except RuntimeError as error:
        assert str(error) == "Model crashed"