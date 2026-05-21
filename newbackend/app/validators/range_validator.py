# app/validators/range_validator.py

def validate_feature_ranges(
    data: dict,
    feature_ranges: dict
) -> list[str]:
    """
    Validate numeric ranges for features.

    Args:
        data: Request payload
        feature_ranges:
            {
                "Age": (10, 100),
                "Sleep_Duration": (0, 24)
            }

    Returns:
        List of validation errors
    """

    errors = []

    for field, limits in feature_ranges.items():

        if field not in data:
            continue

        value = data[field]

        if not isinstance(value, (int, float)):
            continue

        min_value, max_value = limits

        if value < min_value or value > max_value:

            errors.append(
                f"{field} must be between "
                f"{min_value} and {max_value}"
            )

    return errors


def validate_score_limits(
    score: float,
    min_score: float = 0.0,
    max_score: float = 1.0
) -> list[str]:
    """
    Validate confidence/probability score boundaries.
    """

    errors = []

    if score < min_score or score > max_score:

        errors.append(
            f"Score must be between "
            f"{min_score} and {max_score}"
        )

    return errors