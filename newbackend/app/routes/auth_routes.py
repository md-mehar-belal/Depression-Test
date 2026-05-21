from flask import Blueprint

from app.controllers.auth_controller import (
    signup_controller,
    login_controller,
    google_login_controller,
    google_callback_controller,
    forgot_password_controller,
    reset_password_controller,
    verify_email_controller,
    get_current_user_controller,
    logout_controller
)

auth_blueprint = Blueprint(
    "auth_blueprint",
    __name__,
    url_prefix="/auth"
)


@auth_blueprint.route("/signup", methods=["POST"])
def signup():
    return signup_controller()


@auth_blueprint.route("/login", methods=["POST"])
def login():
    return login_controller()


@auth_blueprint.route("/google", methods=["GET"])
def google_login():
    return google_login_controller()


@auth_blueprint.route("/google/callback", methods=["POST"])
def google_callback():
    return google_callback_controller()


@auth_blueprint.route("/forgot-password", methods=["POST"])
def forgot_password():
    return forgot_password_controller()


@auth_blueprint.route("/reset-password", methods=["POST"])
def reset_password():
    return reset_password_controller()


@auth_blueprint.route("/verify-email", methods=["POST"])
def verify_email():
    return verify_email_controller()


@auth_blueprint.route("/me", methods=["GET"])
def get_current_user():
    return get_current_user_controller()


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    return logout_controller()


def register_auth_routes(app):
    app.register_blueprint(auth_blueprint)