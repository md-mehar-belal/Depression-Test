import copy


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


def test_predict_endpoint_success(
    client,
    auth_headers
):
    """
    Test successful prediction generation.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    expected_fields = {
        "prediction",
        "confidence_score",
        "severity",
        "model_used"
    }

    assert expected_fields.issubset(
        data.keys()
    )


def test_predict_endpoint_response_types(
    client,
    auth_headers
):
    """
    Validate prediction response datatypes.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers=auth_headers
    )

    data = response.get_json()

    assert isinstance(
        data["prediction"],
        int
    )

    assert isinstance(
        data["confidence_score"],
        float
    )

    assert isinstance(
        data["severity"],
        str
    )

    assert isinstance(
        data["model_used"],
        str
    )


def test_predict_endpoint_confidence_range(
    client,
    auth_headers
):
    """
    Confidence score must remain valid.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers=auth_headers
    )

    data = response.get_json()

    confidence = data[
        "confidence_score"
    ]

    assert 0.0 <= confidence <= 1.0


def test_predict_endpoint_missing_feature(
    client,
    auth_headers
):
    """
    Test missing required feature validation.
    """

    payload = copy.deepcopy(
        VALID_PAYLOAD
    )

    payload.pop("Age")

    response = client.post(
        "/predict",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_predict_endpoint_invalid_type(
    client,
    auth_headers
):
    """
    Test datatype validation.
    """

    payload = copy.deepcopy(
        VALID_PAYLOAD
    )

    payload["Age"] = "twenty-two"

    response = client.post(
        "/predict",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_predict_endpoint_invalid_range(
    client,
    auth_headers
):
    """
    Test feature range validation.
    """

    payload = copy.deepcopy(
        VALID_PAYLOAD
    )

    payload["Sleep_Duration"] = -5

    response = client.post(
        "/predict",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_predict_endpoint_empty_payload(
    client,
    auth_headers
):
    """
    Test empty request payload.
    """

    response = client.post(
        "/predict",
        json={},
        headers=auth_headers
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_predict_endpoint_null_payload(
    client,
    auth_headers
):
    """
    Null payload should fail safely.
    """

    response = client.post(
        "/predict",
        json=None,
        headers=auth_headers
    )

    assert response.status_code in [
        400,
        415
    ]


def test_predict_endpoint_without_authentication(
    client
):
    """
    Test protected prediction route
    without token.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD
    )

    assert response.status_code in [
        401,
        403
    ]


def test_predict_endpoint_invalid_token(
    client
):
    """
    Test invalid JWT access.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers={
            "Authorization": (
                "Bearer invalid-token"
            )
        }
    )

    assert response.status_code in [
        401,
        403
    ]


def test_predict_endpoint_expired_token(
    client
):
    """
    Test expired JWT rejection.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers={
            "Authorization": (
                "Bearer expired-token"
            )
        }
    )

    assert response.status_code in [
        401,
        403
    ]


def test_predict_endpoint_response_structure(
    client,
    auth_headers
):
    """
    Validate prediction response schema.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers=auth_headers
    )

    data = response.get_json()

    expected_fields = {
        "prediction",
        "confidence_score",
        "severity",
        "model_used"
    }

    assert expected_fields.issubset(
        data.keys()
    )


def test_predict_endpoint_content_types(
    client,
    auth_headers
):
    """
    Test API content type handling.
    """

    response = client.post(
        "/predict",
        data="invalid-body",
        headers={
            **auth_headers,
            "Content-Type": "text/plain"
        }
    )

    assert response.status_code in [
        400,
        415
    ]


def test_predict_endpoint_large_values(
    client,
    auth_headers
):
    """
    Test extremely large numeric values.
    """

    payload = copy.deepcopy(
        VALID_PAYLOAD
    )

    payload[
        "Social_Media_Hours"
    ] = 999999

    response = client.post(
        "/predict",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code == 400


def test_predict_endpoint_negative_values(
    client,
    auth_headers
):
    """
    Negative values should fail validation.
    """

    payload = copy.deepcopy(
        VALID_PAYLOAD
    )

    payload["Age"] = -10

    response = client.post(
        "/predict",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code == 400


def test_predict_endpoint_extra_fields(
    client,
    auth_headers
):
    """
    Unknown fields should not crash API.
    """

    payload = copy.deepcopy(
        VALID_PAYLOAD
    )

    payload["Unknown_Field"] = (
        "unexpected"
    )

    response = client.post(
        "/predict",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code in [
        200,
        400
    ]


def test_predict_endpoint_returns_json(
    client,
    auth_headers
):
    """
    API must return JSON responses.
    """

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers=auth_headers
    )

    assert response.content_type.startswith(
        "application/json"
    )


def test_predict_endpoint_is_deterministic_structure(
    client,
    auth_headers
):
    """
    Same request should produce
    same response structure.
    """

    response_one = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers=auth_headers
    )

    response_two = client.post(
        "/predict",
        json=VALID_PAYLOAD,
        headers=auth_headers
    )

    data_one = response_one.get_json()

    data_two = response_two.get_json()

    assert data_one.keys() == (
        data_two.keys()
    )