# backend/tests/middleware/test_auth_middleware.py

from unittest.mock import MagicMock

from flask import Flask, g

from app.middleware.auth_middleware import (
    authenticate_request
)


def create_test_app():

    app = Flask(__name__)

    @app.route("/protected")
    def protected_route():
        return {
            "message": "authorized",
            "user": g.current_user
        }, 200

    return app


def test_missing_authorization_header(monkeypatch):

    app = create_test_app()

    with app.test_request_context(
        "/protected",
        headers={}
    ):

        response = authenticate_request()

        body, status_code = response

        assert status_code == 401
        assert "error" in body.json


def test_invalid_authorization_format(monkeypatch):

    app = create_test_app()

    with app.test_request_context(
        "/protected",
        headers={
            "Authorization": "InvalidToken"
        }
    ):

        response = authenticate_request()

        body, status_code = response

        assert status_code == 401
        assert "error" in body.json


def test_invalid_token(monkeypatch):

    app = create_test_app()

    mock_verify = MagicMock(
        return_value=None
    )

    monkeypatch.setattr(
        "app.middleware.auth_middleware.verify_token",
        mock_verify
    )

    with app.test_request_context(
        "/protected",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    ):

        response = authenticate_request()

        body, status_code = response

        assert status_code == 401
        assert "error" in body.json


def test_valid_token(monkeypatch):

    app = create_test_app()

    mock_user = {
        "id": "user123",
        "email": "kushal@test.com"
    }

    mock_verify = MagicMock(
        return_value=mock_user
    )

    monkeypatch.setattr(
        "app.middleware.auth_middleware.verify_token",
        mock_verify
    )

    with app.test_request_context(
        "/protected",
        headers={
            "Authorization": "Bearer valid-token"
        }
    ):

        response = authenticate_request()

        assert response is None

        assert g.current_user == mock_user


def test_authenticated_user_attached(monkeypatch):

    app = create_test_app()

    mock_user = {
        "id": "abc123",
        "email": "user@test.com"
    }

    mock_verify = MagicMock(
        return_value=mock_user
    )

    monkeypatch.setattr(
        "app.middleware.auth_middleware.verify_token",
        mock_verify
    )

    with app.test_request_context(
        "/protected",
        headers={
            "Authorization": "Bearer valid-token"
        }
    ):

        authenticate_request()

        assert hasattr(g, "current_user")

        assert g.current_user["id"] == "abc123"
        assert g.current_user["email"] == "user@test.com"


def test_empty_bearer_token(monkeypatch):

    app = create_test_app()

    with app.test_request_context(
        "/protected",
        headers={
            "Authorization": "Bearer "
        }
    ):

        response = authenticate_request()

        body, status_code = response

        assert status_code == 401
        assert "error" in body.json