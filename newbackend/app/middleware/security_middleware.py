from flask import Request, Response, request

from app.utils.security import sanitize_input


SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Referrer-Policy": "no-referrer",
    "Content-Security-Policy": "default-src 'self'",
}


def apply_security_headers(response: Response) -> Response:
    """
    Attach security-related HTTP headers
    to every outgoing response.
    """

    for header, value in SECURITY_HEADERS.items():
        response.headers[header] = value

    return response


def sanitize_request() -> None:
    """
    Sanitize incoming request payload.

    This performs lightweight sanitization only.
    Validation logic belongs to validators.
    """

    if not request.is_json:
        return

    request_data = request.get_json(silent=True)

    if not isinstance(request_data, dict):
        return

    sanitized_data = {}

    for key, value in request_data.items():

        if isinstance(value, str):
            sanitized_data[key] = sanitize_input(value)
        else:
            sanitized_data[key] = value

    # Store sanitized payload inside request context
    request.sanitized_json = sanitized_data