def test_signup_success(client, sample_user):

    response = client.post(
        "/auth/signup",
        json=sample_user
    )

    assert response.status_code == 201

    data = response.get_json()

    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == sample_user["email"]


def test_signup_duplicate_email(client, sample_user):

    client.post(
        "/auth/signup",
        json=sample_user
    )

    response = client.post(
        "/auth/signup",
        json=sample_user
    )

    assert response.status_code == 409


def test_signup_invalid_email(client, sample_user):

    sample_user["email"] = "invalid-email"

    response = client.post(
        "/auth/signup",
        json=sample_user
    )

    assert response.status_code == 400


def test_signup_weak_password(client, sample_user):

    sample_user["password"] = "123"

    response = client.post(
        "/auth/signup",
        json=sample_user
    )

    assert response.status_code == 400


def test_signup_missing_fields(client):

    response = client.post(
        "/auth/signup",
        json={}
    )

    assert response.status_code == 400