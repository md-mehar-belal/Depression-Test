import json

from typing import Any, Dict
from datetime import datetime, UTC

from app.utils.logger import get_logger


request_logger = get_logger(
    "request_logger",
    "data/logs/requests.log"
)

error_logger = get_logger(
    "error_logger",
    "data/logs/errors.log"
)

auth_logger = get_logger(
    "auth_logger",
    "data/logs/auth.log"
)


def log_request(
    method: str | dict,
    endpoint: str | None = None,
    ip_address: str | None = None,
    status_code: int | None = None
) -> None:
    """
    Log incoming API request.
    """

    try:

        # CONTRACT ISSUE:
        # logging_middleware passed a single dictionary while this
        # service expected four positional values. That mismatch breaks
        # the middleware/service lifecycle contract.
        #
        # Legacy strict formatting:
        # request_logger.info(
        #     f"{method} | {endpoint} | "
        #     f"IP={ip_address} | STATUS={status_code}"
        # )
        if isinstance(method, dict):
            request_logger.info(
                json.dumps(method)
            )
        else:
            request_logger.info(
                f"{method} | {endpoint} | "
                f"IP={ip_address} | STATUS={status_code}"
            )

    except Exception:
        pass


def log_error(
    error: Exception,
    context: Dict[str, Any] | None = None
) -> None:
    """
    Log application errors.
    """

    try:

        payload = {
            "timestamp": datetime.now(
                UTC
            ).isoformat(),
            "error": str(error),
            "context": context or {}
        }

        error_logger.error(
            json.dumps(payload)
        )

    except Exception:
        pass


def log_auth_event(
    event: str,
    details: Dict[str, Any]
) -> None:
    """
    Log authentication-related events.
    """

    try:

        payload = {
            "timestamp": datetime.now(
                UTC
            ).isoformat(),
            "event": event,
            "details": details
        }

        auth_logger.info(
            json.dumps(payload)
        )

    except Exception:
        pass


def log_prediction(
    user_id: str,
    prediction_data: Dict[str, Any],
    prediction_id: str | None = None
) -> None:
    """
    Log prediction activity.
    """

    try:

        payload = {
            "timestamp": datetime.now(
                UTC
            ).isoformat(),
            "user_id": user_id,
            "prediction_id": prediction_id,
            "prediction": prediction_data
        }

        request_logger.info(
            json.dumps(payload)
        )

    except Exception:
        pass
