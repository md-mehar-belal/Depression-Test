import pytest

from ml.preprocessing.feature_mapper import (
    align_feature_order,
    map_features
)

from fixtures.prediction_payloads import (
    INVALID_PREDICTION_PAYLOADS,
    VALID_PREDICTION_PAYLOAD
)


def test_map_features_returns_dictionary():

    mapped_features = map_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert isinstance(
        mapped_features,
        dict
    )


def test_map_features_preserves_values():

    mapped_features = map_features(
        VALID_PREDICTION_PAYLOAD
    )

    assert (
        mapped_features["Age"] == 22
    )

    assert (
        mapped_features["Gender"] == 1
    )


def test_align_feature_order_returns_list():

    ordered_features = align_feature_order(
        VALID_PREDICTION_PAYLOAD,
        list(VALID_PREDICTION_PAYLOAD.keys())
    )

    assert isinstance(
        ordered_features,
        list
    )


def test_align_feature_order_matches_feature_order():

    feature_order = [
        "Gender",
        "Age",
        "Sleep_Duration"
    ]

    ordered_features = align_feature_order(
        VALID_PREDICTION_PAYLOAD,
        feature_order
    )

    assert ordered_features == [
        VALID_PREDICTION_PAYLOAD["Gender"],
        VALID_PREDICTION_PAYLOAD["Age"],
        VALID_PREDICTION_PAYLOAD["Sleep_Duration"]
    ]


def test_align_feature_order_raises_key_error():

    feature_order = [
        "Gender",
        "Unknown_Field"
    ]

    with pytest.raises(KeyError):

        align_feature_order(
            VALID_PREDICTION_PAYLOAD,
            feature_order
        )


@pytest.mark.parametrize(
    "payload_key",
    [
        "missing_gender",
        "missing_age"
    ]
)
def test_map_features_missing_fields(
    payload_key
):

    payload = INVALID_PREDICTION_PAYLOADS[
        payload_key
    ]

    mapped_features = map_features(
        payload
    )

    assert isinstance(
        mapped_features,
        dict
    )


def test_align_feature_order_with_full_payload():

    feature_order = list(
        VALID_PREDICTION_PAYLOAD.keys()
    )

    ordered_features = align_feature_order(
        VALID_PREDICTION_PAYLOAD,
        feature_order
    )

    assert len(
        ordered_features
    ) == len(feature_order)