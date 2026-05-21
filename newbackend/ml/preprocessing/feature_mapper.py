from typing import Any

import pandas as pd


def map_features(input_data: dict[str, Any]) -> pd.DataFrame:
    """
    Convert raw request JSON into a single-row DataFrame.

    Args:
        input_data: Incoming API request payload

    Returns:
        pandas.DataFrame
    """

    return pd.DataFrame([input_data])


def align_feature_order(
    dataframe: pd.DataFrame,
    feature_order: list[str]
) -> pd.DataFrame:
    """
    Align dataframe columns to model feature order.

    Args:
        dataframe: Input feature dataframe
        feature_order: Ordered feature list used during training

    Returns:
        Ordered dataframe
    """

    missing_features = [
        feature
        for feature in feature_order
        if feature not in dataframe.columns
    ]

    if missing_features:
        raise ValueError(
            f"Missing required features: {missing_features}"
        )

    return dataframe[feature_order]