VALID_SIGNUP_PAYLOAD = {
    "name": "Kushal Karmakar",
    "email": "kushal@example.com",
    "password": "securepassword123"
}


VALID_LOGIN_PAYLOAD = {
    "email": "kushal@example.com",
    "password": "securepassword123"
}


VALID_GOOGLE_AUTH_PAYLOAD = {
    "token": "valid-google-oauth-token"
}


VALID_FORGOT_PASSWORD_PAYLOAD = {
    "email": "kushal@example.com"
}


VALID_RESET_PASSWORD_PAYLOAD = {
    "token": "valid-reset-token",
    "password": "newsecurepassword123"
}


VALID_VERIFY_EMAIL_PAYLOAD = {
    "token": "valid-email-verification-token"
}


INVALID_SIGNUP_PAYLOADS = {
    "missing_name": {
        "email": "kushal@example.com",
        "password": "securepassword123"
    },

    "missing_email": {
        "name": "Kushal Karmakar",
        "password": "securepassword123"
    },

    "missing_password": {
        "name": "Kushal Karmakar",
        "email": "kushal@example.com"
    },

    "invalid_email": {
        "name": "Kushal Karmakar",
        "email": "invalid-email",
        "password": "securepassword123"
    },

    "short_password": {
        "name": "Kushal Karmakar",
        "email": "kushal@example.com",
        "password": "123"
    }
}


INVALID_LOGIN_PAYLOADS = {
    "missing_email": {
        "password": "securepassword123"
    },

    "missing_password": {
        "email": "kushal@example.com"
    },

    "invalid_credentials": {
        "email": "wrong@example.com",
        "password": "wrongpassword"
    }
}


INVALID_GOOGLE_AUTH_PAYLOADS = {
    "missing_token": {}
}


INVALID_FORGOT_PASSWORD_PAYLOADS = {
    "missing_email": {}
}


EXPIRED_TOKEN = "expired.jwt.token"

INVALID_TOKEN = "invalid.jwt.token"