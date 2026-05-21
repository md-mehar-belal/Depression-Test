def test_get_prediction_history_success(
    client,
    auth_headers,
    prediction_history_factory
):
    """
    Test successful prediction history retrieval.
    """

    prediction_history_factory()

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "history" in data
    assert isinstance(
        data["history"],
        list
    )


def test_get_prediction_history_requires_authentication(
    client
):
    """
    Test protected route without token.
    """

    response = client.get(
        "/predictions/history"
    )

    assert response.status_code in [401, 403]


def test_get_prediction_history_invalid_token(
    client
):
    """
    Test invalid JWT access.
    """

    response = client.get(
        "/predictions/history",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code in [401, 403]


def test_get_prediction_history_empty(
    client,
    auth_headers
):
    """
    Test empty history response.
    """

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "history" in data
    assert data["history"] == []


def test_get_prediction_history_response_structure(
    client,
    auth_headers,
    prediction_history_factory
):
    """
    Validate prediction history schema.
    """

    prediction_history_factory()

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    data = response.get_json()

    history_item = data["history"][0]

    expected_fields = {
        "prediction_id",
        "prediction",
        "confidence_score",
        "severity",
        "model_used",
        "created_at"
    }

    assert expected_fields.issubset(
        history_item.keys()
    )


def test_get_prediction_history_prediction_type(
    client,
    auth_headers,
    prediction_history_factory
):
    """
    Validate prediction datatype.
    """

    prediction_history_factory()

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    data = response.get_json()

    item = data["history"][0]

    assert isinstance(
        item["prediction"],
        int
    )


def test_get_prediction_history_confidence_range(
    client,
    auth_headers,
    prediction_history_factory
):
    """
    Confidence must remain between 0 and 1.
    """

    prediction_history_factory()

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    data = response.get_json()

    confidence = data["history"][0][
        "confidence_score"
    ]

    assert 0.0 <= confidence <= 1.0


def test_get_prediction_history_created_at_type(
    client,
    auth_headers,
    prediction_history_factory
):
    """
    created_at must be serialized as string.
    """

    prediction_history_factory()

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    data = response.get_json()

    created_at = data["history"][0][
        "created_at"
    ]

    assert isinstance(
        created_at,
        str
    )


def test_get_prediction_history_multiple_records(
    client,
    auth_headers,
    prediction_history_factory
):
    """
    Test retrieval of multiple prediction records.
    """

    prediction_history_factory(count=3)

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    data = response.get_json()

    assert len(
        data["history"]
    ) == 3


def test_get_prediction_history_user_isolation(
    client,
    auth_headers,
    prediction_history_factory
):
    """
    Ensure users only access their own history.
    """

    prediction_history_factory(
        user_scope="another_user"
    )

    response = client.get(
        "/predictions/history",
        headers=auth_headers
    )

    data = response.get_json()

    assert data["history"] == []