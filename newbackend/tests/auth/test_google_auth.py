def test_google_auth_missing_token(client):

    response = client.post(
        "/auth/google/callback",
        json={}
    )

    assert response.status_code == 400


def test_google_auth_invalid_token(client):

    response = client.post(
        "/auth/google/callback",
        json={
            "token": "invalid-google-token"
        }
    )

    assert response.status_code in [400, 401]


def test_google_auth_route_exists(client):

    response = client.get("/auth/google")

    assert response.status_code in [200, 302]