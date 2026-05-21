def test_logout_success(client, auth_headers):

    response = client.get(
        "/auth/logout",
        headers=auth_headers
    )

    assert response.status_code in [200, 204]


def test_logout_without_token(client):

    response = client.get(
        "/auth/logout"
    )

    assert response.status_code in [200, 401]