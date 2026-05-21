from urllib.parse import quote_plus
from typing import Optional, TypedDict

import smtplib

from app.external_apis.email_client import send_email_message
from app.services.logging_service import log_auth_event

from app.utils.helpers import get_current_timestamp

from app.utils.constants import (
    EMAIL_VERIFICATION_SUBJECT,
    RESET_PASSWORD_SUBJECT,
    FRONTEND_BASE_URL
)


class EmailResult(TypedDict):
    success: bool
    error: Optional[str]


def send_email(
    to_email: str,
    subject: str,
    body: str
) -> EmailResult:
    """
    Generic email sender wrapper.
    """

    if (
        not isinstance(to_email, str)
        or not isinstance(subject, str)
        or not isinstance(body, str)
    ):
        return {
            "success": False,
            "error": "Invalid input types"
        }

    to_email = to_email.strip()
    subject = subject.strip()
    body = body.strip()

    if not to_email or not subject or not body:
        return {
            "success": False,
            "error": "Missing required email fields"
        }

    try:

        success = send_email_message(
            to_email=to_email,
            subject=subject,
            body=body
        )

        log_auth_event(
            event="email_sent",
            details={
                "recipient": mask_email(to_email),
                "subject": subject,
                "success": success,
                "timestamp": get_current_timestamp()
            }
        )

        return {
            "success": success,
            "error": None if success else "Email provider rejected request"
        }

    except (
        smtplib.SMTPException,
        ConnectionError,
        TimeoutError
    ) as error:

        log_auth_event(
            event="email_failed",
            details={
                "recipient": mask_email(to_email),
                "subject": subject,
                "error": str(error),
                "timestamp": get_current_timestamp()
            }
        )

        return {
            "success": False,
            "error": str(error)
        }


def build_verification_email_body(
    verification_token: str
) -> str:
    """
    Build email verification body.
    """

    encoded_token = quote_plus(
        verification_token
    )

    verification_link = (
        f"{FRONTEND_BASE_URL}/verify-email"
        f"?token={encoded_token}"
    )

    return f"""
Welcome to the platform.

Please verify your email using the link below:

{verification_link}

If you did not create this account,
please ignore this email.
""".strip()


def build_reset_password_email_body(
    reset_token: str
) -> str:
    """
    Build reset password email body.
    """

    encoded_token = quote_plus(
        reset_token
    )

    reset_link = (
        f"{FRONTEND_BASE_URL}/reset-password"
        f"?token={encoded_token}"
    )

    return f"""
A password reset was requested.

Reset your password using the link below:

{reset_link}

If you did not request this,
please ignore this email.
""".strip()


def send_verification_email(
    email: str,
    verification_token: str
) -> EmailResult:
    """
    Send account verification email.
    """

    if not email or not verification_token:
        return {
            "success": False,
            "error": "Missing verification email data"
        }

    body = build_verification_email_body(
        verification_token
    )

    return send_email(
        to_email=email,
        subject=EMAIL_VERIFICATION_SUBJECT,
        body=body
    )


def send_reset_password_email(
    email: str,
    reset_token: str
) -> EmailResult:
    """
    Send reset password email.
    """

    if not email or not reset_token:
        return {
            "success": False,
            "error": "Missing reset email data"
        }

    body = build_reset_password_email_body(
        reset_token
    )

    return send_email(
        to_email=email,
        subject=RESET_PASSWORD_SUBJECT,
        body=body
    )


def mask_email(
    email: str
) -> str:
    """
    Mask email for logs.
    """

    try:

        local, domain = email.split("@")

        if len(local) <= 2:
            masked_local = "*" * len(local)

        else:
            masked_local = (
                local[:2]
                + ("*" * (len(local) - 2))
            )

        return f"{masked_local}@{domain}"

    except ValueError:
        return "***invalid-email***"