from typing import Optional

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def normalize_features(
    dataframe: pd.DataFrame,
    scaler: Optional[MinMaxScaler] = None
) -> tuple[pd.DataFrame, MinMaxScaler]:
    """
    Normalize features using MinMax scaling.

    Args:
        dataframe: Input dataframe
        scaler: Existing scaler instance (optional)

    Returns:
        Tuple of:
        - normalized dataframe
        - fitted scaler
    """

    if scaler is None:
        scaler = MinMaxScaler()
        scaled_values = scaler.fit_transform(dataframe)
    else:
        scaled_values = scaler.transform(dataframe)

    normalized_dataframe = pd.DataFrame(
        scaled_values,
        columns=dataframe.columns
    )

    return normalized_dataframe, scaler


def scale_features(
    dataframe: pd.DataFrame,
    scaler: MinMaxScaler
) -> pd.DataFrame:
    """
    Apply existing scaler to dataframe.

    Args:
        dataframe: Input dataframe
        scaler: Pre-fitted scaler

    Returns:
        Scaled dataframe
    """

    scaled_values = scaler.transform(dataframe)

    return pd.DataFrame(
        scaled_values,
        columns=dataframe.columns
    )