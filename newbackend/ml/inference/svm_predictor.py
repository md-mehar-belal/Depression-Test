import pandas as pd


def predict_svm(
    model,
    feature_order: list[str],
    input_data: dict
) -> int:
    """
    Generate SVM prediction.
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


def predict_svm_probability(
    model,
    feature_order: list[str],
    input_data: dict
) -> float:
    """
    Generate SVM confidence probability.
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