import pytest

from ml.preprocessing.feature_selector import (
    select_x1_features,
    select_x3_features
)

from fixtures.prediction_payloads import (
    VALID_PREDICTION_PAYLOAD
)


X1_FEATURES = [
    "Melancholic",
    "Future_Hopelessness",
    "Interest_Loss",
    "Feeling_Down",
    "Fatigue_Frequency"
]


X3_FEATURES = [
    "Gender",
    "Age",
    "Financial_Pressure",
    "Sleep_Duration",
    "Social_Media_Hours",
    "Melancholic",
    "Feeling_Down"
]


def test_select_x1_features_returns_dictionary():

    selected_features = select_x1_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert isinstance(
        selected_features,
        dict
    )


def test_select_x1_features_contains_expected_fields():

    selected_features = select_x1_features(
        VALID_PREDICTION_PAYLOAD
    )

    for feature in X1_FEATURES:

        assert feature in selected_features


def test_select_x1_features_excludes_unrelated_fields():

    selected_features = select_x1_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert (
        "Gender" not in selected_features
    )


def test_select_x3_features_returns_dictionary():

    selected_features = select_x3_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert isinstance(
        selected_features,
        dict
    )


def test_select_x3_features_contains_expected_fields():

    selected_features = select_x3_features(
        VALID_PREDICTION_PAYLOAD
    )

    for feature in X3_FEATURES:

        assert feature in selected_features


def test_select_x3_features_preserves_values():

    selected_features = select_x3_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert (
        selected_features["Age"] == 22
    )

    assert (
        selected_features["Gender"] == 1
    )


def test_select_x1_features_returns_subset():

    selected_features = select_x1_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert (
        len(selected_features)
        < len(VALID_PREDICTION_PAYLOAD)
    )


def test_select_x3_features_returns_subset():

    selected_features = select_x3_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert (
        len(selected_features)
        < len(VALID_PREDICTION_PAYLOAD)
    )


def test_select_x1_features_handles_missing_feature():

    incomplete_payload = {
        key: value
        for key, value in
        VALID_PREDICTION_PAYLOAD.items()
        if key != "Melancholic"
    }

    with pytest.raises(KeyError):

        select_x1_features(
            incomplete_payload
        )


def test_select_x3_features_handles_missing_feature():

    incomplete_payload = {
        key: value
        for key, value in
        VALID_PREDICTION_PAYLOAD.items()
        if key != "Age"
    }

    with pytest.raises(KeyError):

        select_x3_features(
            incomplete_payload
        )