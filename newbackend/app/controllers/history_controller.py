from flask import g

from app.services.logging_service import (
    log_error
)


from app.services.history_service import (
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

        current_user = getattr(
            g,
            "current_user",
            None
        )


        if not isinstance(
            current_user,
            dict
        ):

            return error_response(
                message="Authentication required",
                status_code=401
            )


        user_id = current_user.get(
            "id"
        )

        if not user_id:

            return error_response(
                message=(
                    "Invalid authentication context"
                ),
                status_code=401
            )

        history = (
            get_user_prediction_history(
                user_id=user_id,
                limit=20
            )
        )

        return success_response(
            message=(
                "Prediction history fetched "
                "successfully"
            ),
            data=history,
            status_code=200
        )

    except RuntimeError as error:

        log_error(
            "Prediction history error",
            {
                "error": str(error),
                "user_id": user_id
            }
        )

        return error_response(

            message=(
                "Failed to retrieve "
                "prediction history"
            ),
            status_code=500
        )

    except Exception as error:

        log_error(

            "Unhandled prediction history error",
            {
                "error": str(error)
            }
        )

        return error_response(
            message="Internal server error",
            status_code=500
        )