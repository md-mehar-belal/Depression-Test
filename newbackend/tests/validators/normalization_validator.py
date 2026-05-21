import math


def validate_normalized_input(
    features: dict
) -> tuple[bool, str | None]:

    for field, value in features.items():

        if isinstance(value, float):

            if math.isnan(value):
                return (
                    False,
                    f"Field '{field}' contains NaN"
                )

            if math.isinf(value):
                return (
                    False,
                    f"Field '{field}' contains infinite value"
                )

    return True, None


def validate_feature_scaling(
    features: dict,
    minimum: float = -10.0,
    maximum: float = 10.0
) -> tuple[bool, str | None]:

    for field, value in features.items():

        if not isinstance(value, (int, float)):
            continue

        if value < minimum or value > maximum:
            return (
                False,
                f"Scaled feature '{field}' out of range"
            )

    return True, None