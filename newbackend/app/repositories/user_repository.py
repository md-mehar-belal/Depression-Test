from typing import Optional, Dict, Any
from bson import ObjectId

from app.database.collections import users_collection
from app.utils.helpers import get_current_timestamp


def _get_users_collection():
    """
    Resolve the users collection accessor.
    """

    # ARCHITECTURAL VIOLATION:
    # This repository previously used users_collection as if it were a
    # PyMongo collection object, even though database/collections.py
    # exposes accessor functions. That violates the repository/database
    # boundary and raises attribute errors at runtime.
    #
    # Legacy problematic usage:
    # users_collection.insert_one(...)
    if callable(users_collection) and not hasattr(
        users_collection,
        "insert_one"
    ):
        return users_collection()

    return users_collection


def create_user(
    user_data: Optional[Dict[str, Any]] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Create a new user document.
    """

    # BACKWARD COMPATIBILITY:
    # Some services historically called create_user(name=..., email=...),
    # while the repository contract accepts a user_data dictionary.
    # Supporting kwargs avoids a cascading rewrite outside the explicit
    # violation scope.
    if user_data is None:
        user_data = kwargs

    document = {
        "name": user_data["name"],
        "email": user_data["email"],
        "password": user_data["password"],
        "is_verified": False,
        "role": "user",
        "created_at": get_current_timestamp(),
        "updated_at": get_current_timestamp()
    }

    collection = _get_users_collection()

    result = collection.insert_one(document)

    document["_id"] = result.inserted_id

    return serialize_user(document)


def find_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """
    Find user using email address.
    """

    collection = _get_users_collection()

    user = collection.find_one({
        "email": email
    })

    if not user:
        return None

    return serialize_user(user, include_password=True)


def find_user_by_id(user_id: str) -> Optional[Dict[str, Any]]:
    """
    Find user using MongoDB ObjectId.
    """

    try:
        collection = _get_users_collection()

        user = collection.find_one({
            "_id": ObjectId(user_id)
        })

        if not user:
            return None

        return serialize_user(user)

    except Exception:
        return None


def update_user(
    user_id: str,
    update_data: Dict[str, Any]
) -> bool:
    """
    Update user fields.
    """

    update_data["updated_at"] = get_current_timestamp()

    collection = _get_users_collection()

    result = collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    return result.modified_count > 0


def verify_user_email(user_id: str) -> bool:
    """
    Mark user email as verified.
    """

    collection = _get_users_collection()

    result = collection.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "is_verified": True,
                "updated_at": get_current_timestamp()
            }
        }
    )

    return result.modified_count > 0


def serialize_user(
    user: Dict[str, Any],
    include_password: bool = False
) -> Dict[str, Any]:
    """
    Convert MongoDB document into API-safe dictionary.
    """

    serialized_user = {
        "id": str(user["_id"]),
        "name": user.get("name"),
        "email": user.get("email"),
        "role": user.get("role", "user"),
        "is_verified": user.get("is_verified", False),
        "created_at": user.get("created_at"),
        "updated_at": user.get("updated_at")
    }

    if include_password:
        serialized_user["password"] = user.get("password")

    return serialized_user
