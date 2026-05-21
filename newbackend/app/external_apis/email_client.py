import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL")


def connect_smtp_server() -> smtplib.SMTP:
    """
    Create and authenticate SMTP connection.
    """

    server = smtplib.SMTP(
        SMTP_HOST,
        SMTP_PORT
    )

    server.starttls()

    server.login(
        SMTP_USERNAME,
        SMTP_PASSWORD
    )

    return server


def send_email_message(
    to_email: str,
    subject: str,
    body: str,
    is_html: bool = False
) -> bool:
    """
    Send email using configured SMTP server.
    """

    try:
        message = MIMEMultipart()

        message["From"] = SMTP_FROM_EMAIL
        message["To"] = to_email
        message["Subject"] = subject

        content_type = "html" if is_html else "plain"

        message.attach(
            MIMEText(body, content_type)
        )

        server = connect_smtp_server()

        server.sendmail(
            SMTP_FROM_EMAIL,
            to_email,
            message.as_string()
        )

        server.quit()

        return True

    except Exception:
        return False