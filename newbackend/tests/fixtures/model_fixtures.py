import numpy as np

from fixtures.prediction_payloads import (
    HIGH_RISK_PREDICTION_PAYLOAD,
    LOW_RISK_PREDICTION_PAYLOAD,
    VALID_PREDICTION_PAYLOAD
)


MOCK_MODEL_PREDICTION = np.array([1])

MOCK_MODEL_PROBABILITIES = np.array([
    [0.12, 0.88]
])

MOCK_LOW_RISK_PREDICTION = np.array([0])

MOCK_LOW_RISK_PROBABILITIES = np.array([
    [0.91, 0.09]
])

MOCK_HIGH_RISK_PREDICTION = np.array([1])

MOCK_HIGH_RISK_PROBABILITIES = np.array([
    [0.03, 0.97]
])


MOCK_MODEL_RESPONSE = {
    "prediction": 1,
    "confidence_score": 0.88,
    "mental_health_tip": (
        "Take regular rest, stay connected with "
        "trusted people, and seek support when needed."
    )
}


MOCK_LOW_RISK_RESPONSE = {
    "prediction": 0,
    "confidence_score": 0.91,
    "mental_health_tip": (
        "Maintain healthy routines, balanced sleep, "
        "and regular physical activity."
    )
}


MOCK_HIGH_RISK_RESPONSE = {
    "prediction": 1,
    "confidence_score": 0.97,
    "mental_health_tip": (
        "Please consider reaching out to a trusted "
        "person or mental health professional for support."
    )
}


MOCK_FEATURE_ORDER = list(
    VALID_PREDICTION_PAYLOAD.keys()
)


MOCK_MODEL_INPUT_DATAFRAME = [
    list(VALID_PREDICTION_PAYLOAD.values())
]


MOCK_LOW_RISK_INPUT_DATAFRAME = [
    list(LOW_RISK_PREDICTION_PAYLOAD.values())
]


MOCK_HIGH_RISK_INPUT_DATAFRAME = [
    list(HIGH_RISK_PREDICTION_PAYLOAD.values())
]