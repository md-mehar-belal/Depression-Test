from flask import Flask

from app.config import load_config

# Route registration
from app.routes.auth_routes import register_auth_routes
from app.routes.prediction_routes import register_prediction_routes
from app.routes.history_routes import register_history_routes

# Middleware
from app.middleware.logging_middleware import (
    log_request_middleware,
    log_response_middleware
)
from app.middleware.security_middleware import (
    sanitize_request,
    apply_security_headers
)
from app.middleware.auth_middleware import authenticate_request
from app.middleware.rate_limit_middleware import rate_limit_middleware

# Error handlers
from app.middleware.error_middleware import (
    handle_validation_error,
    handle_auth_error,
    handle_server_error
)

# Database
from app.database.database import (
    connect_database,
    close_database
)

# ML initialization
from ml.inference.model_loader import initialize_ml_models


def create_app() -> Flask:
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(load_config())

    # Initialize database connection
    with app.app_context():
        connect_database()

    # Initialize ML models
    with app.app_context():
        initialize_ml_models()

    # =========================
    # BEFORE REQUEST MIDDLEWARE
    # =========================

    app.before_request(log_request_middleware)
    app.before_request(sanitize_request)
    app.before_request(rate_limit_middleware)
    app.before_request(authenticate_request)

    # =========================
    # AFTER REQUEST MIDDLEWARE
    # =========================

    app.after_request(log_response_middleware)
    app.after_request(apply_security_headers)

    # =========================
    # ERROR HANDLERS
    # =========================

    app.register_error_handler(ValueError, handle_validation_error)
    app.register_error_handler(PermissionError, handle_auth_error)
    app.register_error_handler(Exception, handle_server_error)

    # =========================
    # ROUTES
    # =========================

    register_auth_routes(app)
    register_prediction_routes(app)
    register_history_routes(app)

    # Graceful DB cleanup
    @app.teardown_appcontext
    def shutdown_db(exception=None):
        close_database()

    return app