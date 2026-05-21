# app/validators/prediction_validator.py

from app.validators.type_validator import (
    validate_numeric_fields
)

from app.validators.range_validator import (
    validate_feature_ranges
)


REQUIRED_FEATURES = [
    "Age",
    "Sleep_Duration",
    "Social_Media_Hours",
    "Financial_Pressure"
]


FEATURE_RANGES = {
    "Age": (10, 100),
    "Sleep_Duration": (0, 24),
    "Social_Media_Hours": (0, 24),
    "Financial_Pressure": (0, 10)
}


NUMERIC_FIELDS = [
    "Age",
    "Sleep_Duration",
    "Social_Media_Hours",
    "Financial_Pressure"
]


def validate_prediction_input(
    data: dict
) -> list[str]:
    """
    Main prediction validation pipeline.
    """

    errors = []

    required_errors = validate_required_features(data)

    if required_errors:
        errors.extend(required_errors)

    numeric_errors = validate_numeric_fields(
        data=data,
        numeric_fields=NUMERIC_FIELDS
    )

    errors.extend(numeric_errors)

    range_errors = validate_feature_ranges(
        data=data,
        feature_ranges=FEATURE_RANGES
    )

    errors.extend(range_errors)

    return errors


def validate_required_features(
    data: dict
) -> list[str]:
    """
    Ensure required ML features exist.
    """

    errors = []

    for feature in REQUIRED_FEATURES:

        if feature not in data:
            errors.append(
                f"Missing required feature: {feature}"
            )

    return errors