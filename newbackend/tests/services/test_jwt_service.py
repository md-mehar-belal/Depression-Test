from flask import Flask, request

from app.services.jwt_service import (
    create_access_token,
    create_refresh_token,
    decode_token,
    verify_token,
    extract_token
)


# =========================================================
# ACCESS TOKEN TESTS
# =========================================================

def test_create_access_token():

    payload = {
        "user_id": "123",
        "email": "kushal@test.com"
    }

    token = create_access_token(payload)

    assert isinstance(token, str)

    decoded_payload = decode_token(token)

    assert decoded_payload is not None
    assert decoded_payload["user_id"] == "123"
    assert decoded_payload["email"] == "kushal@test.com"
    assert decoded_payload["type"] == "access"

    assert "exp" in decoded_payload
    assert "iat" in decoded_payload


def test_create_refresh_token():

    payload = {
        "user_id": "123",
        "email": "kushal@test.com"
    }

    token = create_refresh_token(payload)

    assert isinstance(token, str)

    decoded_payload = decode_token(token)

    assert decoded_payload is not None
    assert decoded_payload["user_id"] == "123"
    assert decoded_payload["email"] == "kushal@test.com"
    assert decoded_payload["type"] == "refresh"

    assert "exp" in decoded_payload
    assert "iat" in decoded_payload


# =========================================================
# DECODE TOKEN TESTS
# =========================================================

def test_decode_valid_access_token():

    token = create_access_token({
        "user_id": "123"
    })

    decoded_payload = decode_token(token)

    assert decoded_payload is not None
    assert decoded_payload["user_id"] == "123"


def test_decode_valid_refresh_token():

    token = create_refresh_token({
        "user_id": "456"
    })

    decoded_payload = decode_token(token)

    assert decoded_payload is not None
    assert decoded_payload["user_id"] == "456"


def test_decode_invalid_token():

    decoded_payload = decode_token(
        "invalid.jwt.token"
    )

    assert decoded_payload is None


def test_decode_malformed_token():

    decoded_payload = decode_token(
        "not-a-token"
    )

    assert decoded_payload is None


def test_decode_empty_token():

    decoded_payload = decode_token("")

    assert decoded_payload is None


# =========================================================
# VERIFY TOKEN TESTS
# =========================================================

def test_verify_valid_access_token():

    token = create_access_token({
        "user_id": "123",
        "email": "kushal@test.com"
    })

    payload = verify_token(token)

    assert payload is not None
    assert payload["user_id"] == "123"
    assert payload["email"] == "kushal@test.com"
    assert payload["type"] == "access"


def test_verify_valid_refresh_token():

    token = create_refresh_token({
        "user_id": "123"
    })

    payload = verify_token(
        token,
        expected_type="refresh"
    )

    assert payload is not None
    assert payload["user_id"] == "123"
    assert payload["type"] == "refresh"


def test_verify_wrong_token_type():

    token = create_refresh_token({
        "user_id": "123"
    })

    payload = verify_token(
        token,
        expected_type="access"
    )

    assert payload is None


def test_verify_invalid_token():

    payload = verify_token(
        "invalid-token"
    )

    assert payload is None


def test_verify_empty_token():

    payload = verify_token("")

    assert payload is None


# =========================================================
# EXTRACT TOKEN TESTS
# =========================================================

def test_extract_token_success():

    app = Flask(__name__)

    token = create_access_token({
        "user_id": "123"
    })

    with app.test_request_context(
        headers={
            "Authorization": f"Bearer {token}"
        }
    ):

        extracted_token = extract_token(request)

        assert extracted_token == token


def test_extract_token_missing_header():

    app = Flask(__name__)

    with app.test_request_context():

        extracted_token = extract_token(request)

        assert extracted_token is None


def test_extract_token_invalid_prefix():

    app = Flask(__name__)

    with app.test_request_context(
        headers={
            "Authorization": "Token abc123"
        }
    ):

        extracted_token = extract_token(request)

        assert extracted_token is None


def test_extract_token_empty_bearer():

    app = Flask(__name__)

    with app.test_request_context(
        headers={
            "Authorization": "Bearer "
        }
    ):

        extracted_token = extract_token(request)

        assert extracted_token is None


def test_extract_token_whitespace_bearer():

    app = Flask(__name__)

    with app.test_request_context(
        headers={
            "Authorization": "Bearer      "
        }
    ):

        extracted_token = extract_token(request)

        assert extracted_token is None