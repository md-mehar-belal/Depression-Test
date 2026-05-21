from typing import Dict, Any, List, Optional
from bson import ObjectId

from app.database.collections import predictions_collection
from app.utils.helpers import get_current_timestamp


def _get_predictions_collection():
    """
    Resolve the predictions collection accessor.
    """

    # ARCHITECTURAL VIOLATION:
    # This repository previously used predictions_collection as if it
    # were a PyMongo collection object, even though database/collections.py
    # exposes accessor functions. That violates the repository/database
    # boundary and raises attribute errors at runtime.
    #
    # Legacy problematic usage:
    # predictions_collection.insert_one(...)
    if callable(predictions_collection) and not hasattr(
        predictions_collection,
        "insert_one"
    ):
        return predictions_collection()

    return predictions_collection


def save_prediction(
    prediction_data: Optional[Dict[str, Any]] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Save prediction result into database.
    """

    # BACKWARD COMPATIBILITY:
    # prediction_service previously called save_prediction(user_id=...,
    # input_data=..., prediction_data=...). The repository contract is
    # a single prediction_data dictionary, so kwargs are folded into
    # that shape without requiring unrelated callers to change.
    if prediction_data is None:
        prediction_data = kwargs
    elif kwargs:
        prediction_data = {
            **kwargs,
            "prediction_data": prediction_data
        }

    response_data = prediction_data.get(
        "prediction_data",
        {}
    )

    document = {
        "user_id": prediction_data.get("user_id"),
        "input_data": prediction_data.get("input_data"),
        "model_results": prediction_data.get(
            "model_results",
            response_data.get("model_results")
        ),
        "final_prediction": prediction_data.get(
            "final_prediction",
            response_data.get(
                "final_prediction",
                response_data.get("prediction")
            )
        ),
        "confidence_score": prediction_data.get(
            "confidence_score",
            response_data.get(
                "confidence_score",
                response_data.get("confidence")
            )
        ),
        "severity": prediction_data.get(
            "severity",
            response_data.get("severity")
        ),
        "recommendation": prediction_data.get(
            "recommendation",
            response_data.get("recommendation")
        ),
        "created_at": get_current_timestamp()
    }

    collection = _get_predictions_collection()

    result = collection.insert_one(document)

    document["_id"] = result.inserted_id

    return serialize_prediction(document)


def get_prediction_history(
    user_id: str,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    Retrieve user prediction history.
    """

    collection = _get_predictions_collection()

    predictions = collection.find(
        {"user_id": user_id}
    ).sort(
        "created_at",
        -1
    )

    if hasattr(predictions, "limit"):
        predictions = predictions.limit(limit)

    return [
        serialize_prediction(prediction)
        for prediction in predictions
    ]


def get_prediction_by_id(
    prediction_id: str
) -> Optional[Dict[str, Any]]:
    """
    Retrieve single prediction document.
    """

    try:
        collection = _get_predictions_collection()

        prediction = collection.find_one({
            "_id": ObjectId(prediction_id)
        })

        if not prediction:
            return None

        return serialize_prediction(prediction)

    except Exception:
        return None


def serialize_prediction(
    prediction: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Convert MongoDB prediction document into API-safe response.
    """

    return {
        "id": str(prediction["_id"]),
        "user_id": prediction.get("user_id"),
        "input_data": prediction.get("input_data"),
        "model_results": prediction.get("model_results"),
        "final_prediction": prediction.get("final_prediction"),
        "prediction": prediction.get(
            "prediction",
            prediction.get("final_prediction")
        ),
        "confidence_score": prediction.get("confidence_score"),
        "confidence": prediction.get(
            "confidence",
            prediction.get("confidence_score")
        ),
        "severity": prediction.get("severity"),
        "recommendation": prediction.get("recommendation"),
        "created_at": prediction.get("created_at")
    }
