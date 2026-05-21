from app.external_apis.google_oauth import (
    exchange_auth_code,
    get_google_user_info
)

from app.repositories.user_repository import (
    find_user_by_email,
    create_user
)

from app.services.jwt_service import (
    create_access_token
)


def generate_google_auth_url() -> str:
    """
    Generate Google OAuth URL.
    """

    return (
        "https://accounts.google.com/o/oauth2/v2/auth"
    )


def verify_google_token(
    auth_code: str
) -> dict | None:
    """
    Exchange auth code and retrieve
    Google user information.
    """

    if not auth_code:
        return None

    try:

        access_token = exchange_auth_code(
            auth_code
        )

        if not access_token:
            return None

        google_user = get_google_user_info(
            access_token
        )

        if not google_user:
            return None

        return google_user

    except Exception:
        return None


def process_google_login(
    auth_code: str
) -> dict:
    """
    Handle Google OAuth login/signup flow.
    """

    if not auth_code:
        return {
            "success": False,
            "message": "Authorization code is required"
        }

    google_user = verify_google_token(
        auth_code
    )

    if not google_user:
        return {
            "success": False,
            "message": "Google authentication failed"
        }

    email = google_user.get("email")
    name = google_user.get("name")

    if not email or not name:
        return {
            "success": False,
            "message": "Invalid Google account data"
        }

    existing_user = find_user_by_email(
        email
    )

    if not existing_user:

        existing_user = create_user(
            name=name,
            email=email,
            password=None
        )

    token = create_access_token({
        "user_id": existing_user["id"],
        "email": existing_user["email"]
    })

    return {
        "success": True,
        "message": "Google authentication successful",
        "token": token,
        "user": {
            "id": existing_user["id"],
            "name": existing_user["name"],
            "email": existing_user["email"]
        }
    }