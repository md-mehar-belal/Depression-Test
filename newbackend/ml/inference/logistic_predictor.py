import pandas as pd


def predict_logistic(
    model,
    feature_order: list[str],
    input_data: dict
) -> int:
    """
    Generate Logistic Regression prediction.
    """

    ordered_features = [
        input_data[feature]
        for feature in feature_order
    ]

    dataframe = pd.DataFrame(
        [ordered_features],
        columns=feature_order
    )

    prediction = model.predict(dataframe)[0]

    return int(prediction)


def predict_logistic_probability(
    model,
    feature_order: list[str],
    input_data: dict
) -> float:
    """
    Generate Logistic Regression confidence.
    """

    ordered_features = [
        input_data[feature]
        for feature in feature_order
    ]

    dataframe = pd.DataFrame(
        [ordered_features],
        columns=feature_order
    )

    probability = (
        model.predict_proba(dataframe).max()
    )

    return float(probability)