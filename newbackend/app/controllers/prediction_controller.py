from flask import g, request

from app.services.prediction_service import (
    generate_prediction
)

from app.utils.response import (
    success_response,
    error_response
)

def predict_controller():
    """
    Handle ML prediction requests.
    """

    try:
        request_data = request.get_json() or {}

        current_user = getattr(g, "current_user", None)

        # ARCHITECTURAL VIOLATION:
        # The controller previously performed validation and history
        # persistence orchestration. That placed business workflow logic
        # in the HTTP layer and duplicated service responsibilities.
        #
        # Legacy problematic flow:
        # validation_result = validate_prediction_input(request_data)
        # prediction_response = generate_prediction(request_data)
        # save_prediction_history(...)
        prediction_response = generate_prediction(
            input_data=request_data,
            user_id=current_user["id"] if current_user else None,
            persist_history=bool(current_user),
            validate_input=True
        )

        if prediction_response.get("success") is False:
            return error_response(
                message=prediction_response["message"],
                errors=prediction_response.get("errors"),
                status_code=400
            )

        return success_response(
            message="Prediction generated successfully",
            data=prediction_response,
            status_code=200
        )

    except Exception as error:

        return error_response(
            message=str(error),
            status_code=500
        )
