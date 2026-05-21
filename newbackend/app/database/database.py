from typing import Optional

from flask import current_app
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import PyMongoError

_client: Optional[MongoClient] = None


def connect_database() -> MongoClient:
    """
    Initialize and return MongoDB client.

    Creates a singleton MongoClient instance and validates
    connectivity immediately to fail fast during startup.
    """

    global _client

    if _client is not None:
        return _client

    mongo_uri = current_app.config.get("MONGODB_URI")

    if not mongo_uri:
        raise RuntimeError("MONGODB_URI is not configured")

    try:
        client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
            socketTimeoutMS=5000,
            retryWrites=True,
        )

        # Force immediate connection validation
        client.admin.command("ping")

        _client = client
        return _client

    except PyMongoError as exc:
        raise RuntimeError(
            f"Failed to connect to MongoDB: {exc}"
        ) from exc


def get_db() -> Database:
    """
    Return configured MongoDB database instance.
    """

    database_name = current_app.config.get("DATABASE_NAME")

    if not database_name:
        raise RuntimeError("DATABASE_NAME is not configured")

    client = connect_database()

    return client[database_name]


def close_database() -> None:
    """
    Close MongoDB client connection cleanly.
    """

    global _client

    if _client is not None:
        _client.close()
        _client = None