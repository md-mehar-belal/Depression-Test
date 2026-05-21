# backend/tests/middleware/test_security_middleware.py

from flask import Flask, jsonify, request

from app.middleware.security_middleware import (
    apply_security_headers,
    sanitize_request
)


def create_test_app():

    app = Flask(__name__)

    @app.route("/health")
    def health():

        return jsonify({
            "status": "ok"
        }), 200

    return app


def test_apply_security_headers():

    app = create_test_app()

    with app.app_context():

        response = jsonify({
            "message": "secured"
        })

        secured_response = (
            apply_security_headers(response)
        )

        headers = secured_response.headers

        assert (
            "X-Content-Type-Options"
            in headers
        )

        assert (
            headers["X-Content-Type-Options"]
            == "nosniff"
        )

        assert (
            "X-Frame-Options"
            in headers
        )

        assert (
            "Content-Security-Policy"
            in headers
        )


def test_security_headers_return_response():

    app = create_test_app()

    with app.app_context():

        response = jsonify({
            "message": "ok"
        })

        secured_response = (
            apply_security_headers(response)
        )

        assert secured_response == response


def test_sanitize_request_safe_payload():

    app = create_test_app()

    with app.test_request_context(
        "/health",
        method="POST",
        json={
            "name": "Kushal",
            "message": "Hello world"
        }
    ):

        sanitized = sanitize_request()

        assert sanitized is None


def test_sanitize_request_script_injection():

    app = create_test_app()

    malicious_payload = {
        "message": "<script>alert('xss')</script>"
    }

    with app.test_request_context(
        "/health",
        method="POST",
        json=malicious_payload
    ):

        response = sanitize_request()

        body, status_code = response

        assert status_code == 400

        json_body = body.get_json()

        assert json_body["success"] is False

        assert "malicious" in (
            json_body["error"].lower()
        )


def test_sanitize_request_sql_injection():

    app = create_test_app()

    malicious_payload = {
        "query": "' OR 1=1 --"
    }

    with app.test_request_context(
        "/health",
        method="POST",
        json=malicious_payload
    ):

        response = sanitize_request()

        body, status_code = response

        assert status_code == 400

        json_body = body.get_json()

        assert json_body["success"] is False


def test_sanitize_request_handles_empty_json():

    app = create_test_app()

    with app.test_request_context(
        "/health",
        method="POST",
        json={}
    ):

        response = sanitize_request()

        assert response is None


def test_sanitize_request_handles_missing_json():

    app = create_test_app()

    with app.test_request_context(
        "/health",
        method="POST"
    ):

        response = sanitize_request()

        assert response is None


def test_security_headers_do_not_remove_existing_headers():

    app = create_test_app()

    with app.app_context():

        response = jsonify({
            "message": "ok"
        })

        response.headers[
            "Custom-Header"
        ] = "custom-value"

        secured_response = (
            apply_security_headers(response)
        )

        assert (
            secured_response.headers[
                "Custom-Header"
            ]
            == "custom-value"
        )


def test_security_headers_content_type():

    app = create_test_app()

    with app.app_context():

        response = jsonify({
            "message": "ok"
        })

        secured_response = (
            apply_security_headers(response)
        )

        assert (
            secured_response.content_type
            == "application/json"
        )


def test_sanitize_request_nested_payload():

    app = create_test_app()

    payload = {
        "profile": {
            "bio": "Normal text"
        }
    }

    with app.test_request_context(
        "/health",
        method="POST",
        json=payload
    ):

        response = sanitize_request()

        assert response is None