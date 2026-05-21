from flask import g

from app.services.prediction_service import (
    get_user_prediction_history
)

from app.utils.response import (
    success_response,
    error_response
)


def get_prediction_history_controller():
    """
    Return authenticated user's
    prediction history.
    """

    try:
        current_user = getattr(g, "current_user", None)

        if not current_user:

            return error_response(
                message="Authentication required",
                status_code=401
            )

        # ARCHITECTURAL VIOLATION:
        # The controller previously imported the prediction repository
        # and serialized persistence data itself. That bypassed the
        # service/use-case boundary and coupled HTTP handling to the
        # database layer.
        #
        # Legacy problematic flow:
        # history_records = get_prediction_history(current_user["id"])
        # serialized_history = serialize_prediction_history(history_records)
        serialized_history = get_user_prediction_history(
            current_user["id"]
        )

        return success_response(
            message="Prediction history fetched successfully",
            data=serialized_history,
            status_code=200
        )

    except Exception as error:

        return error_response(
            message=str(error),
            status_code=500
        )
