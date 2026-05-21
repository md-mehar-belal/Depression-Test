from datetime import datetime, timedelta, UTC

import jwt

from app.services.jwt_service import create_access_token
from fixtures.user_fixtures import SERIALIZED_USER


JWT_SECRET = "test-secret-key"
JWT_ALGORITHM = "HS256"


VALID_USER_ID = SERIALIZED_USER["id"]
VALID_USER_EMAIL = SERIALIZED_USER["email"]


VALID_TOKEN_PAYLOAD = {
    "user_id": VALID_USER_ID,
    "email": VALID_USER_EMAIL
}


VALID_ACCESS_TOKEN = create_access_token(
    VALID_TOKEN_PAYLOAD
)


EXPIRED_TOKEN = jwt.encode(
    {
        "user_id": VALID_USER_ID,
        "email": VALID_USER_EMAIL,
        "exp": datetime.now(UTC) - timedelta(hours=1)
    },
    JWT_SECRET,
    algorithm=JWT_ALGORITHM
)


INVALID_TOKEN = (
    "invalid.jwt.token"
)


MALFORMED_TOKEN = (
    "abc.def"
)


BEARER_TOKEN = (
    f"Bearer {VALID_ACCESS_TOKEN}"
)


INVALID_BEARER_TOKEN = (
    f"Bearer {INVALID_TOKEN}"
)