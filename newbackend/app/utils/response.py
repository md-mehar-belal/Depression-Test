from flask import jsonify

def success_response(
    message: str,
    data=None,
    status_code: int = 200
):
    response = {
        "success": True,
        "message": message,
        "data": data
    }
    return jsonify(response), status_code


def error_response(
    message: str,
    status_code: int = 400,
    errors=None
):
    response = {
        "success": False,
        "message": message,
        "errors": errors
    }
    return jsonify(response), status_code