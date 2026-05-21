import secrets
import bcrypt

def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )
    return hashed_password.decode("utf-8")

def verify_password(
    password: str,
    hashed_password: str
) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

def generate_secure_token(
    length: int = 32
) -> str:
    return secrets.token_hex(length)

def sanitize_input(value: str) -> str:
    return value.strip()