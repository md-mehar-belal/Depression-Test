from flask import Blueprint

from app.controllers.prediction_controller import (
    predict_controller
)

prediction_blueprint = Blueprint(
    "prediction_blueprint",
    __name__
)


@prediction_blueprint.route("/predict", methods=["POST"])
def predict():
    return predict_controller()


def register_prediction_routes(app):
    app.register_blueprint(prediction_blueprint)