from datetime import datetime, timedelta, UTC

import jwt


JWT_SECRET = "test-secret-key"

JWT_ALGORITHM = "HS256"


MOCK_TOKEN_PAYLOAD = {
    "user_id": "507f1f77bcf86cd799439011",
    "email": "kushal@example.com"
}


def generate_valid_token():

    payload = {
        **MOCK_TOKEN_PAYLOAD,
        "exp": datetime.now(UTC)
        + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


def generate_expired_token():

    payload = {
        **MOCK_TOKEN_PAYLOAD,
        "exp": datetime.now(UTC)
        - timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


def generate_refresh_token():

    payload = {
        **MOCK_TOKEN_PAYLOAD,
        "type": "refresh",
        "exp": datetime.now(UTC)
        + timedelta(days=7)
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


MOCK_VALID_TOKEN = generate_valid_token()

MOCK_EXPIRED_TOKEN = (
    generate_expired_token()
)

MOCK_REFRESH_TOKEN = (
    generate_refresh_token()
)

MOCK_INVALID_TOKEN = (
    "invalid.jwt.token"
)

MOCK_TAMPERED_TOKEN = (
    MOCK_VALID_TOKEN + "tampered"
)

MOCK_EMPTY_TOKEN = ""

MOCK_BEARER_TOKEN = (
    f"Bearer {MOCK_VALID_TOKEN}"
)

MOCK_INVALID_BEARER_TOKEN = (
    "Bearer invalid.jwt.token"
)

MOCK_AUTH_HEADERS = {
    "Authorization": MOCK_BEARER_TOKEN
}

MOCK_INVALID_AUTH_HEADERS = {
    "Authorization": (
        MOCK_INVALID_BEARER_TOKEN
    )
}

MOCK_EXPIRED_AUTH_HEADERS = {
    "Authorization": (
        f"Bearer {MOCK_EXPIRED_TOKEN}"
    )
}

MOCK_DECODED_PAYLOAD = {
    "user_id": (
        "507f1f77bcf86cd799439011"
    ),
    "email": "kushal@example.com"
}