from flask import g, request

from app.services.jwt_service import (
    extract_token
)

from app.services.auth_service import (
    authenticate_access_token
)


PUBLIC_ROUTES = {
    "/auth/login",
    "/auth/signup",
    "/auth/google",
    "/auth/google/callback",
    "/auth/forgot-password",
    "/auth/reset-password",
    "/auth/verify-email",
}


def authenticate_request():
    """
    Authenticate protected routes using JWT.
    """

    if request.path in PUBLIC_ROUTES:
        return None

    token = extract_token(request)

    if not token:
        return {
            "success": False,
            "message": "Authentication token missing"
        }, 401

    # ARCHITECTURAL VIOLATION:
    # Middleware previously verified tokens and loaded users by calling
    # the repository directly. That made request lifecycle code own
    # persistence access and bypassed the auth service boundary.
    #
    # Legacy problematic flow:
    # payload = verify_token(token)
    # user = find_user_by_id(payload.get("user_id"))
    auth_result = authenticate_access_token(token)

    if not auth_result["success"]:
        return {
            "success": False,
            "message": auth_result["message"]
        }, auth_result["status_code"]

    attach_current_user(
        auth_result["user"]
    )

    return None


def attach_current_user(user: dict) -> None:
    """
    Attach authenticated user to Flask request context.
    """

    g.current_user = user
