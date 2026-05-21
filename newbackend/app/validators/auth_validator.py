# app/validators/auth_validator.py

import re
from typing import Any


EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

PASSWORD_MIN_LENGTH = 8


def _build_validation_response(
    errors: list[str]
) -> dict:

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "message": (
            "Validation successful"
            if not errors
            else "Validation failed"
        )
    }


def validate_signup_data(
    data: dict[str, Any]
) -> dict:

    errors = []

    if not isinstance(data, dict):

        return _build_validation_response(
            ["Invalid request payload"]
        )

    required_fields = [
        "name",
        "email",
        "password"
    ]

    for field in required_fields:

        value = data.get(field)

        if (
            value is None or
            (
                isinstance(value, str)
                and not value.strip()
            )
        ):
            errors.append(f"{field} is required")

    email = (
        data.get("email", "")
        .strip()
        .lower()
    )

    if email and not validate_email(email):
        errors.append("Invalid email format")

    password = data.get("password", "")

    password_validation = validate_password(password)

    errors.extend(
        password_validation["errors"]
    )

    return _build_validation_response(errors)


def validate_login_data(
    data: dict[str, Any]
) -> dict:

    errors = []

    if not isinstance(data, dict):

        return _build_validation_response(
            ["Invalid request payload"]
        )

    email = (
        data.get("email", "")
        .strip()
        .lower()
    )

    password = data.get("password", "")

    if not email:
        errors.append("email is required")

    elif not validate_email(email):
        errors.append("Invalid email format")

    if not password:
        errors.append("password is required")

    return _build_validation_response(errors)


def validate_email(
    email: str
) -> bool:

    if not isinstance(email, str):
        return False

    return bool(
        re.match(
            EMAIL_REGEX,
            email.strip().lower()
        )
    )


def validate_password(
    password: str
) -> dict:

    errors = []

    if not isinstance(password, str):

        return _build_validation_response(
            ["Password must be a string"]
        )

    if len(password) < PASSWORD_MIN_LENGTH:
        errors.append(
            f"Password must be at least "
            f"{PASSWORD_MIN_LENGTH} characters long"
        )

    if not re.search(r"[A-Z]", password):
        errors.append(
            "Password must contain at least one uppercase letter"
        )

    if not re.search(r"[a-z]", password):
        errors.append(
            "Password must contain at least one lowercase letter"
        )

    if not re.search(r"\d", password):
        errors.append(
            "Password must contain at least one number"
        )

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append(
            "Password must contain at least one special character"
        )

    return _build_validation_response(errors)