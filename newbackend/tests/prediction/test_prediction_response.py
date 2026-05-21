VALID_RESPONSE = {
    "prediction": 1,
    "confidence_score": 0.87,
    "severity": "moderate",
    "model_used": "svm_x3_cesd",
    "recommendation": "Consider reaching out to trusted people."
}


def test_prediction_response_contains_required_fields():
    """
    Test required response fields exist.
    """

    required_fields = {
        "prediction",
        "confidence_score",
        "severity",
        "model_used"
    }

    assert required_fields.issubset(
        VALID_RESPONSE.keys()
    )


def test_prediction_response_prediction_type():
    """
    Test prediction datatype.
    """

    assert isinstance(
        VALID_RESPONSE["prediction"],
        int
    )


def test_prediction_response_confidence_type():
    """
    Test confidence datatype.
    """

    assert isinstance(
        VALID_RESPONSE["confidence_score"],
        float
    )


def test_prediction_response_confidence_range():
    """
    Confidence score must be between 0 and 1.
    """

    confidence = VALID_RESPONSE[
        "confidence_score"
    ]

    assert 0.0 <= confidence <= 1.0


def test_prediction_response_severity_type():
    """
    Test severity datatype.
    """

    assert isinstance(
        VALID_RESPONSE["severity"],
        str
    )


def test_prediction_response_valid_severity():
    """
    Validate severity labels.
    """

    allowed_severity = {
        "minimal",
        "mild",
        "moderate",
        "severe"
    }

    assert VALID_RESPONSE[
        "severity"
    ] in allowed_severity


def test_prediction_response_model_used_type():
    """
    Test model name datatype.
    """

    assert isinstance(
        VALID_RESPONSE["model_used"],
        str
    )


def test_prediction_response_model_used_not_empty():
    """
    Ensure model identifier exists.
    """

    assert len(
        VALID_RESPONSE["model_used"]
    ) > 0


def test_prediction_response_optional_recommendation():
    """
    Recommendation field should be string when present.
    """

    assert isinstance(
        VALID_RESPONSE["recommendation"],
        str
    )


def test_prediction_response_prediction_not_negative():
    """
    Prediction output should never be negative.
    """

    assert VALID_RESPONSE[
        "prediction"
    ] >= 0


def test_prediction_response_confidence_precision():
    """
    Validate confidence precision consistency.
    """

    confidence = VALID_RESPONSE[
        "confidence_score"
    ]

    decimal_part = str(confidence).split(".")[-1]

    assert len(decimal_part) <= 4


def test_prediction_response_serializable():
    """
    Ensure response can be JSON serialized.
    """

    import json

    serialized = json.dumps(
        VALID_RESPONSE
    )

    assert isinstance(
        serialized,
        str
    )