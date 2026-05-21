import jwt

from app.services.jwt_service import (
    create_access_token,
    decode_token
)


def test_generate_access_token():

    token = create_access_token({
        "user_id": "123",
        "email": "test@test.com"
    })

    assert token is not None
    assert isinstance(token, str)


def test_decode_valid_token():

    token = create_access_token({
        "user_id": "123",
        "email": "test@test.com"
    })

    payload = decode_token(token)

    assert payload["email"] == "test@test.com"


def test_decode_invalid_token():

    invalid_token = "invalid.jwt.token"

    payload = decode_token(invalid_token)

    assert payload is None


def test_decode_tampered_token():

    token = create_access_token({
        "user_id": "123"
    })

    tampered = token + "abc"

    payload = decode_token(tampered)

    assert payload is None