from unittest.mock import patch

from app.services.email_service import (
    send_email,
    send_verification_email,
    send_reset_password_email,
    build_verification_email_body,
    build_reset_password_email_body
)


# =========================================================
# GENERIC EMAIL TESTS
# =========================================================

@patch("app.services.email_service.log_auth_event")
@patch("app.services.email_service.send_email_message")
def test_send_email_success(
    mock_send_email_message,
    mock_log_auth_event
):

    mock_send_email_message.return_value = True

    result = send_email(
        to_email="kushal@test.com",
        subject="Test Subject",
        body="Test Body"
    )

    assert result is True

    mock_send_email_message.assert_called_once_with(
        recipient="kushal@test.com",
        subject="Test Subject",
        body="Test Body"
    )

    mock_log_auth_event.assert_called_once()


def test_send_email_missing_email():

    result = send_email(
        to_email="",
        subject="Test Subject",
        body="Test Body"
    )

    assert result is False


def test_send_email_missing_subject():

    result = send_email(
        to_email="kushal@test.com",
        subject="",
        body="Test Body"
    )

    assert result is False


def test_send_email_missing_body():

    result = send_email(
        to_email="kushal@test.com",
        subject="Test Subject",
        body=""
    )

    assert result is False


@patch("app.services.email_service.log_auth_event")
@patch("app.services.email_service.send_email_message")
def test_send_email_transport_failure(
    mock_send_email_message,
    mock_log_auth_event
):

    mock_send_email_message.side_effect = Exception(
        "SMTP connection failed"
    )

    result = send_email(
        to_email="kushal@test.com",
        subject="Test Subject",
        body="Test Body"
    )

    assert result is False

    mock_log_auth_event.assert_called_once()


# =========================================================
# EMAIL BODY BUILDER TESTS
# =========================================================

def test_build_verification_email_body():

    body = build_verification_email_body(
        verification_token="verify-token"
    )

    assert "verify-token" in body
    assert "verify-email" in body


def test_build_reset_password_email_body():

    body = build_reset_password_email_body(
        reset_token="reset-token"
    )

    assert "reset-token" in body
    assert "reset-password" in body


# =========================================================
# VERIFICATION EMAIL TESTS
# =========================================================

@patch("app.services.email_service.send_email")
def test_send_verification_email_success(
    mock_send_email
):

    mock_send_email.return_value = True

    result = send_verification_email(
        email="kushal@test.com",
        verification_token="verify-token"
    )

    assert result is True

    mock_send_email.assert_called_once()


def test_send_verification_email_missing_email():

    result = send_verification_email(
        email="",
        verification_token="verify-token"
    )

    assert result is False


def test_send_verification_email_missing_token():

    result = send_verification_email(
        email="kushal@test.com",
        verification_token=""
    )

    assert result is False


# =========================================================
# RESET PASSWORD EMAIL TESTS
# =========================================================

@patch("app.services.email_service.send_email")
def test_send_reset_password_email_success(
    mock_send_email
):

    mock_send_email.return_value = True

    result = send_reset_password_email(
        email="kushal@test.com",
        reset_token="reset-token"
    )

    assert result is True

    mock_send_email.assert_called_once()


def test_send_reset_password_email_missing_email():

    result = send_reset_password_email(
        email="",
        reset_token="reset-token"
    )

    assert result is False


def test_send_reset_password_email_missing_token():

    result = send_reset_password_email(
        email="kushal@test.com",
        reset_token=""
    )

    assert result is False