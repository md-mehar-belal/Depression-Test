def test_login_success(client, sample_user, login_payload):

    client.post(
        "/auth/signup",
        json=sample_user
    )

    response = client.post(
        "/auth/login",
        json=login_payload
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "token" in data
    assert "user" in data


def test_login_wrong_password(client, sample_user):

    client.post(
        "/auth/signup",
        json=sample_user
    )

    response = client.post(
        "/auth/login",
        json={
            "email": sample_user["email"],
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401


def test_login_nonexistent_user(client):

    response = client.post(
        "/auth/login",
        json={
            "email": "nouser@test.com",
            "password": "password123"
        }
    )

    assert response.status_code == 401


def test_login_missing_email(client):

    response = client.post(
        "/auth/login",
        json={
            "password": "password123"
        }
    )

    assert response.status_code == 400


def test_login_missing_password(client):

    response = client.post(
        "/auth/login",
        json={
            "email": "test@test.com"
        }
    )

    assert response.status_code == 400