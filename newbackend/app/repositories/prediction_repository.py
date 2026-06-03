from typing import Any, Dict, List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pymongo.collection import Collection
from pymongo.errors import PyMongoError

from app.database.collections import (
    predictions_collection
)
from app.utils.helpers import (
    get_current_timestamp
)


def _get_predictions_collection() -> Collection:
    """
    Resolve MongoDB predictions collection.
    Return predictions collection.
    """

    if callable(predictions_collection):
        return predictions_collection()

    return predictions_collection


def save_prediction(
    *,
    user_id: str,
    input_data: Dict[str, Any],
    prediction_results: Dict[str, Any],
    recommendation: Optional[str] = None
) -> Dict[str, Any]:
    """
    Save prediction history record.
    """

    document = {
        "user_id": user_id,
        "created_at": get_current_timestamp(),
        "input_data": input_data,
        "prediction_results": prediction_results,
        "recommendation": recommendation
    }

    try:

        result = (
            _get_predictions_collection()
            .insert_one(document)
        )

    except PyMongoError as error:

        raise RuntimeError(
            "Failed to save prediction"
        ) from error

    document["_id"] = result.inserted_id

    return document


def get_prediction_history(
    user_id: str,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    Get prediction history for a user.
    """

    try:
        return list(
            _get_predictions_collection()
            .find({"user_id": user_id})
            .sort("created_at", -1)
            .limit(limit)
        )

    except PyMongoError as error:

        raise RuntimeError(
            "Failed to retrieve prediction history"
        ) from error

def get_prediction_by_id(
    prediction_id: str
) -> Optional[Dict[str, Any]]:
    """
    Get prediction by ID.
    """

    try:
        object_id = ObjectId(
            prediction_id
        )

    except InvalidId:
        return None

    try:

        return (
            _get_predictions_collection()
            .find_one(
                {"_id": object_id}
            )
        )

    except PyMongoError as error:

        raise RuntimeError(
            "Failed to retrieve prediction"
        ) from error

def delete_prediction(
    prediction_id: str
) -> bool:
    """
    Delete prediction by ID.
    """

    try:

        object_id = ObjectId(
            prediction_id
        )

    except InvalidId:

        return False

    try:

        result = (
            _get_predictions_collection()
            .delete_one(
                {"_id": object_id}
            )
        )

    except PyMongoError as error:

        raise RuntimeError(
            "Failed to delete prediction"
        ) from error

    return result.deleted_count > 0
