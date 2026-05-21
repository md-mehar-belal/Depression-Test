def test_forgot_password_success(client, sample_user):

    client.post(
        "/auth/signup",
        json=sample_user
    )

    response = client.post(
        "/auth/forgot-password",
        json={
            "email": sample_user["email"]
        }
    )

    assert response.status_code == 200


def test_forgot_password_invalid_email(client):

    response = client.post(
        "/auth/forgot-password",
        json={
            "email": ""
        }
    )

    assert response.status_code == 400


def test_reset_password_route_exists(client):

    response = client.post(
        "/auth/reset-password",
        json={}
    )

    assert response.status_code in [200, 400, 401]