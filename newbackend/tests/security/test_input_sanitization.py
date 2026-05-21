import re


def sanitize_input(value):

    if value is None:
        return ""

    value = str(value).strip()

    # Remove script tags
    value = re.sub(
        r"<script.*?>.*?</script>",
        "",
        value,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Remove basic HTML tags
    value = re.sub(
        r"<.*?>",
        "",
        value
    )

    return value


def test_remove_script_tags():

    malicious_input = (
        "<script>alert('hacked')</script>"
    )

    sanitized = sanitize_input(
        malicious_input
    )

    assert "<script>" not in sanitized

    assert "alert" not in sanitized


def test_remove_html_tags():

    raw_input = "<h1>Hello</h1>"

    sanitized = sanitize_input(
        raw_input
    )

    assert sanitized == "Hello"


def test_trim_whitespace():

    raw_input = "   test@example.com   "

    sanitized = sanitize_input(
        raw_input
    )

    assert sanitized == "test@example.com"


def test_email_normalization():

    email = "   USER@Example.COM   "

    sanitized = sanitize_input(
        email
    ).lower()

    assert sanitized == "user@example.com"


def test_none_input_returns_empty_string():

    sanitized = sanitize_input(None)

    assert sanitized == ""


def test_safe_plain_text_remains_unchanged():

    text = "Normal user message"

    sanitized = sanitize_input(text)

    assert sanitized == text


def test_nested_html_removed():

    raw_input = (
        "<div><b>Important</b></div>"
    )

    sanitized = sanitize_input(
        raw_input
    )

    assert sanitized == "Important"


def test_sql_like_input_not_executed():

    raw_input = "'; DROP TABLE users; --"

    sanitized = sanitize_input(
        raw_input
    )

    assert "DROP TABLE" in sanitized

    assert isinstance(sanitized, str)


def test_javascript_event_attributes_removed():

    raw_input = (
        '<img src="x" onerror="alert(1)">'
    )

    sanitized = sanitize_input(
        raw_input
    )

    assert "onerror" not in sanitized

    assert "<img" not in sanitized