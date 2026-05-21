# backend/tests/middleware/test_logging_middleware.py

from unittest.mock import MagicMock

from flask import Flask, jsonify

from app.middleware.logging_middleware import (
    log_request_middleware,
    log_response_middleware
)


def create_test_app():

    app = Flask(__name__)

    @app.route("/health")
    def health_check():
        return jsonify({
            "status": "ok"
        }), 200

    return app


def test_log_request_called(monkeypatch):

    app = create_test_app()

    mock_logger = MagicMock()

    monkeypatch.setattr(
        "app.middleware.logging_middleware.log_request",
        mock_logger
    )

    with app.test_request_context(
        "/health",
        method="GET"
    ):

        log_request_middleware()

        mock_logger.assert_called_once()


def test_log_response_called(monkeypatch):

    app = create_test_app()

    mock_logger = MagicMock()

    monkeypatch.setattr(
        "app.middleware.logging_middleware.log_response",
        mock_logger
    )

    with app.test_request_context(
        "/health",
        method="GET"
    ):

        response = jsonify({
            "status": "ok"
        })

        log_response_middleware(response)

        mock_logger.assert_called_once()


def test_log_response_returns_response(monkeypatch):

    app = create_test_app()

    mock_logger = MagicMock()

    monkeypatch.setattr(
        "app.middleware.logging_middleware.log_response",
        mock_logger
    )

    with app.test_request_context(
        "/health"
    ):

        response = jsonify({
            "message": "success"
        })

        returned_response = (
            log_response_middleware(response)
        )

        assert returned_response == response


def test_request_logging_does_not_crash(monkeypatch):

    app = create_test_app()

    mock_logger = MagicMock(
        side_effect=Exception(
            "Logging failure"
        )
    )

    monkeypatch.setattr(
        "app.middleware.logging_middleware.log_request",
        mock_logger
    )

    with app.test_request_context(
        "/health"
    ):

        try:
            log_request_middleware()
        except Exception:
            assert False, (
                "Logging middleware should not crash requests"
            )


def test_response_logging_does_not_crash(monkeypatch):

    app = create_test_app()

    mock_logger = MagicMock(
        side_effect=Exception(
            "Response logging failure"
        )
    )

    monkeypatch.setattr(
        "app.middleware.logging_middleware.log_response",
        mock_logger
    )

    with app.test_request_context(
        "/health"
    ):

        response = jsonify({
            "status": "ok"
        })

        try:
            returned_response = (
                log_response_middleware(response)
            )

            assert returned_response == response

        except Exception:
            assert False, (
                "Response logging should not break response flow"
            )


def test_request_logging_with_headers(monkeypatch):

    app = create_test_app()

    mock_logger = MagicMock()

    monkeypatch.setattr(
        "app.middleware.logging_middleware.log_request",
        mock_logger
    )

    with app.test_request_context(
        "/health",
        headers={
            "User-Agent": "pytest"
        }
    ):

        log_request_middleware()

        mock_logger.assert_called_once()


def test_response_logging_status_code(monkeypatch):

    app = create_test_app()

    mock_logger = MagicMock()

    monkeypatch.setattr(
        "app.middleware.logging_middleware.log_response",
        mock_logger
    )

    with app.test_request_context(
        "/health"
    ):

        response = jsonify({
            "status": "created"
        })

        response.status_code = 201

        log_response_middleware(response)

        mock_logger.assert_called_once()
        