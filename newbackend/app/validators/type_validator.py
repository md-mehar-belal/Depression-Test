# app/validators/type_validator.py

from typing import Any


def validate_input_types(
    data: dict,
    expected_types: dict
) -> list[str]:
    """
    Validate field datatypes.

    Args:
        data: Incoming request payload
        expected_types: Mapping of field -> expected type

    Returns:
        List of validation errors
    """

    errors = []

    for field, expected_type in expected_types.items():

        if field not in data:
            continue

        value = data[field]

        if not isinstance(value, expected_type):

            expected_name = (
                expected_type.__name__
                if hasattr(expected_type, "__name__")
                else str(expected_type)
            )

            actual_name = type(value).__name__

            errors.append(
                f"{field} must be of type "
                f"{expected_name}, got {actual_name}"
            )

    return errors


def validate_numeric_fields(
    data: dict,
    numeric_fields: list[str]
) -> list[str]:
    """
    Ensure fields contain numeric values.

    Accepts:
    - int
    - float

    Rejects:
    - bool
    - str
    - None
    """

    errors = []

    for field in numeric_fields:

        if field not in data:
            continue

        value = data[field]

        if isinstance(value, bool):
            errors.append(f"{field} must be numeric")
            continue

        if not isinstance(value, (int, float)):
            errors.append(f"{field} must be numeric")

    return errors