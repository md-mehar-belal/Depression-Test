from functools import wraps
from typing import Callable

from flask import request, jsonify, g

from app.services.jwt_service import (
    extract_token,
    decode_token,
    verify_token
)


def jwt_required():
    """
    Require valid access token.
    """

    def decorator(function: Callable):

        @wraps(function)
        def wrapper(*args, **kwargs):

            token = extract_token(request)

            if not token:
                return jsonify({
                    "success": False,
                    "message": "Authorization token missing"
                }), 401

            is_valid = verify_token(
                token,
                expected_type="access"
            )

            if not is_valid:
                return jsonify({
                    "success": False,
                    "message": "Invalid or expired token"
                }), 401

            payload = decode_token(token)

            g.current_user = payload

            return function(*args, **kwargs)

        return wrapper

    return decorator


def optional_jwt():
    """
    Attach JWT payload if token exists,
    but do not block request.
    """

    def decorator(function: Callable):

        @wraps(function)
        def wrapper(*args, **kwargs):

            token = extract_token(request)

            if not token:
                g.current_user = None
                return function(*args, **kwargs)

            is_valid = verify_token(
                token,
                expected_type="access"
            )

            if not is_valid:
                g.current_user = None
                return function(*args, **kwargs)

            g.current_user = decode_token(token)

            return function(*args, **kwargs)

        return wrapper

    return decorator