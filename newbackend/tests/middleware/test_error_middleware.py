# backend/tests/middleware/test_error_middleware.py

from flask import Flask

from app.middleware.error_middleware import (
    handle_validation_error,
    handle_auth_error,
    handle_server_error
)


class MockValidationError(Exception):
    pass


class MockAuthError(Exception):
    pass


def create_test_app():

    app = Flask(__name__)

    return app


def test_handle_validation_error():

    app = create_test_app()

    with app.app_context():

        error = MockValidationError(
            "Invalid input data"
        )

        response, status_code = (
            handle_validation_error(error)
        )

        body = response.get_json()

        assert status_code == 400

        assert body["success"] is False

        assert body["error"] == (
            "Invalid input data"
        )


def test_handle_auth_error():

    app = create_test_app()

    with app.app_context():

        error = MockAuthError(
            "Unauthorized access"
        )

        response, status_code = (
            handle_auth_error(error)
        )

        body = response.get_json()

        assert status_code == 401

        assert body["success"] is False

        assert body["error"] == (
            "Unauthorized access"
        )


def test_handle_server_error():

    app = create_test_app()

    with app.app_context():

        error = Exception(
            "Internal server issue"
        )

        response, status_code = (
            handle_server_error(error)
        )

        body = response.get_json()

        assert status_code == 500

        assert body["success"] is False

        assert body["error"] == (
            "Internal server error"
        )


def test_validation_error_response_type():

    app = create_test_app()

    with app.app_context():

        error = MockValidationError(
            "Validation failed"
        )

        response, _ = (
            handle_validation_error(error)
        )

        assert response.content_type == (
            "application/json"
        )


def test_auth_error_response_type():

    app = create_test_app()

    with app.app_context():

        error = MockAuthError(
            "Token invalid"
        )

        response, _ = (
            handle_auth_error(error)
        )

        assert response.content_type == (
            "application/json"
        )


def test_server_error_hides_internal_details():

    app = create_test_app()

    with app.app_context():

        error = Exception(
            "Sensitive DB failure details"
        )

        response, status_code = (
            handle_server_error(error)
        )

        body = response.get_json()

        assert status_code == 500

        assert (
            body["error"]
            != "Sensitive DB failure details"
        )

        assert body["error"] == (
            "Internal server error"
        )


def test_server_error_response_type():

    app = create_test_app()

    with app.app_context():

        error = Exception(
            "Unexpected issue"
        )

        response, _ = (
            handle_server_error(error)
        )

        assert response.content_type == (
            "application/json"
        )