from flask import jsonify, request

from app.services.rate_limit_service import (
    check_rate_limit,
    update_rate_limit,
    get_client_ip
)


def rate_limit_middleware():
    """
    Global API throttling middleware.
    """

    client_ip = get_client_ip(request)

    # CONTRACT ISSUE:
    # check_rate_limit() returns a boolean, but this middleware tried
    # to unpack it as (is_allowed, retry_after). That violates the
    # middleware/service contract and fails before a response can be
    # returned.
    #
    # Legacy problematic call:
    # is_allowed, retry_after = check_rate_limit(client_ip)
    is_allowed = check_rate_limit(client_ip)

    if not is_allowed:

        return jsonify({
            "success": False,
            "error": "Rate limit exceeded",
            "message": "Rate limit exceeded",
            "retry_after_seconds": None
        }), 429

    update_rate_limit(client_ip)

    return None
