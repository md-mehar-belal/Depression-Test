# app/config.py

import os
from datetime import timedelta
from dotenv import load_dotenv


load_dotenv()


class ConfigError(Exception):
    """Raised when configuration validation fails."""
    pass


def _get_env(
    key: str,
    *,
    required: bool = True,
    default=None,
    cast_type=str,
):
    """
    Safely fetch and cast environment variables.
    """

    value = os.getenv(key, default)

    if required and (value is None or str(value).strip() == ""):
        raise ConfigError(f"Missing required environment variable: {key}")

    if value is None:
        return None

    try:
        if cast_type == bool:
            return str(value).lower() in ("1", "true", "yes", "on")

        return cast_type(value)

    except (TypeError, ValueError) as exc:
        raise ConfigError(
            f"Invalid value for environment variable '{key}'"
        ) from exc


def _parse_timedelta_minutes(key: str) -> timedelta:
    """
    Parse token expiration values from minutes.
    """

    minutes = _get_env(key, cast_type=int)

    if minutes <= 0:
        raise ConfigError(
            f"{key} must be greater than 0"
        )

    return timedelta(minutes=minutes)


class BaseConfig:
    """
    Base configuration shared across all environments.
    """

    # --------------------------------------------------
    # Flask
    # --------------------------------------------------

    SECRET_KEY = _get_env("SECRET_KEY")

    DEBUG = False
    TESTING = False

    JSON_SORT_KEYS = False

    # --------------------------------------------------
    # MongoDB
    # --------------------------------------------------

    MONGO_URI = _get_env("MONGO_URI")

    DATABASE_NAME = _get_env("DATABASE_NAME")

    # --------------------------------------------------
    # JWT
    # --------------------------------------------------

    JWT_SECRET_KEY = _get_env("JWT_SECRET_KEY")

    JWT_ACCESS_TOKEN_EXPIRES = _parse_timedelta_minutes(
        "JWT_ACCESS_TOKEN_EXPIRES"
    )

    JWT_REFRESH_TOKEN_EXPIRES = _parse_timedelta_minutes(
        "JWT_REFRESH_TOKEN_EXPIRES"
    )

    JWT_TOKEN_LOCATION = ["headers"]

    JWT_HEADER_NAME = "Authorization"

    JWT_HEADER_TYPE = "Bearer"

    # --------------------------------------------------
    # Google OAuth
    # --------------------------------------------------

    GOOGLE_CLIENT_ID = _get_env(
        "GOOGLE_CLIENT_ID",
        required=False,
    )

    GOOGLE_CLIENT_SECRET = _get_env(
        "GOOGLE_CLIENT_SECRET",
        required=False,
    )

    # --------------------------------------------------
    # SMTP / Mail
    # --------------------------------------------------

    SMTP_HOST = _get_env(
        "SMTP_HOST",
        required=False,
    )

    SMTP_PORT = _get_env(
        "SMTP_PORT",
        required=False,
        cast_type=int,
    )

    SMTP_USERNAME = _get_env(
        "SMTP_USERNAME",
        required=False,
    )

    SMTP_PASSWORD = _get_env(
        "SMTP_PASSWORD",
        required=False,
    )

    MAIL_FROM = _get_env(
        "MAIL_FROM",
        required=False,
    )

    # --------------------------------------------------
    # Security
    # --------------------------------------------------

    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SECURE = True

    # --------------------------------------------------
    # Rate Limiting
    # --------------------------------------------------

    RATE_LIMIT_ENABLED = _get_env(
        "RATE_LIMIT_ENABLED",
        required=False,
        default="true",
        cast_type=bool,
    )

    RATE_LIMIT_PER_MINUTE = _get_env(
        "RATE_LIMIT_PER_MINUTE",
        required=False,
        default=60,
        cast_type=int,
    )

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    LOG_LEVEL = _get_env(
        "LOG_LEVEL",
        required=False,
        default="INFO",
    )

    # --------------------------------------------------
    # ML
    # --------------------------------------------------

    ML_MODELS_PATH = _get_env(
        "ML_MODELS_PATH",
        required=False,
        default="ml/models",
    )

    FEATURE_ORDER_PATH = _get_env(
        "FEATURE_ORDER_PATH",
        required=False,
        default="ml/artifacts/feature_order.json",
    )

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    @classmethod
    def validate(cls):
        """
        Validate critical production settings.
        """

        if cls.DEBUG and os.getenv("FLASK_ENV") == "production":
            raise ConfigError(
                "DEBUG cannot be enabled in production"
            )

        if len(cls.JWT_SECRET_KEY) < 32:
            raise ConfigError(
                "JWT_SECRET_KEY must be at least 32 characters long"
            )

        if len(cls.SECRET_KEY) < 32:
            raise ConfigError(
                "SECRET_KEY must be at least 32 characters long"
            )

        if not cls.MONGO_URI.startswith("mongodb://") and not cls.MONGO_URI.startswith("mongodb+srv://"):
            raise ConfigError(
                "Invalid MongoDB connection URI"
            )

        return True


class DevelopmentConfig(BaseConfig):

    DEBUG = True

    SESSION_COOKIE_SECURE = False


class TestingConfig(BaseConfig):

    TESTING = True

    DEBUG = False

    MONGO_URI = os.getenv(
        "TEST_MONGO_URI",
        "mongodb://localhost:27017"
    )

    DATABASE_NAME = os.getenv(
        "TEST_DATABASE_NAME",
        "test_db"
    )

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)

    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=10)

    SESSION_COOKIE_SECURE = False


class ProductionConfig(BaseConfig):

    DEBUG = False

    TESTING = False

    SESSION_COOKIE_SECURE = True


def load_config():
    """
    Load configuration class based on FLASK_ENV.
    """

    env = os.getenv("FLASK_ENV", "development").lower()

    config_mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }

    config_class = config_mapping.get(env)

    if not config_class:
        raise ConfigError(
            f"Invalid FLASK_ENV value: {env}"
        )

    config_class.validate()

    return config_class