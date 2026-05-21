from datetime import datetime, timedelta, UTC

import jwt
import pytest


JWT_SECRET = "test-secret-key"
JWT_ALGORITHM = "HS256"


def generate_token(payload):

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


def test_jwt_token_generation():

    payload = {
        "user_id": "123",
        "email": "test@example.com",
        "exp": datetime.now(UTC) + timedelta(hours=1)
    }

    token = generate_token(payload)

    assert isinstance(token, str)

    assert len(token) > 20


def test_jwt_token_decoding():

    payload = {
        "user_id": "123",
        "email": "test@example.com",
        "exp": datetime.now(UTC) + timedelta(hours=1)
    }

    token = generate_token(payload)

    decoded_payload = jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[JWT_ALGORITHM]
    )

    assert decoded_payload["user_id"] == "123"

    assert decoded_payload["email"] == "test@example.com"


def test_expired_jwt_token():

    payload = {
        "user_id": "123",
        "email": "expired@example.com",
        "exp": datetime.now(UTC) - timedelta(seconds=1)
    }

    token = generate_token(payload)

    with pytest.raises(jwt.ExpiredSignatureError):

        jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )


def test_invalid_secret_key():

    payload = {
        "user_id": "123",
        "email": "test@example.com",
        "exp": datetime.now(UTC) + timedelta(hours=1)
    }

    token = generate_token(payload)

    with pytest.raises(jwt.InvalidTokenError):

        jwt.decode(
            token,
            "wrong-secret-key",
            algorithms=[JWT_ALGORITHM]
        )


def test_tampered_jwt_token():

    payload = {
        "user_id": "123",
        "email": "test@example.com",
        "exp": datetime.now(UTC) + timedelta(hours=1)
    }

    token = generate_token(payload)

    tampered_token = token + "corrupted"

    with pytest.raises(jwt.InvalidTokenError):

        jwt.decode(
            tampered_token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )


def test_bearer_token_extraction():

    token = "sample.jwt.token"

    authorization_header = f"Bearer {token}"

    extracted_token = authorization_header.replace(
        "Bearer ",
        ""
    )

    assert extracted_token == token