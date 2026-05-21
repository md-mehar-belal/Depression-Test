from unittest.mock import patch

from app.services.google_auth_service import (
    generate_google_auth_url,
    verify_google_token,
    process_google_login
)


# =========================================================
# AUTH URL TESTS
# =========================================================

def test_generate_google_auth_url():

    url = generate_google_auth_url()

    assert isinstance(url, str)

    assert "google.com" in url


# =========================================================
# VERIFY TOKEN TESTS
# =========================================================

@patch("app.services.google_auth_service.get_google_user_info")
@patch("app.services.google_auth_service.exchange_auth_code")
def test_verify_google_token_success(
    mock_exchange_auth_code,
    mock_get_google_user_info
):

    mock_exchange_auth_code.return_value = (
        "access-token"
    )

    mock_get_google_user_info.return_value = {
        "email": "kushal@test.com",
        "name": "Kushal"
    }

    result = verify_google_token(
        "auth-code"
    )

    assert result is not None

    assert result["email"] == (
        "kushal@test.com"
    )


def test_verify_google_token_missing_auth_code():

    result = verify_google_token("")

    assert result is None


@patch("app.services.google_auth_service.exchange_auth_code")
def test_verify_google_token_exchange_failure(
    mock_exchange_auth_code
):

    mock_exchange_auth_code.return_value = None

    result = verify_google_token(
        "auth-code"
    )

    assert result is None


@patch("app.services.google_auth_service.exchange_auth_code")
def test_verify_google_token_exception(
    mock_exchange_auth_code
):

    mock_exchange_auth_code.side_effect = (
        Exception("OAuth failure")
    )

    result = verify_google_token(
        "auth-code"
    )

    assert result is None


# =========================================================
# PROCESS LOGIN TESTS
# =========================================================

def test_process_google_login_missing_auth_code():

    result = process_google_login("")

    assert result["success"] is False


@patch("app.services.google_auth_service.verify_google_token")
def test_process_google_login_failed_auth(
    mock_verify_google_token
):

    mock_verify_google_token.return_value = None

    result = process_google_login(
        "bad-auth-code"
    )

    assert result["success"] is False


@patch("app.services.google_auth_service.verify_google_token")
def test_process_google_login_invalid_google_data(
    mock_verify_google_token
):

    mock_verify_google_token.return_value = {
        "name": "Kushal"
    }

    result = process_google_login(
        "auth-code"
    )

    assert result["success"] is False


@patch("app.services.google_auth_service.create_access_token")
@patch("app.services.google_auth_service.find_user_by_email")
@patch("app.services.google_auth_service.verify_google_token")
def test_process_google_login_existing_user(
    mock_verify_google_token,
    mock_find_user_by_email,
    mock_create_access_token
):

    mock_verify_google_token.return_value = {
        "email": "kushal@test.com",
        "name": "Kushal"
    }

    mock_find_user_by_email.return_value = {
        "id": "123",
        "name": "Kushal",
        "email": "kushal@test.com"
    }

    mock_create_access_token.return_value = (
        "jwt-token"
    )

    result = process_google_login(
        "auth-code"
    )

    assert result["success"] is True

    assert result["token"] == "jwt-token"


@patch("app.services.google_auth_service.create_access_token")
@patch("app.services.google_auth_service.create_user")
@patch("app.services.google_auth_service.find_user_by_email")
@patch("app.services.google_auth_service.verify_google_token")
def test_process_google_login_new_user(
    mock_verify_google_token,
    mock_find_user_by_email,
    mock_create_user,
    mock_create_access_token
):

    mock_verify_google_token.return_value = {
        "email": "new@test.com",
        "name": "New User"
    }

    mock_find_user_by_email.return_value = None

    mock_create_user.return_value = {
        "id": "999",
        "name": "New User",
        "email": "new@test.com"
    }

    mock_create_access_token.return_value = (
        "jwt-token"
    )

    result = process_google_login(
        "auth-code"
    )

    assert result["success"] is True

    mock_create_user.assert_called_once()