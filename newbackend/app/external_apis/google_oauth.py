import os
from typing import Dict, Any, Optional

import requests


GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")


def get_google_provider_config() -> Dict[str, Any]:
    """
    Fetch Google OAuth provider metadata.
    """

    response = requests.get(
        GOOGLE_DISCOVERY_URL,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def exchange_auth_code(code: str) -> Optional[Dict[str, Any]]:
    """
    Exchange Google authorization code for tokens.
    """

    provider_config = get_google_provider_config()

    token_endpoint = provider_config["token_endpoint"]

    payload = {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": GOOGLE_REDIRECT_URI
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(
        token_endpoint,
        data=payload,
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        return None

    return response.json()


def get_google_user_info(
    access_token: str
) -> Optional[Dict[str, Any]]:
    """
    Retrieve authenticated Google user profile.
    """

    provider_config = get_google_provider_config()

    userinfo_endpoint = provider_config["userinfo_endpoint"]

    response = requests.get(
        userinfo_endpoint,
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        timeout=10
    )

    if response.status_code != 200:
        return None

    return response.json()