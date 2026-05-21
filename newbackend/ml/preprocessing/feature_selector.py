import pandas as pd


# Example feature groups
# Update these lists to match your actual trained model exports.

X1_FEATURES = [
    "Age",
    "Gender",
    "Sleep_Duration",
    "Social_Media_Hours",
    "Financial_Pressure"
]


X3_FEATURES = [
    "Age",
    "Gender",
    "Sleep_Duration",
    "Social_Media_Hours",
    "Financial_Pressure",
    "Melancholic",
    "Future_Hopelessness",
    "Interest_Loss",
    "Fatigue_Frequency",
    "Loneliness_Frequency"
]


def select_x1_features(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Select lightweight feature subset.

    Args:
        dataframe: Full feature dataframe

    Returns:
        Filtered dataframe
    """

    return dataframe[X1_FEATURES]


def select_x3_features(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Select extended feature subset.

    Args:
        dataframe: Full feature dataframe

    Returns:
        Filtered dataframe
    """

    return dataframe[X3_FEATURES]