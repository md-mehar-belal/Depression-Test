import time

from flask import Request, Response, g, request

from app.services.logging_service import (
    log_request,
    log_error
)


def log_response(
    response_data: dict
) -> None:
    """
    Backward-compatible response logging adapter.
    """

    # REFACTOR IMPROVEMENT:
    # Older tests and callers patch log_response at the middleware
    # boundary. Keeping this adapter preserves compatibility while the
    # actual logging contract remains centralized in logging_service.
    log_request(
        method=response_data["method"],
        endpoint=response_data["path"],
        ip_address=response_data.get("ip_address"),
        status_code=response_data["status_code"]
    )


def log_request_middleware() -> None:
    """
    Logs incoming request metadata.
    """

    g.request_start_time = time.time()

    request_data = {
        "method": request.method,
        "path": request.path,
        "ip_address": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
    }

    # CONTRACT ISSUE:
    # Passing the whole dictionary relied on a service contract that
    # did not match log_request(method, endpoint, ip_address,
    # status_code). That can hide middleware failures and make request
    # lifecycle logging inconsistent.
    #
    # Legacy problematic call:
    # log_request(request_data)
    try:
        log_request(
            method=request_data["method"],
            endpoint=request_data["path"],
            ip_address=request_data["ip_address"],
            status_code=0
        )
    except Exception as error:
        log_error(
            f"Request logging middleware error: {str(error)}"
        )


def log_response_middleware(response: Response) -> Response:
    """
    Logs outgoing response metadata and request duration.
    """

    try:
        duration = round(
            time.time() - getattr(
                g,
                "request_start_time",
                time.time()
            ),
            4
        )

        response_data = {
            "method": request.method,
            "path": request.path,
            "ip_address": request.remote_addr,
            "status_code": response.status_code,
            "duration_seconds": duration,
        }

        # CONTRACT ISSUE:
        # Passing the whole dictionary relied on a service contract
        # mismatch and could fail during after_request handling.
        #
        # Legacy problematic call:
        # log_request(response_data)
        log_response(response_data)

    except Exception as error:
        log_error(
            f"Response logging middleware error: {str(error)}"
        )

    return response
