from flask import Flask, request

from app.services.rate_limit_service import (
    RATE_LIMIT_STORAGE,
    cleanup_expired_requests,
    get_client_ip,
    check_rate_limit,
    update_rate_limit
)

from app.utils.constants import (
    RATE_LIMIT_MAX_REQUESTS
)


# =========================================================
# SETUP
# =========================================================

def setup_function():

    RATE_LIMIT_STORAGE.clear()


# =========================================================
# CLIENT IP TESTS
# =========================================================

def test_get_client_ip_from_forwarded_header():

    app = Flask(__name__)

    with app.test_request_context(
        headers={
            "X-Forwarded-For": (
                "192.168.1.1"
            )
        }
    ):

        ip_address = get_client_ip(
            request
        )

        assert ip_address == (
            "192.168.1.1"
        )


def test_get_client_ip_from_remote_addr():

    app = Flask(__name__)

    with app.test_request_context():

        ip_address = get_client_ip(
            request
        )

        assert ip_address is not None


# =========================================================
# CLEANUP TESTS
# =========================================================

def test_cleanup_expired_requests():

    client_ip = "127.0.0.1"

    RATE_LIMIT_STORAGE[
        client_ip
    ] = []

    cleanup_expired_requests(
        client_ip
    )

    assert isinstance(
        RATE_LIMIT_STORAGE[client_ip],
        list
    )


# =========================================================
# RATE LIMIT CHECK TESTS
# =========================================================

def test_check_rate_limit_initially_true():

    result = check_rate_limit(
        "127.0.0.1"
    )

    assert result is True


def test_check_rate_limit_exceeded():

    client_ip = "127.0.0.1"

    for _ in range(
        RATE_LIMIT_MAX_REQUESTS
    ):

        update_rate_limit(
            client_ip
        )

    result = check_rate_limit(
        client_ip
    )

    assert result is False


def test_check_rate_limit_unknown_ip():

    result = check_rate_limit("")

    assert result is True


# =========================================================
# UPDATE RATE LIMIT TESTS
# =========================================================

def test_update_rate_limit():

    client_ip = "127.0.0.1"

    update_rate_limit(
        client_ip
    )

    assert client_ip in (
        RATE_LIMIT_STORAGE
    )

    assert len(
        RATE_LIMIT_STORAGE[
            client_ip
        ]
    ) == 1


def test_update_rate_limit_unknown_ip():

    update_rate_limit("")

    assert "unknown" in (
        RATE_LIMIT_STORAGE
    )