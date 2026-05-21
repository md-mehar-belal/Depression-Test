from typing import Any


def validate_input_types(
    data: dict,
    expected_types: dict
) -> tuple[bool, str | None]:

    for field, expected_type in expected_types.items():

        if field not in data:
            continue

        value = data[field]

        if not isinstance(value, expected_type):
            return (
                False,
                f"Field '{field}' must be of type "
                f"{expected_type.__name__}"
            )

    return True, None


def validate_numeric_fields(
    data: dict,
    numeric_fields: list[str]
) -> tuple[bool, str | None]:

    for field in numeric_fields:

        if field not in data:
            continue

        value = data[field]

        if not isinstance(value, (int, float)):
            return (
                False,
                f"Field '{field}' must be numeric"
            )

    return True, None