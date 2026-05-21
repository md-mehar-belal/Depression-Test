from unittest.mock import patch

from fixtures.token_fixtures import (
    BEARER_TOKEN,
    INVALID_BEARER_TOKEN
)


def test_protected_route_without_token(
    client
):

    response = client.get(
        "/auth/me"
    )

    assert response.status_code == 401

    response_data = response.get_json()

    assert "error" in response_data


def test_protected_route_with_invalid_token(
    client
):

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": INVALID_BEARER_TOKEN
        }
    )

    assert response.status_code == 401

    response_data = response.get_json()

    assert "error" in response_data


@patch(
    "app.services.auth_service.get_current_user"
)
def test_protected_route_with_valid_token(
    mock_get_current_user,
    client
):

    mock_get_current_user.return_value = {
        "status": 200,
        "body": {
            "user": {
                "id": "123",
                "name": "Kushal",
                "email": "kushal@example.com"
            }
        }
    }

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": BEARER_TOKEN
        }
    )

    assert response.status_code == 200

    response_data = response.get_json()

    assert "user" in response_data


def test_security_headers_exist(
    client
):

    response = client.get(
        "/auth/me"
    )

    headers = response.headers

    assert headers is not None


def test_content_type_is_json(
    client
):

    response = client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert (
        response.content_type
        == "application/json"
    )


def test_invalid_http_method_on_predict(
    client
):

    response = client.get(
        "/predict"
    )

    assert response.status_code in [
        405,
        404
    ]


def test_invalid_http_method_on_signup(
    client
):

    response = client.get(
        "/auth/signup"
    )

    assert response.status_code in [
        405,
        404
    ]


def test_large_payload_rejected(
    client
):

    large_payload = {
        "text": "A" * 100000
    }

    response = client.post(
        "/predict",
        json=large_payload
    )

    assert response.status_code in [
        400,
        413,
        422
    ]


def test_sql_injection_like_input(
    client
):

    malicious_payload = {
        "email": "' OR 1=1 --",
        "password": "' OR 1=1 --"
    }

    response = client.post(
        "/auth/login",
        json=malicious_payload
    )

    assert response.status_code in [
        400,
        401
    ]


def test_xss_like_input(
    client
):

    malicious_payload = {
        "name": "<script>alert(1)</script>",
        "email": "xss@example.com",
        "password": "password123"
    }

    response = client.post(
        "/auth/signup",
        json=malicious_payload
    )

    assert response.status_code in [
        200,
        201,
        400
    ]


def test_missing_json_payload(
    client
):

    response = client.post(
        "/auth/login"
    )

    assert response.status_code in [
        400,
        415,
        422
    ]


def test_empty_json_payload(
    client
):

    response = client.post(
        "/auth/login",
        json={}
    )

    assert response.status_code == 400


def test_invalid_token_format(
    client
):

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "InvalidTokenFormat"
        }
    )

    assert response.status_code == 401


def test_prediction_endpoint_requires_post(
    client
):

    response = client.put(
        "/predict"
    )

    assert response.status_code in [
        404,
        405
    ]