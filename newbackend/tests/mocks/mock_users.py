from datetime import datetime, timedelta, UTC

import bcrypt
import jwt


JWT_SECRET = "test-secret-key"
JWT_ALGORITHM = "HS256"


MOCK_SIGNUP_PAYLOAD = {
    "name": "Kushal",
    "email": "kushal@example.com",
    "password": "StrongPassword123"
}


MOCK_LOGIN_PAYLOAD = {
    "email": "kushal@example.com",
    "password": "StrongPassword123"
}


MOCK_INVALID_LOGIN_PAYLOAD = {
    "email": "kushal@example.com",
    "password": "WrongPassword"
}


MOCK_USER = {
    "id": "507f1f77bcf86cd799439011",
    "name": "Kushal",
    "email": "kushal@example.com",
    "password": bcrypt.hashpw(
        "StrongPassword123".encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")
}


MOCK_SECOND_USER = {
    "id": "507f191e810c19729de860ea",
    "name": "Test User",
    "email": "test@example.com",
    "password": bcrypt.hashpw(
        "AnotherPassword123".encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")
}


def generate_mock_jwt_token():

    payload = {
        "user_id": MOCK_USER["id"],
        "email": MOCK_USER["email"],
        "exp": datetime.now(UTC)
        + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


MOCK_BEARER_TOKEN = (
    f"Bearer {generate_mock_jwt_token()}"
)


MOCK_EXPIRED_TOKEN = jwt.encode(
    {
        "user_id": MOCK_USER["id"],
        "email": MOCK_USER["email"],
        "exp": datetime.now(UTC)
        - timedelta(hours=1)
    },
    JWT_SECRET,
    algorithm=JWT_ALGORITHM
)


MOCK_AUTH_HEADERS = {
    "Authorization": MOCK_BEARER_TOKEN
}


MOCK_INVALID_AUTH_HEADERS = {
    "Authorization": "Bearer invalid.jwt.token"
}