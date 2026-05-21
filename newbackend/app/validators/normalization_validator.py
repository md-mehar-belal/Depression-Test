# app/validators/normalization_validator.py

import math


def validate_normalized_input(
    normalized_data: dict
) -> list[str]:
    """
    Validate normalized feature values.
    """

    errors = []

    for field, value in normalized_data.items():

        if not isinstance(value, (int, float)):
            errors.append(
                f"{field} contains invalid normalized value"
            )
            continue

        if math.isnan(value):
            errors.append(
                f"{field} contains NaN value"
            )

        if math.isinf(value):
            errors.append(
                f"{field} contains infinite value"
            )

    return errors


def validate_feature_scaling(
    normalized_data: dict,
    min_allowed: float = -10.0,
    max_allowed: float = 10.0
) -> list[str]:
    """
    Validate scaled feature boundaries.
    """

    errors = []

    for field, value in normalized_data.items():

        if not isinstance(value, (int, float)):
            continue

        if value < min_allowed or value > max_allowed:

            errors.append(
                f"{field} scaled value out of bounds"
            )

    return errors