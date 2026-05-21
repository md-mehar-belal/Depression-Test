import bcrypt


def test_password_is_hashed():

    password = "SecurePassword123"

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    assert hashed_password != password

    assert hashed_password.startswith("$2b$")


def test_password_hash_verification_success():

    password = "MyPassword123"

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    is_valid = bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password
    )

    assert is_valid is True


def test_password_hash_verification_failure():

    password = "CorrectPassword"

    wrong_password = "WrongPassword"

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    is_valid = bcrypt.checkpw(
        wrong_password.encode("utf-8"),
        hashed_password
    )

    assert is_valid is False


def test_same_password_generates_different_hashes():

    password = "RepeatedPassword"

    hash_one = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    hash_two = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    assert hash_one != hash_two


def test_hashes_still_validate_for_same_password():

    password = "RepeatedPassword"

    hash_one = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    hash_two = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    assert bcrypt.checkpw(
        password.encode("utf-8"),
        hash_one
    )

    assert bcrypt.checkpw(
        password.encode("utf-8"),
        hash_two
    )