from flask import request

from app.services.auth_service import (
    signup_user,
    login_user,
    get_current_user,
    logout_user,
    forgot_password,
    reset_password,
    verify_email
)

from app.services.google_auth_service import (
    generate_google_auth_url,
    process_google_login
)

from app.utils.response import (
    success_response,
    error_response
)


def signup_controller():
    """
    Handle user signup requests.
    """

    try:
        request_data = request.get_json() or {}

        result = signup_user(request_data)

        return success_response(
            message="Signup successful",
            data=result,
            status_code=201
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=400
        )


def login_controller():
    """
    Handle user login requests.
    """

    try:
        request_data = request.get_json() or {}

        result = login_user(request_data)

        return success_response(
            message="Login successful",
            data=result
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=401
        )


def google_login_controller():
    """
    Generate Google OAuth login URL.
    """

    try:
        auth_url = generate_google_auth_url()

        return success_response(
            message="Google auth URL generated",
            data={
                "auth_url": auth_url
            }
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=500
        )


def google_callback_controller():
    """
    Handle Google OAuth callback flow.
    """

    try:
        request_data = request.get_json() or {}

        # CONTRACT ISSUE:
        # process_google_login() expects an authorization code string,
        # but the controller passed the full request dictionary. That
        # violates the controller/service contract and can make the
        # Google flow fail even with a valid payload.
        #
        # Legacy problematic call:
        # result = process_google_login(request_data)
        result = process_google_login(
            request_data.get("code")
            or request_data.get("auth_code")
        )

        return success_response(
            message="Google login successful",
            data=result
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=401
        )


def forgot_password_controller():
    """
    Handle forgot password requests.
    """

    try:
        request_data = request.get_json() or {}

        result = forgot_password(request_data)

        return success_response(
            message="Password reset initiated",
            data=result
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=400
        )


def reset_password_controller():
    """
    Handle password reset requests.
    """

    try:
        request_data = request.get_json() or {}

        # CONTRACT ISSUE:
        # reset_password() expects token and new_password arguments,
        # but the controller passed the whole JSON dictionary. That
        # violates the controller/service contract and causes a
        # missing-argument runtime failure.
        #
        # Legacy problematic call:
        # result = reset_password(request_data)
        result = reset_password(
            token=request_data.get("token"),
            new_password=request_data.get("new_password")
        )

        return success_response(
            message="Password reset successful",
            data=result
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=400
        )


def verify_email_controller():
    """
    Handle email verification requests.
    """

    try:
        request_data = request.get_json() or {}

        # CONTRACT ISSUE:
        # verify_email() expects a token string, but the controller
        # passed the whole JSON dictionary. That violates the
        # controller/service contract and causes token verification to
        # receive the wrong type.
        #
        # Legacy problematic call:
        # result = verify_email(request_data)
        result = verify_email(
            request_data.get("token")
        )

        return success_response(
            message="Email verified successfully",
            data=result
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=400
        )


def get_current_user_controller():
    """
    Return authenticated user profile.
    """

    try:
        token = request.headers.get("Authorization")

        result = get_current_user(token)

        return success_response(
            message="Current user fetched successfully",
            data=result
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=401
        )


def logout_controller():
    """
    Handle logout requests.
    """

    try:
        result = logout_user()

        return success_response(
            message="Logout successful",
            data=result
        )

    except Exception as error:
        return error_response(
            message=str(error),
            status_code=400
        )
