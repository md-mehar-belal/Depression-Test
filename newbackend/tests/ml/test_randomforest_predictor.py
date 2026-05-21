from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from ml.inference.randomforest_predictor import (
    predict_randomforest,
    predict_randomforest_probability
)

from fixtures.model_fixtures import (
    MOCK_FEATURE_ORDER,
    MOCK_HIGH_RISK_PREDICTION,
    MOCK_HIGH_RISK_PROBABILITIES,
    MOCK_LOW_RISK_PREDICTION,
    MOCK_LOW_RISK_PROBABILITIES,
    MOCK_MODEL_PREDICTION,
    MOCK_MODEL_PROBABILITIES
)

from fixtures.prediction_payloads import (
    HIGH_RISK_PREDICTION_PAYLOAD,
    LOW_RISK_PREDICTION_PAYLOAD,
    VALID_PREDICTION_PAYLOAD
)


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_returns_prediction(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict.return_value = (
        MOCK_MODEL_PREDICTION
    )

    prediction = predict_randomforest(
        model=mock_model,
        input_data=VALID_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    assert prediction == 1


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_probability_returns_float(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict_proba.return_value = (
        MOCK_MODEL_PROBABILITIES
    )

    probability = predict_randomforest_probability(
        model=mock_model,
        input_data=VALID_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    assert isinstance(
        probability,
        float
    )


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_probability_returns_expected_value(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict_proba.return_value = (
        MOCK_MODEL_PROBABILITIES
    )

    probability = predict_randomforest_probability(
        model=mock_model,
        input_data=VALID_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    assert probability == 0.88


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_handles_low_risk_prediction(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict.return_value = (
        MOCK_LOW_RISK_PREDICTION
    )

    prediction = predict_randomforest(
        model=mock_model,
        input_data=LOW_RISK_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    assert prediction == 0


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_handles_high_risk_prediction(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict.return_value = (
        MOCK_HIGH_RISK_PREDICTION
    )

    prediction = predict_randomforest(
        model=mock_model,
        input_data=HIGH_RISK_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    assert prediction == 1


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_probability_handles_low_risk(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict_proba.return_value = (
        MOCK_LOW_RISK_PROBABILITIES
    )

    probability = predict_randomforest_probability(
        model=mock_model,
        input_data=LOW_RISK_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    assert probability == 0.91


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_probability_handles_high_risk(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict_proba.return_value = (
        MOCK_HIGH_RISK_PROBABILITIES
    )

    probability = predict_randomforest_probability(
        model=mock_model,
        input_data=HIGH_RISK_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    assert probability == 0.97


def test_predict_randomforest_raises_key_error():

    mock_model = MagicMock()

    invalid_payload = {
        "Age": 22
    }

    with pytest.raises(KeyError):

        predict_randomforest(
            model=mock_model,
            input_data=invalid_payload,
            feature_order=MOCK_FEATURE_ORDER
        )


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_calls_model_predict(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict.return_value = (
        np.array([1])
    )

    predict_randomforest(
        model=mock_model,
        input_data=VALID_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    mock_model.predict.assert_called_once()


@patch("ml.inference.randomforest_predictor.pd.DataFrame")
def test_predict_randomforest_probability_calls_predict_proba(
    mock_dataframe
):

    mock_model = MagicMock()

    mock_model.predict_proba.return_value = (
        MOCK_MODEL_PROBABILITIES
    )

    predict_randomforest_probability(
        model=mock_model,
        input_data=VALID_PREDICTION_PAYLOAD,
        feature_order=MOCK_FEATURE_ORDER
    )

    mock_model.predict_proba.assert_called_once()