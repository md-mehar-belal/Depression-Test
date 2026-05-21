from flask import jsonify

from app.services.logging_service import log_error


def handle_validation_error(error):
    """
    Handles request validation errors.
    """

    log_error(
        f"Validation Error: {str(error)}"
    )

    return jsonify({
        "success": False,
        "message": "Validation failed",
        "error": str(error)
    }), 400


def handle_auth_error(error):
    """
    Handles authentication and authorization errors.
    """

    log_error(
        f"Authentication Error: {str(error)}"
    )

    return jsonify({
        "success": False,
        "message": "Authentication failed",
        "error": str(error)
    }), 401


def handle_server_error(error):
    """
    Handles unexpected server-side exceptions.
    """

    log_error(
        f"Internal Server Error: {str(error)}"
    )

    return jsonify({
        "success": False,
        "message": "Internal server error"
    }), 500