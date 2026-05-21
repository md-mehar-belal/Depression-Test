from app.validators.prediction_validator import (
    validate_prediction_input,
    validate_required_features
)


VALID_PAYLOAD = {
    "Gender": 1,
    "Relationship_Status_Single": 1,
    "Age": 22,
    "Academic Status": 3,
    "Financial_Pressure": 1,
    "Physical_Activity": 1,
    "Sleep_Duration": 7,
    "Social_Media_Hours": 3,
    "Melancholic": 1,
    "Future_Hopelessness": 1,
    "Self_Perceived_Failure": 1,
    "Interest_Loss": 1,
    "Meaninglessness": 1,
    "Feeling_Down": 1,
    "Low_Concentration": 1,
    "Isolation_Frequency": 1,
    "Loneliness_Frequency": 1
}


def test_validate_prediction_input_success():

    result = validate_prediction_input(
        VALID_PAYLOAD
    )

    assert result is True


def test_validate_required_features_success():

    result = validate_required_features(
        VALID_PAYLOAD
    )

    assert result is True


def test_validate_prediction_input_empty_payload():

    result = validate_prediction_input({})

    assert result is not True


def test_validate_prediction_input_missing_required_feature():

    payload = VALID_PAYLOAD.copy()

    payload.pop("Age")

    result = validate_required_features(
        payload
    )

    assert result is not True


def test_validate_prediction_input_invalid_gender():

    payload = VALID_PAYLOAD.copy()

    payload["Gender"] = 5

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_age_below_minimum():

    payload = VALID_PAYLOAD.copy()

    payload["Age"] = 16

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_age_above_maximum():

    payload = VALID_PAYLOAD.copy()

    payload["Age"] = 40

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_invalid_sleep_duration_low():

    payload = VALID_PAYLOAD.copy()

    payload["Sleep_Duration"] = 2

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_invalid_sleep_duration_high():

    payload = VALID_PAYLOAD.copy()

    payload["Sleep_Duration"] = 15

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_invalid_social_media_hours():

    payload = VALID_PAYLOAD.copy()

    payload["Social_Media_Hours"] = 24

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_invalid_binary_field():

    payload = VALID_PAYLOAD.copy()

    payload["Physical_Activity"] = 7

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_invalid_scale_value():

    payload = VALID_PAYLOAD.copy()

    payload["Melancholic"] = 10

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_string_in_numeric_field():

    payload = VALID_PAYLOAD.copy()

    payload["Age"] = "twenty"

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_none_value():

    payload = VALID_PAYLOAD.copy()

    payload["Age"] = None

    result = validate_prediction_input(
        payload
    )

    assert result is not True


def test_validate_prediction_input_float_for_integer_field():

    payload = VALID_PAYLOAD.copy()

    payload["Age"] = 22.5

    result = validate_prediction_input(
        payload
    )

    assert result is not True