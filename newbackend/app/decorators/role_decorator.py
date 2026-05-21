from functools import wraps
from typing import Callable, List

from flask import jsonify, g


def role_required(
    allowed_roles: List[str]
):
    """
    Restrict route access based on user role.
    """

    def decorator(function: Callable):

        @wraps(function)
        def wrapper(*args, **kwargs):

            current_user = getattr(
                g,
                "current_user",
                None
            )

            if not current_user:
                return jsonify({
                    "success": False,
                    "message": "Unauthorized"
                }), 401

            user_role = current_user.get(
                "role",
                "user"
            )

            if user_role not in allowed_roles:
                return jsonify({
                    "success": False,
                    "message": "Forbidden"
                }), 403

            return function(*args, **kwargs)

        return wrapper

    return decorator