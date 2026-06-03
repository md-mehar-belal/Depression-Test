# app/validators/prediction_validator.py

from typing import Any
from app.constants.model_features import (
    ALL_FEATURES
)

from app.constants.model_ranges import (
    ALL_FEATURE_RANGES
)
from app.validators.type_validator import (
    validate_numeric_fields
)

from app.validators.range_validator import (
    validate_feature_ranges
)

NUMERIC_FIELDS = ALL_FEATURES


def validate_prediction_input(
    data: dict[str, Any]
) -> list[str]:
    """
    Main prediction validation pipeline.

    Validates:
    1. JSON object
    2. Required features
    3. Unknown features
    4. Numeric values
    5. Feature ranges
    """

    if not isinstance(data, dict):
        return [
            "Prediction payload must be a JSON object."
        ]

    errors = []
    errors.extend(
        validate_required_features(
            data=data,
            required_features=ALL_FEATURES
        )
    )

    errors.extend(
        validate_unknown_features(
            data=data,
            allowed_features=ALL_FEATURES
        )
    )

    errors.extend(
        validate_numeric_fields(
            data=data,
            numeric_fields=NUMERIC_FIELDS
        )
    )

    errors.extend(
        validate_feature_ranges(
            data=data,
            feature_ranges=ALL_FEATURE_RANGES
        )
    )
    return errors


def validate_required_features(
    data: dict[str, Any],
    required_features: list[str]
) -> list[str]:
    """
    Ensure all required features exist.
    """

    if not isinstance(data, dict):
        return [
            "Prediction payload must be a JSON object."
        ]
    errors = []

    for feature in required_features:

        if feature not in data:

            errors.append(
                f"Missing required feature: {feature}"
            )

    return errors


def validate_unknown_features(
    data: dict[str, Any],
    allowed_features: list[str]
) -> list[str]:
    """
    Reject unexpected fields.
    """

    allowed = set(allowed_features)

    errors = []

    for feature in data.keys():

        if feature not in allowed:

            errors.append(
                f"Unknown feature: {feature}"
            )
    return errors