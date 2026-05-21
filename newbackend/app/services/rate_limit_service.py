from time import time
from typing import Dict, List

from flask import Request

from app.utils.constants import (
    RATE_LIMIT_MAX_REQUESTS,
    RATE_LIMIT_WINDOW_SECONDS
)


RATE_LIMIT_STORAGE: Dict[str, List[float]] = {}


def get_client_ip(
    request: Request
) -> str:
    """
    Extract client IP address safely.
    """

    forwarded_for = request.headers.get(
        "X-Forwarded-For"
    )

    if forwarded_for:

        return forwarded_for.split(
            ","
        )[0].strip()

    return request.remote_addr or "unknown"


def cleanup_expired_requests(
    client_ip: str
) -> None:
    """
    Remove expired timestamps from storage.
    """

    current_time = time()

    request_timestamps = RATE_LIMIT_STORAGE.get(
        client_ip,
        []
    )

    valid_timestamps = [
        timestamp
        for timestamp in request_timestamps
        if current_time - timestamp
        < RATE_LIMIT_WINDOW_SECONDS
    ]

    RATE_LIMIT_STORAGE[client_ip] = (
        valid_timestamps
    )


def check_rate_limit(
    client_ip: str
) -> bool:
    """
    Check whether client exceeded limit.
    """

    client_ip = client_ip or "unknown"

    cleanup_expired_requests(
        client_ip
    )

    request_count = len(
        RATE_LIMIT_STORAGE.get(
            client_ip,
            []
        )
    )

    # CONTRACT ISSUE:
    # The middleware previously assumed this function returned
    # (is_allowed, retry_after), but the service contract has always
    # been a boolean limit check. Returning a boolean preserves
    # existing service callers and keeps retry calculation out of the
    # core counter check.
    #
    # Legacy incompatible middleware expectation:
    # return is_allowed, retry_after
    return (
        request_count
        < RATE_LIMIT_MAX_REQUESTS
    )


def update_rate_limit(
    client_ip: str
) -> None:
    """
    Store current request timestamp.
    """

    client_ip = client_ip or "unknown"

    cleanup_expired_requests(
        client_ip
    )

    current_time = time()

    if client_ip not in RATE_LIMIT_STORAGE:

        RATE_LIMIT_STORAGE[client_ip] = []

    RATE_LIMIT_STORAGE[
        client_ip
    ].append(current_time)
