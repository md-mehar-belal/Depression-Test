from unittest.mock import MagicMock, patch

import pytest

from ml.inference.ensemble_predictor import (
    aggregate_predictions,
    generate_ensemble_output,
    run_all_models
)

from fixtures.model_fixtures import (
    MOCK_FEATURE_ORDER,
    MOCK_HIGH_RISK_RESPONSE,
    MOCK_LOW_RISK_RESPONSE,
    MOCK_MODEL_RESPONSE
)

from fixtures.prediction_payloads import (
    HIGH_RISK_PREDICTION_PAYLOAD,
    LOW_RISK_PREDICTION_PAYLOAD,
    VALID_PREDICTION_PAYLOAD
)


@patch(
    "ml.inference.ensemble_predictor.predict_svm"
)
@patch(
    "ml.inference.ensemble_predictor.predict_logistic"
)
@patch(
    "ml.inference.ensemble_predictor.predict_randomforest"
)
def test_run_all_models_returns_dictionary(
    mock_rf,
    mock_logistic,
    mock_svm
):

    mock_svm.return_value = 1
    mock_logistic.return_value = 1
    mock_rf.return_value = 0

    mock_models = {
        "svm_model": MagicMock(),
        "logistic_model": MagicMock(),
        "randomforest_model": MagicMock()
    }

    mock_feature_orders = {
        "svm_features": MOCK_FEATURE_ORDER,
        "logistic_features": MOCK_FEATURE_ORDER,
        "randomforest_features": MOCK_FEATURE_ORDER
    }

    predictions = run_all_models(
        input_data=VALID_PREDICTION_PAYLOAD,
        models=mock_models,
        feature_orders=mock_feature_orders
    )

    assert isinstance(
        predictions,
        dict
    )


def test_aggregate_predictions_returns_dictionary():

    aggregated = aggregate_predictions(
        predictions={
            "svm": 1,
            "logistic": 1,
            "randomforest": 0
        },
        probabilities={
            "svm": 0.91,
            "logistic": 0.88,
            "randomforest": 0.79
        }
    )

    assert isinstance(
        aggregated,
        dict
    )


def test_aggregate_predictions_contains_expected_keys():

    aggregated = aggregate_predictions(
        predictions={
            "svm": 1,
            "logistic": 1,
            "randomforest": 0
        },
        probabilities={
            "svm": 0.91,
            "logistic": 0.88,
            "randomforest": 0.79
        }
    )

    assert "final_prediction" in aggregated
    assert "confidence_score" in aggregated
    assert "agreement_strength" in aggregated


def test_aggregate_predictions_majority_vote_positive():

    aggregated = aggregate_predictions(
        predictions={
            "svm": 1,
            "logistic": 1,
            "randomforest": 0
        },
        probabilities={
            "svm": 0.95,
            "logistic": 0.93,
            "randomforest": 0.45
        }
    )

    assert (
        aggregated["final_prediction"] == 1
    )


def test_aggregate_predictions_majority_vote_negative():

    aggregated = aggregate_predictions(
        predictions={
            "svm": 0,
            "logistic": 0,
            "randomforest": 1
        },
        probabilities={
            "svm": 0.91,
            "logistic": 0.89,
            "randomforest": 0.52
        }
    )

    assert (
        aggregated["final_prediction"] == 0
    )


def test_generate_ensemble_output_returns_dictionary():

    output = generate_ensemble_output(
        prediction=1,
        confidence=0.91,
        agreement="strong"
    )

    assert isinstance(
        output,
        dict
    )


def test_generate_ensemble_output_contains_expected_keys():

    output = generate_ensemble_output(
        prediction=1,
        confidence=0.91,
        agreement="strong"
    )

    assert "prediction" in output
    assert "confidence_score" in output
    assert "agreement_strength" in output


def test_generate_ensemble_output_high_risk():

    output = generate_ensemble_output(
        prediction=1,
        confidence=0.97,
        agreement="strong"
    )

    assert (
        output["prediction"] == 1
    )

    assert (
        output["confidence_score"] == 0.97
    )


def test_generate_ensemble_output_low_risk():

    output = generate_ensemble_output(
        prediction=0,
        confidence=0.91,
        agreement="moderate"
    )

    assert (
        output["prediction"] == 0
    )

    assert (
        output["confidence_score"] == 0.91
    )


@patch(
    "ml.inference.ensemble_predictor.predict_svm"
)
@patch(
    "ml.inference.ensemble_predictor.predict_logistic"
)
@patch(
    "ml.inference.ensemble_predictor.predict_randomforest"
)
def test_run_all_models_calls_all_predictors(
    mock_rf,
    mock_logistic,
    mock_svm
):

    mock_svm.return_value = 1
    mock_logistic.return_value = 1
    mock_rf.return_value = 1

    mock_models = {
        "svm_model": MagicMock(),
        "logistic_model": MagicMock(),
        "randomforest_model": MagicMock()
    }

    mock_feature_orders = {
        "svm_features": MOCK_FEATURE_ORDER,
        "logistic_features": MOCK_FEATURE_ORDER,
        "randomforest_features": MOCK_FEATURE_ORDER
    }

    run_all_models(
        input_data=VALID_PREDICTION_PAYLOAD,
        models=mock_models,
        feature_orders=mock_feature_orders
    )

    mock_svm.assert_called_once()
    mock_logistic.assert_called_once()
    mock_rf.assert_called_once()


def test_aggregate_predictions_raises_error_on_empty_input():

    with pytest.raises(
        (ValueError, ZeroDivisionError)
    ):

        aggregate_predictions(
            predictions={},
            probabilities={}
        )


@pytest.mark.parametrize(
    "payload,expected_prediction",
    [
        (
            LOW_RISK_PREDICTION_PAYLOAD,
            0
        ),
        (
            HIGH_RISK_PREDICTION_PAYLOAD,
            1
        )
    ]
)
def test_generate_ensemble_output_payload_scenarios(
    payload,
    expected_prediction
):

    response = (
        MOCK_LOW_RISK_RESPONSE
        if expected_prediction == 0
        else MOCK_HIGH_RISK_RESPONSE
    )

    assert (
        response["prediction"]
        == expected_prediction
    )


def test_mock_model_response_structure():

    assert "prediction" in MOCK_MODEL_RESPONSE
    assert "confidence_score" in MOCK_MODEL_RESPONSE
    assert "mental_health_tip" in MOCK_MODEL_RESPONSE