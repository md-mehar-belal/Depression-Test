import jwt
from datetime import datetime, timedelta, UTC

from app.services.jwt_service import create_access_token
from app.utils.constants import JWT_ALGORITHM


def test_get_current_user_success(
    client,
    test_user,
    monkeypatch
):
    """
    Test authenticated user retrieval.
    """

    token = create_access_token({
        "user_id": str(test_user["_id"]),
        "email": test_user["email"]
    })

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "user" in data
    assert data["user"]["email"] == test_user["email"]


def test_get_current_user_missing_token(
    client
):
    """
    Test request without authorization token.
    """

    response = client.get(
        "/auth/me"
    )

    assert response.status_code == 401

    data = response.get_json()

    assert "error" in data


def test_get_current_user_invalid_token(
    client
):
    """
    Test invalid JWT token handling.
    """

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code == 401

    data = response.get_json()

    assert "error" in data


def test_get_current_user_expired_token(
    client,
    app
):
    """
    Test expired JWT token handling.
    """

    expired_payload = {
        "user_id": "123",
        "email": "expired@example.com",
        "exp": datetime.now(UTC) - timedelta(hours=1)
    }

    expired_token = jwt.encode(
        expired_payload,
        app.config["JWT_SECRET"],
        algorithm=JWT_ALGORITHM
    )

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {expired_token}"
        }
    )

    assert response.status_code == 401

    data = response.get_json()

    assert "error" in data


def test_get_current_user_user_not_found(
    client
):
    """
    Test valid token but deleted/nonexistent user.
    """

    token = create_access_token({
        "user_id": "missing-user-id",
        "email": "missing@example.com"
    })

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404

    data = response.get_json()

    assert "error" in data