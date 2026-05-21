from bson import ObjectId

from fixtures.auth_payloads import (
    VALID_LOGIN_PAYLOAD,
    VALID_SIGNUP_PAYLOAD
)


MOCK_USER = {
    "_id": ObjectId(),
    "name": VALID_SIGNUP_PAYLOAD["name"],
    "email": VALID_SIGNUP_PAYLOAD["email"],
    "password": (
        "$2b$12$KIXQ4Qzr1I6Q671O5jM7I."
        "f6xQ6fWQK5n2mQ9n1yP8w9x7mQk2z7u"
    )
}


SERIALIZED_USER = {
    "id": str(MOCK_USER["_id"]),
    "name": MOCK_USER["name"],
    "email": MOCK_USER["email"]
}


MOCK_AUTH_RESPONSE = {
    "message": "Login successful",
    "token": "mock-jwt-token",
    "user": SERIALIZED_USER
}


MOCK_SIGNUP_RESPONSE = {
    "message": "Signup successful",
    "token": "mock-jwt-token",
    "user": SERIALIZED_USER
}


MOCK_GOOGLE_USER = {
    "id": "google-user-id",
    "name": "Google User",
    "email": "googleuser@example.com"
}


MOCK_GOOGLE_AUTH_RESPONSE = {
    "message": "Google authentication successful",
    "token": "mock-google-jwt-token",
    "user": MOCK_GOOGLE_USER
}


MOCK_FORGOT_PASSWORD_RESPONSE = {
    "message": (
        f"Password reset link sent to "
        f"{VALID_LOGIN_PAYLOAD['email']}"
    )
}


MOCK_RESET_PASSWORD_RESPONSE = {
    "message": "Password reset successful"
}


MOCK_VERIFY_EMAIL_RESPONSE = {
    "message": "Email verified successfully"
}


MOCK_LOGOUT_RESPONSE = {
    "message": "Logout successful"
}