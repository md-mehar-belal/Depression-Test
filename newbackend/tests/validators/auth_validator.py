import re


EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def validate_signup_data(
    data: dict
) -> tuple[bool, str | None]:

    required_fields = [
        "name",
        "email",
        "password"
    ]

    for field in required_fields:

        if not data.get(field):
            return (
                False,
                f"'{field}' is required"
            )

    email_valid, email_error = validate_email(
        data["email"]
    )

    if not email_valid:
        return False, email_error

    password_valid, password_error = validate_password(
        data["password"]
    )

    if not password_valid:
        return False, password_error

    return True, None


def validate_login_data(
    data: dict
) -> tuple[bool, str | None]:

    if not data.get("email"):
        return False, "Email is required"

    if not data.get("password"):
        return False, "Password is required"

    return True, None


def validate_email(
    email: str
) -> tuple[bool, str | None]:

    if not re.match(EMAIL_REGEX, email):
        return (
            False,
            "Invalid email format"
        )

    return True, None


def validate_password(
    password: str
) -> tuple[bool, str | None]:

    if len(password) < 6:
        return (
            False,
            "Password must be at least 6 characters long"
        )

    return True, None