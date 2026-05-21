# app/services/auth_service.py

from app.repositories.user_repository import (
    create_user,
    find_user_by_email,
    find_user_by_id,
    verify_user_email,
    update_user
)

from app.services.jwt_service import (
    create_access_token,
    verify_token
)

from app.services.email_service import (
    send_verification_email,
    send_reset_password_email
)

from app.utils.security import (
    hash_password,
    verify_password
)

from app.validators.auth_validator import (
    validate_signup_data,
    validate_login_data,
    validate_password
)


def signup_user(data: dict) -> dict:

    data = data or {}

    validation = validate_signup_data(data)

    if not validation["valid"]:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": validation["errors"]
        }

    existing_user = find_user_by_email(
        data["email"]
    )

    if existing_user:
        return {
            "success": False,
            "message": "User already exists"
        }

    hashed_password = hash_password(
        data["password"]
    )

    new_user = create_user({
        "name": data["name"],
        "email": data["email"],
        "password": hashed_password,
        "is_verified": False
    })

    if not new_user:
        return {
            "success": False,
            "message": "Failed to create user"
        }

    verification_token = create_access_token({
        "user_id": new_user["id"],
        "email": new_user["email"],
        "purpose": "email_verification"
    })

    send_verification_email(
        email=new_user["email"],
        verification_token=verification_token
    )

    token = create_access_token({
        "user_id": new_user["id"],
        "email": new_user["email"],
        "purpose": "access"
    })

    return {
        "success": True,
        "message": "Signup successful",
        "token": token,
        "user": new_user
    }


def login_user(data: dict) -> dict:

    data = data or {}

    validation = validate_login_data(data)

    if not validation["valid"]:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": validation["errors"]
        }

    user = find_user_by_email(
        data["email"]
    )

    if not user:
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    if not verify_password(
        data["password"],
        user["password"]
    ):
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    if not user.get("is_verified", False):
        return {
            "success": False,
            "message": "Email not verified"
        }

    token = create_access_token({
        "user_id": user["id"],
        "email": user["email"],
        "purpose": "access"
    })

    return {
        "success": True,
        "message": "Login successful",
        "token": token,
        "user": user
    }


def get_current_user(token: str) -> dict:

    if not token:
        return {
            "success": False,
            "message": "Token is required"
        }

    if token.startswith("Bearer "):
        token = token.replace(
            "Bearer ",
            ""
        ).strip()

    payload = verify_token(token)

    if not payload:
        return {
            "success": False,
            "message": "Invalid token"
        }

    if payload.get("purpose") != "access":
        return {
            "success": False,
            "message": "Invalid token purpose"
        }

    user = find_user_by_id(
        payload.get("user_id")
    )

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    return {
        "success": True,
        "user": user
    }


def logout_user() -> dict:

    # Stateless JWT logout.
    # Real logout requires:
    # - token blacklist
    # - refresh token revocation
    # - session storage

    return {
        "success": True,
        "message": "Logout successful"
    }


def forgot_password(data: dict) -> dict:

    data = data or {}

    email = data.get("email")

    if not email:
        return {
            "success": False,
            "message": "Email is required"
        }

    user = find_user_by_email(email)

    # Prevent user enumeration
    if not user:
        return {
            "success": True,
            "message": "If the account exists, a reset email has been sent"
        }

    reset_token = create_access_token({
        "user_id": user["id"],
        "email": user["email"],
        "purpose": "password_reset"
    })

    send_reset_password_email(
        email=user["email"],
        reset_token=reset_token
    )

    return {
        "success": True,
        "message": "If the account exists, a reset email has been sent"
    }


def reset_password(
    token: str,
    new_password: str
) -> dict:

    if not token or not new_password:
        return {
            "success": False,
            "message": "Token and new password are required"
        }

    password_validation = validate_password(
        new_password
    )

    if not password_validation["valid"]:
        return {
            "success": False,
            "message": "Invalid password",
            "errors": password_validation["errors"]
        }

    payload = verify_token(token)

    if not payload:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    if payload.get("purpose") != "password_reset":
        return {
            "success": False,
            "message": "Invalid token purpose"
        }

    hashed_password = hash_password(
        new_password
    )

    updated = update_user(
        user_id=payload["user_id"],
        update_data={
            "password": hashed_password
        }
    )

    if not updated:
        return {
            "success": False,
            "message": "Password update failed"
        }

    return {
        "success": True,
        "message": "Password reset successful"
    }


def verify_email(token: str) -> dict:

    if not token:
        return {
            "success": False,
            "message": "Verification token is required"
        }

    payload = verify_token(token)

    if not payload:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    if payload.get("purpose") != "email_verification":
        return {
            "success": False,
            "message": "Invalid token purpose"
        }

    verified = verify_user_email(
        payload["user_id"]
    )

    if not verified:
        return {
            "success": False,
            "message": "Failed to verify email"
        }

    return {
        "success": True,
        "message": "Email verified successfully"
    }


def authenticate_access_token(token: str) -> dict:
    """
    Validate access token and resolve current user.
    """

    if not token:
        return {
            "success": False,
            "message": "Authentication token missing",
            "status_code": 401
        }

    payload = verify_token(token)

    if not payload:
        return {
            "success": False,
            "message": "Invalid or expired token",
            "status_code": 401
        }

    if payload.get("purpose") != "access":
        return {
            "success": False,
            "message": "Invalid token purpose",
            "status_code": 401
        }

    user = find_user_by_id(
        payload.get("user_id")
    )

    if not user:
        return {
            "success": False,
            "message": "User not found",
            "status_code": 404
        }

    return {
        "success": True,
        "user": user,
        "status_code": 200
    }