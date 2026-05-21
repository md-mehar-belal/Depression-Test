# backend/tests/middleware/test_rate_limit_middleware.py

from unittest.mock import MagicMock

from flask import Flask, jsonify

from app.middleware.rate_limit_middleware import (
    rate_limit_middleware
)


def create_test_app():

    app = Flask(__name__)

    @app.route("/predict")
    def predict():
        return jsonify({
            "message": "allowed"
        }), 200

    return app


def test_request_allowed(monkeypatch):

    app = create_test_app()

    mock_check = MagicMock(
        return_value=True
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.check_rate_limit",
        mock_check
    )

    with app.test_request_context(
        "/predict"
    ):

        response = rate_limit_middleware()

        assert response is None

        mock_check.assert_called_once()


def test_request_blocked(monkeypatch):

    app = create_test_app()

    mock_check = MagicMock(
        return_value=False
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.check_rate_limit",
        mock_check
    )

    with app.test_request_context(
        "/predict"
    ):

        response = rate_limit_middleware()

        body, status_code = response

        assert status_code == 429

        json_body = body.get_json()

        assert json_body["success"] is False

        assert "Rate limit exceeded" in (
            json_body["error"]
        )


def test_rate_limit_uses_client_ip(monkeypatch):

    app = create_test_app()

    mock_check = MagicMock(
        return_value=True
    )

    mock_get_ip = MagicMock(
        return_value="127.0.0.1"
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.check_rate_limit",
        mock_check
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.get_client_ip",
        mock_get_ip
    )

    with app.test_request_context(
        "/predict"
    ):

        rate_limit_middleware()

        mock_get_ip.assert_called_once()

        mock_check.assert_called_once_with(
            "127.0.0.1"
        )


def test_rate_limit_response_is_json(monkeypatch):

    app = create_test_app()

    mock_check = MagicMock(
        return_value=False
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.check_rate_limit",
        mock_check
    )

    with app.test_request_context(
        "/predict"
    ):

        response = rate_limit_middleware()

        body, _ = response

        assert body.content_type == (
            "application/json"
        )


def test_rate_limit_allows_multiple_valid_requests(monkeypatch):

    app = create_test_app()

    mock_check = MagicMock(
        side_effect=[True, True, True]
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.check_rate_limit",
        mock_check
    )

    with app.test_request_context(
        "/predict"
    ):

        response_1 = rate_limit_middleware()
        response_2 = rate_limit_middleware()
        response_3 = rate_limit_middleware()

        assert response_1 is None
        assert response_2 is None
        assert response_3 is None

        assert mock_check.call_count == 3


def test_rate_limit_handles_missing_ip(monkeypatch):

    app = create_test_app()

    mock_get_ip = MagicMock(
        return_value=None
    )

    mock_check = MagicMock(
        return_value=False
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.get_client_ip",
        mock_get_ip
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.check_rate_limit",
        mock_check
    )

    with app.test_request_context(
        "/predict"
    ):

        response = rate_limit_middleware()

        body, status_code = response

        assert status_code == 429

        assert body.get_json()["success"] is False


def test_rate_limit_middleware_does_not_modify_successful_requests(
    monkeypatch
):

    app = create_test_app()

    mock_check = MagicMock(
        return_value=True
    )

    monkeypatch.setattr(
        "app.middleware.rate_limit_middleware.check_rate_limit",
        mock_check
    )

    with app.test_request_context(
        "/predict"
    ):

        response = rate_limit_middleware()

        assert response is None