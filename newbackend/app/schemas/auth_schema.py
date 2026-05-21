# app/schemas/auth_schema.py

def serialize_user(
    user: dict
) -> dict:
    """
    Serialize user object.
    """

    # DUPLICATED SERIALIZATION LOGIC:
    # This schema had a narrower user shape than the repository
    # serializer. That created two competing API user representations
    # and increased maintenance risk when user fields changed.
    #
    # Legacy narrower response:
    # return {
    #     "id": str(user.get("id")),
    #     "name": user.get("name"),
    #     "email": user.get("email")
    # }
    return {
        "id": str(user.get("id")),
        "name": user.get("name"),
        "email": user.get("email"),
        "role": user.get("role", "user"),
        "is_verified": user.get("is_verified", False),
        "created_at": user.get("created_at"),
        "updated_at": user.get("updated_at")
    }


def serialize_auth_response(
    message: str,
    token: str,
    user: dict
) -> dict:
    """
    Serialize authentication response.
    """

    return {
        "message": message,
        "token": token,
        "user": serialize_user(user)
    }
