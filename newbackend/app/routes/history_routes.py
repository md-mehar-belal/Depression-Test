from flask import Blueprint

from app.controllers.history_controller import (
    get_prediction_history_controller
)

history_blueprint = Blueprint(
    "history_blueprint",
    __name__,
    url_prefix="/predictions"
)


@history_blueprint.route("/history", methods=["GET"])
def get_prediction_history():
    return get_prediction_history_controller()


def register_history_routes(app):
    app.register_blueprint(history_blueprint)