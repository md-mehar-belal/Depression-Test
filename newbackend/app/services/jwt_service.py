from datetime import datetime, timedelta, UTC
from typing import Optional, Dict, Any

import jwt
from flask import Request, current_app


TOKEN_TYPE_ACCESS = "access"
TOKEN_TYPE_REFRESH = "refresh"

DEFAULT_JWT_ALGORITHM = "HS256"


def _get_jwt_config() -> Dict[str, Any]:
    """
    Resolve JWT configuration from Flask app config.

    Fails fast if critical configuration is missing.
    """

    jwt_secret = current_app.config.get(
        "JWT_SECRET"
    ) or current_app.config.get(
        "JWT_SECRET_KEY"
    )

    if not jwt_secret:
        raise RuntimeError(
            "JWT secret is not configured."
        )

    return {
        "secret": jwt_secret,
        "algorithm": current_app.config.get(
            "JWT_ALGORITHM",
            DEFAULT_JWT_ALGORITHM
        ),
        "access_expiration": current_app.config.get(
            "JWT_ACCESS_EXPIRATION",
            current_app.config.get(
                "JWT_ACCESS_TOKEN_EXPIRES",
                15
            )
        ),
        "refresh_expiration": current_app.config.get(
            "JWT_REFRESH_EXPIRATION",
            current_app.config.get(
                "JWT_REFRESH_TOKEN_EXPIRES",
                30
            )
        )
    }


def _build_token(
    payload: Dict[str, Any],
    token_type: str,
    expiration_delta: timedelta
) -> str:
    """
    Internal JWT builder.
    """

    config = _get_jwt_config()

    now = datetime.now(UTC)

    token_payload = {
        **payload,
        "type": token_type,
        "iat": now,
        "exp": now + expiration_delta
    }

    return jwt.encode(
        token_payload,
        config["secret"],
        algorithm=config["algorithm"]
    )


def create_access_token(
    payload: Dict[str, Any]
) -> str:
    """
    Generate short-lived access token.
    """

    config = _get_jwt_config()

    return _build_token(
        payload=payload,
        token_type=TOKEN_TYPE_ACCESS,
        expiration_delta=timedelta(
            minutes=config["access_expiration"]
        )
    )


def create_refresh_token(
    payload: Dict[str, Any]
) -> str:
    """
    Generate long-lived refresh token.
    """

    config = _get_jwt_config()

    return _build_token(
        payload=payload,
        token_type=TOKEN_TYPE_REFRESH,
        expiration_delta=timedelta(
            days=config["refresh_expiration"]
        )
    )


def decode_token(
    token: str
) -> Optional[Dict[str, Any]]:
    """
    Safely decode JWT token.

    Returns:
        Decoded payload if valid, otherwise None.
    """

    if not token:
        return None

    config = _get_jwt_config()

    try:

        decoded_payload = jwt.decode(
            token,
            config["secret"],
            algorithms=[
                config["algorithm"]
            ],
            options={
                "require": [
                    "exp",
                    "iat",
                    "type"
                ]
            }
        )

        return decoded_payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None


def verify_token(
    token: str,
    expected_type: str = TOKEN_TYPE_ACCESS
) -> Optional[Dict[str, Any]]:
    """
    Verify token validity and expected type.
    """

    payload = decode_token(token)

    if not payload:
        return None

    if payload.get("type") != expected_type:
        return None

    return payload


def extract_token(
    request: Request
) -> Optional[str]:
    """
    Extract Bearer token from Authorization header.
    """

    auth_header = request.headers.get(
        "Authorization"
    )

    if not auth_header:
        return None

    parts = auth_header.strip().split(
        " ",
        1
    )

    if len(parts) != 2:
        return None

    scheme, token = parts

    if scheme != "Bearer":
        return None

    token = token.strip()

    return token or None