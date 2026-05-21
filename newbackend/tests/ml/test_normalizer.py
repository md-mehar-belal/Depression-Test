import pytest

from ml.preprocessing.normalizer import (
    normalize_features,
    scale_features
)

from fixtures.prediction_payloads import (
    HIGH_RISK_PREDICTION_PAYLOAD,
    LOW_RISK_PREDICTION_PAYLOAD,
    VALID_PREDICTION_PAYLOAD
)


def test_normalize_features_returns_dictionary():

    normalized_data = normalize_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert isinstance(
        normalized_data,
        dict
    )


def test_normalize_features_preserves_keys():

    normalized_data = normalize_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert set(
        normalized_data.keys()
    ) == set(
        VALID_PREDICTION_PAYLOAD.keys()
    )


def test_normalize_features_returns_numeric_values():

    normalized_data = normalize_features(
        VALID_PREDICTION_PAYLOAD
    )

    for value in normalized_data.values():

        assert isinstance(
            value,
            (int, float)
        )


def test_scale_features_returns_dictionary():

    scaled_data = scale_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert isinstance(
        scaled_data,
        dict
    )


def test_scale_features_preserves_keys():

    scaled_data = scale_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert set(
        scaled_data.keys()
    ) == set(
        VALID_PREDICTION_PAYLOAD.keys()
    )


def test_scale_features_returns_numeric_values():

    scaled_data = scale_features(
        VALID_PREDICTION_PAYLOAD
    )

    for value in scaled_data.values():

        assert isinstance(
            value,
            (int, float)
        )


def test_normalize_features_handles_low_risk_payload():

    normalized_data = normalize_features(
        LOW_RISK_PREDICTION_PAYLOAD
    )

    assert (
        normalized_data["Melancholic"]
        >= 0
    )


def test_normalize_features_handles_high_risk_payload():

    normalized_data = normalize_features(
        HIGH_RISK_PREDICTION_PAYLOAD
    )

    assert (
        normalized_data["Future_Hopelessness"]
        >= 0
    )


def test_scale_features_handles_empty_payload():

    with pytest.raises(
        (ValueError, TypeError, KeyError)
    ):

        scale_features({})


def test_normalize_features_handles_invalid_input():

    with pytest.raises(
        (TypeError, AttributeError)
    ):

        normalize_features(None)