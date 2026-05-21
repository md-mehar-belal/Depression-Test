from unittest.mock import patch

from app.services.logging_service import (
    log_request,
    log_error,
    log_auth_event,
    log_prediction
)


# =========================================================
# REQUEST LOG TESTS
# =========================================================

@patch("app.services.logging_service.request_logger")
def test_log_request_success(
    mock_request_logger
):

    log_request(
        method="POST",
        endpoint="/predict",
        ip_address="127.0.0.1",
        status_code=200
    )

    mock_request_logger.info.assert_called_once()


@patch("app.services.logging_service.request_logger")
def test_log_request_logger_failure(
    mock_request_logger
):

    mock_request_logger.info.side_effect = (
        Exception("Logging failed")
    )

    log_request(
        method="GET",
        endpoint="/health",
        ip_address="127.0.0.1",
        status_code=200
    )


# =========================================================
# ERROR LOG TESTS
# =========================================================

@patch("app.services.logging_service.error_logger")
def test_log_error_success(
    mock_error_logger
):

    log_error(
        error=ValueError("Invalid value"),
        context={
            "endpoint": "/predict"
        }
    )

    mock_error_logger.error.assert_called_once()


@patch("app.services.logging_service.error_logger")
def test_log_error_logger_failure(
    mock_error_logger
):

    mock_error_logger.error.side_effect = (
        Exception("Logger failed")
    )

    log_error(
        error=RuntimeError("Failure")
    )


# =========================================================
# AUTH LOG TESTS
# =========================================================

@patch("app.services.logging_service.auth_logger")
def test_log_auth_event_success(
    mock_auth_logger
):

    log_auth_event(
        event="login_success",
        details={
            "email": "kushal@test.com"
        }
    )

    mock_auth_logger.info.assert_called_once()


@patch("app.services.logging_service.auth_logger")
def test_log_auth_event_logger_failure(
    mock_auth_logger
):

    mock_auth_logger.info.side_effect = (
        Exception("Logger failed")
    )

    log_auth_event(
        event="login_failure",
        details={}
    )


# =========================================================
# PREDICTION LOG TESTS
# =========================================================

@patch("app.services.logging_service.request_logger")
def test_log_prediction_success(
    mock_request_logger
):

    log_prediction(
        user_id="123",
        prediction_data={
            "prediction": 1,
            "severity": "moderate"
        }
    )

    mock_request_logger.info.assert_called_once()


@patch("app.services.logging_service.request_logger")
def test_log_prediction_logger_failure(
    mock_request_logger
):

    mock_request_logger.info.side_effect = (
        Exception("Logger failed")
    )

    log_prediction(
        user_id="123",
        prediction_data={}
    )