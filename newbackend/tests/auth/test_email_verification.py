def test_verify_email_route_exists(client):

    response = client.post(
        "/auth/verify-email",
        json={}
    )

    assert response.status_code in [200, 400, 401]


def test_verify_email_invalid_token(client):

    response = client.post(
        "/auth/verify-email",
        json={
            "token": "invalid-token"
        }
    )

    assert response.status_code in [400, 401]