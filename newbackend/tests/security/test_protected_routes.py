from datetime import datetime, timedelta, UTC

import jwt


JWT_SECRET = "test-secret-key"
JWT_ALGORITHM = "HS256"


def create_test_token():

    payload = {
        "user_id": "123",
        "email": "test@example.com",
        "exp": datetime.now(UTC) + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


def verify_protected_route(authorization_header):

    if not authorization_header:
        return {
            "status": 401,
            "error": "Authorization token missing"
        }

    if not authorization_header.startswith(
        "Bearer "
    ):
        return {
            "status": 401,
            "error": "Invalid authorization format"
        }

    token = authorization_header.replace(
        "Bearer ",
        ""
    )

    try:

        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )

        return {
            "status": 200,
            "user_id": payload["user_id"]
        }

    except jwt.ExpiredSignatureError:

        return {
            "status": 401,
            "error": "Token expired"
        }

    except jwt.InvalidTokenError:

        return {
            "status": 401,
            "error": "Invalid token"
        }


def test_protected_route_without_token():

    response = verify_protected_route(
        None
    )

    assert response["status"] == 401

    assert (
        response["error"]
        == "Authorization token missing"
    )


def test_protected_route_with_invalid_format():

    response = verify_protected_route(
        "InvalidTokenFormat"
    )

    assert response["status"] == 401

    assert (
        response["error"]
        == "Invalid authorization format"
    )


def test_protected_route_with_valid_token():

    token = create_test_token()

    response = verify_protected_route(
        f"Bearer {token}"
    )

    assert response["status"] == 200

    assert response["user_id"] == "123"


def test_protected_route_with_tampered_token():

    token = create_test_token()

    tampered_token = token + "corrupted"

    response = verify_protected_route(
        f"Bearer {tampered_token}"
    )

    assert response["status"] == 401

    assert response["error"] == "Invalid token"


def test_protected_route_with_expired_token():

    expired_payload = {
        "user_id": "123",
        "email": "expired@example.com",
        "exp": datetime.now(UTC) - timedelta(minutes=5)
    }

    expired_token = jwt.encode(
        expired_payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

    response = verify_protected_route(
        f"Bearer {expired_token}"
    )

    assert response["status"] == 401

    assert response["error"] == "Token expired"


def test_protected_route_with_empty_bearer_token():

    response = verify_protected_route(
        "Bearer "
    )

    assert response["status"] == 401

    assert response["error"] == "Invalid token"