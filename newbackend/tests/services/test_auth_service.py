import pytest
from unittest.mock import patch

from app.services.auth_service import (
    signup_user,
    login_user,
    get_current_user,
    logout_user,
    forgot_password,
    reset_password,
    verify_email
)


# =========================================================
# SIGNUP TESTS
# =========================================================

@patch("app.services.auth_service.create_access_token")
@patch("app.services.auth_service.send_verification_email")
@patch("app.services.auth_service.generate_secure_token")
@patch("app.services.auth_service.hash_password")
@patch("app.services.auth_service.create_user")
@patch("app.services.auth_service.find_user_by_email")
@patch("app.services.auth_service.validate_signup_data")
def test_signup_success(
    mock_validate,
    mock_find_user,
    mock_create_user,
    mock_hash_password,
    mock_generate_token,
    mock_send_email,
    mock_create_access_token
):

    mock_validate.return_value = {
        "valid": True
    }

    mock_find_user.return_value = None

    mock_hash_password.return_value = "hashed-password"

    mock_generate_token.return_value = "verification-token"

    mock_create_user.return_value = {
        "id": "123",
        "name": "Kushal",
        "email": "kushal@test.com"
    }

    mock_create_access_token.return_value = "jwt-token"

    payload = {
        "name": "Kushal",
        "email": "kushal@test.com",
        "password": "secure123"
    }

    result = signup_user(payload)

    assert result["success"] is True
    assert result["token"] == "jwt-token"
    assert result["user"]["email"] == "kushal@test.com"

    mock_send_email.assert_called_once()


@patch("app.services.auth_service.validate_signup_data")
def test_signup_validation_failure(mock_validate):

    mock_validate.return_value = {
        "valid": False,
        "message": "Invalid input"
    }

    result = signup_user({})

    assert result["valid"] is False


@patch("app.services.auth_service.find_user_by_email")
@patch("app.services.auth_service.validate_signup_data")
def test_signup_existing_user(
    mock_validate,
    mock_find_user
):

    mock_validate.return_value = {
        "valid": True
    }

    mock_find_user.return_value = {
        "email": "existing@test.com"
    }

    payload = {
        "name": "Kushal",
        "email": "existing@test.com",
        "password": "secure123"
    }

    result = signup_user(payload)

    assert result["success"] is False
    assert result["message"] == "User already exists"


# =========================================================
# LOGIN TESTS
# =========================================================

@patch("app.services.auth_service.create_access_token")
@patch("app.services.auth_service.verify_password")
@patch("app.services.auth_service.find_user_by_email")
@patch("app.services.auth_service.validate_login_data")
def test_login_success(
    mock_validate,
    mock_find_user,
    mock_verify_password,
    mock_create_access_token
):

    mock_validate.return_value = {
        "valid": True
    }

    mock_find_user.return_value = {
        "id": "123",
        "name": "Kushal",
        "email": "kushal@test.com",
        "password": "hashed-password"
    }

    mock_verify_password.return_value = True

    mock_create_access_token.return_value = "jwt-token"

    payload = {
        "email": "kushal@test.com",
        "password": "secure123"
    }

    result = login_user(payload)

    assert result["success"] is True
    assert result["token"] == "jwt-token"


@patch("app.services.auth_service.validate_login_data")
def test_login_validation_failure(mock_validate):

    mock_validate.return_value = {
        "valid": False,
        "message": "Invalid login"
    }

    result = login_user({})

    assert result["valid"] is False


@patch("app.services.auth_service.find_user_by_email")
@patch("app.services.auth_service.validate_login_data")
def test_login_user_not_found(
    mock_validate,
    mock_find_user
):

    mock_validate.return_value = {
        "valid": True
    }

    mock_find_user.return_value = None

    payload = {
        "email": "wrong@test.com",
        "password": "wrongpass"
    }

    result = login_user(payload)

    assert result["success"] is False
    assert result["message"] == "Invalid credentials"


@patch("app.services.auth_service.verify_password")
@patch("app.services.auth_service.find_user_by_email")
@patch("app.services.auth_service.validate_login_data")
def test_login_wrong_password(
    mock_validate,
    mock_find_user,
    mock_verify_password
):

    mock_validate.return_value = {
        "valid": True
    }

    mock_find_user.return_value = {
        "id": "123",
        "email": "test@test.com",
        "password": "hashed-password"
    }

    mock_verify_password.return_value = False

    payload = {
        "email": "test@test.com",
        "password": "wrong-password"
    }

    result = login_user(payload)

    assert result["success"] is False
    assert result["message"] == "Invalid credentials"


# =========================================================
# CURRENT USER TESTS
# =========================================================

@patch("app.services.auth_service.find_user_by_email")
@patch("app.services.auth_service.verify_token")
def test_get_current_user_success(
    mock_verify_token,
    mock_find_user
):

    mock_verify_token.return_value = {
        "email": "kushal@test.com"
    }

    mock_find_user.return_value = {
        "id": "123",
        "email": "kushal@test.com"
    }

    result = get_current_user("jwt-token")

    assert result["success"] is True


@patch("app.services.auth_service.verify_token")
def test_get_current_user_invalid_token(
    mock_verify_token
):

    mock_verify_token.return_value = None

    result = get_current_user("invalid-token")

    assert result["success"] is False


# =========================================================
# LOGOUT TESTS
# =========================================================

def test_logout_user():

    result = logout_user()

    assert result["success"] is True


# =========================================================
# FORGOT PASSWORD TESTS
# =========================================================

@patch("app.services.auth_service.send_reset_password_email")
@patch("app.services.auth_service.generate_secure_token")
@patch("app.services.auth_service.find_user_by_email")
def test_forgot_password_success(
    mock_find_user,
    mock_generate_token,
    mock_send_email
):

    mock_find_user.return_value = {
        "id": "123",
        "email": "kushal@test.com"
    }

    mock_generate_token.return_value = "reset-token"

    payload = {
        "email": "kushal@test.com"
    }

    result = forgot_password(payload)

    assert result["success"] is True

    mock_send_email.assert_called_once()


@patch("app.services.auth_service.find_user_by_email")
def test_forgot_password_user_not_found(
    mock_find_user
):

    mock_find_user.return_value = None

    payload = {
        "email": "missing@test.com"
    }

    result = forgot_password(payload)

    assert result["success"] is False


# =========================================================
# RESET PASSWORD TESTS
# =========================================================

@patch("app.services.auth_service.update_user")
@patch("app.services.auth_service.hash_password")
@patch("app.services.auth_service.verify_token")
def test_reset_password_success(
    mock_verify_token,
    mock_hash_password,
    mock_update_user
):

    mock_verify_token.return_value = {
        "user_id": "123"
    }

    mock_hash_password.return_value = "hashed-password"

    result = reset_password(
        token="reset-token",
        new_password="new-password"
    )

    assert result["success"] is True

    mock_update_user.assert_called_once()


@patch("app.services.auth_service.verify_token")
def test_reset_password_invalid_token(
    mock_verify_token
):

    mock_verify_token.return_value = None

    result = reset_password(
        token="invalid-token",
        new_password="password"
    )

    assert result["success"] is False


# =========================================================
# VERIFY EMAIL TESTS
# =========================================================

@patch("app.services.auth_service.verify_user_email")
@patch("app.services.auth_service.verify_token")
def test_verify_email_success(
    mock_verify_token,
    mock_verify_user_email
):

    mock_verify_token.return_value = {
        "user_id": "123"
    }

    result = verify_email("verification-token")

    assert result["success"] is True

    mock_verify_user_email.assert_called_once()


@patch("app.services.auth_service.verify_token")
def test_verify_email_invalid_token(
    mock_verify_token
):

    mock_verify_token.return_value = None

    result = verify_email("invalid-token")

    assert result["success"] is False