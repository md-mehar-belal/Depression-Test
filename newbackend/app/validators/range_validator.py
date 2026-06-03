# app/validators/range_validator.py

def validate_feature_ranges(
    data: dict,
    feature_ranges: dict
) -> list[str]:
    errors = []

    for field, rule in feature_ranges.items():

        if field not in data:
            continue

        value = data[field]

        if not isinstance(value, (int, float)):
            continue

        #
        # Allowed values
        #
        if isinstance(rule, list):

            if value not in rule:

                errors.append(
                    f"{field} must be one of {rule}"
                )

            continue

        #
        # Dictionary range
        #
        if isinstance(rule, dict):

            min_value = rule["min"]
            max_value = rule["max"]

            if value < min_value or value > max_value:

                errors.append(
                    f"{field} must be between "
                    f"{min_value} and {max_value}"
                )

            continue

        #
        # Tuple range (backward compatibility)
        #
        if isinstance(rule, tuple):

            min_value, max_value = rule

            if value < min_value or value > max_value:

                errors.append(
                    f"{field} must be between "
                    f"{min_value} and {max_value}"
                )
    return errors