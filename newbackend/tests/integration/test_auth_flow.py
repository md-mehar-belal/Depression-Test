import pytest

from app import app


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_complete_auth_flow(client):

    signup_payload = {
        "name": "Kushal",
        "email": "kushal@example.com",
        "password": "StrongPassword123"
    }

    signup_response = client.post(
        "/auth/signup",
        json=signup_payload
    )

    assert signup_response.status_code == 201

    signup_data = signup_response.get_json()

    assert "token" in signup_data

    assert signup_data["user"]["email"] == (
        "kushal@example.com"
    )

    # Login with same credentials
    login_payload = {
        "email": "kushal@example.com",
        "password": "StrongPassword123"
    }

    login_response = client.post(
        "/auth/login",
        json=login_payload
    )

    assert login_response.status_code == 200

    login_data = login_response.get_json()

    assert "token" in login_data

    token = login_data["token"]

    # Access protected route
    me_response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert me_response.status_code == 200

    me_data = me_response.get_json()

    assert me_data["user"]["email"] == (
        "kushal@example.com"
    )


def test_duplicate_signup_rejected(client):

    payload = {
        "name": "Duplicate User",
        "email": "duplicate@example.com",
        "password": "Password123"
    }

    first_response = client.post(
        "/auth/signup",
        json=payload
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/auth/signup",
        json=payload
    )

    assert second_response.status_code == 409

    response_data = second_response.get_json()

    assert (
        response_data["error"]
        == "User already exists"
    )


def test_login_with_invalid_password(client):

    signup_payload = {
        "name": "Test User",
        "email": "wrongpass@example.com",
        "password": "CorrectPassword123"
    }

    client.post(
        "/auth/signup",
        json=signup_payload
    )

    login_payload = {
        "email": "wrongpass@example.com",
        "password": "WrongPassword"
    }

    response = client.post(
        "/auth/login",
        json=login_payload
    )

    assert response.status_code == 401

    response_data = response.get_json()

    assert (
        response_data["error"]
        == "Invalid credentials"
    )


def test_access_protected_route_without_token(client):

    response = client.get(
        "/auth/me"
    )

    assert response.status_code == 401

    response_data = response.get_json()

    assert (
        response_data["error"]
        == "Authorization token missing"
    )


def test_forgot_password_flow(client):

    payload = {
        "email": "forgot@example.com"
    }

    response = client.post(
        "/auth/forgot-password",
        json=payload
    )

    assert response.status_code == 200

    response_data = response.get_json()

    assert "Password reset link sent" in (
        response_data["message"]
    )