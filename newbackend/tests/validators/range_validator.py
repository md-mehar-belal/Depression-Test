from typing import Any


def validate_feature_ranges(
    data: dict,
    feature_ranges: dict
) -> tuple[bool, str | None]:

    for field, rules in feature_ranges.items():

        if field not in data:
            continue

        value = data[field]

        # ---------------------------------
        # ENUM STYLE VALIDATION
        # Example:
        # [0, 1, 2, 3]
        # ---------------------------------

        if isinstance(rules, list):

            if value not in rules:
                return (
                    False,
                    f"Field '{field}' must be one of {rules}"
                )

        # ---------------------------------
        # MIN/MAX RANGE VALIDATION
        # Example:
        # {"min": 1, "max": 5}
        # ---------------------------------

        elif isinstance(rules, dict):

            minimum = rules.get("min")
            maximum = rules.get("max")

            if minimum is not None and value < minimum:
                return (
                    False,
                    f"Field '{field}' must be >= {minimum}"
                )

            if maximum is not None and value > maximum:
                return (
                    False,
                    f"Field '{field}' must be <= {maximum}"
                )

        else:
            return (
                False,
                f"Invalid validation rule configuration "
                f"for field '{field}'"
            )

    return True, None


def validate_score_limits(
    score: float,
    minimum: float = 0.0,
    maximum: float = 1.0
) -> tuple[bool, str |None]:

    if score < minimum or score > maximum:
        return (
            False,
            f"Score must be between "
            f"{minimum} and {maximum}"
        )

    return True, None