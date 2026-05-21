from app.validators.type_validator import (
    validate_numeric_fields
)

from app.validators.range_validator import (
    validate_feature_ranges
)

from app.validators.feature_rules import (
    CESD_X3_FEATURES,
    CESD_X3_RANGES
)


def validate_prediction_input(
    data: dict
) -> tuple[bool, str | None]:

    # ---------------------------------
    # Required Feature Validation
    # ---------------------------------

    required_valid, required_error = (
        validate_required_features(
            data=data,
            required_features=CESD_X3_FEATURES
        )
    )

    if not required_valid:
        return False, required_error

    # ---------------------------------
    # Numeric Type Validation
    # ---------------------------------

    numeric_valid, numeric_error = (
        validate_numeric_fields(
            data=data,
            numeric_fields=CESD_X3_FEATURES
        )
    )

    if not numeric_valid:
        return False, numeric_error

    # ---------------------------------
    # Feature Range Validation
    # ---------------------------------

    range_valid, range_error = (
        validate_feature_ranges(
            data=data,
            feature_ranges=CESD_X3_RANGES
        )
    )

    if not range_valid:
        return False, range_error

    return True, None


def validate_required_features(
    data: dict,
    required_features: list[str]
) -> tuple[bool, str | None]:

    missing_fields = []

    for field in required_features:

        if field not in data:
            missing_fields.append(field)

    if missing_fields:

        return (
            False,
            "Missing required features: "
            + ", ".join(missing_fields)
        )

    return True, None