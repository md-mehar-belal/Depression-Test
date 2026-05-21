from unittest.mock import Mock


MOCK_SVM_PREDICTION = 1

MOCK_SVM_PROBABILITY = 0.84


MOCK_LOGISTIC_PREDICTION = 1

MOCK_LOGISTIC_PROBABILITY = 0.79


MOCK_RANDOMFOREST_PREDICTION = 0

MOCK_RANDOMFOREST_PROBABILITY = 0.61


MOCK_ENSEMBLE_RESULT = {
    "final_prediction": 1,
    "confidence_score": 0.81,
    "agreement_strength": 0.67
}


MOCK_HIGH_CONFIDENCE_RESULT = {
    "prediction": 1,
    "confidence_score": 0.94,
    "confidence_level": "high"
}


MOCK_MEDIUM_CONFIDENCE_RESULT = {
    "prediction": 1,
    "confidence_score": 0.68,
    "confidence_level": "medium"
}


MOCK_LOW_CONFIDENCE_RESULT = {
    "prediction": 1,
    "confidence_score": 0.41,
    "confidence_level": "low"
}


MOCK_MODEL_RESPONSE = {
    "prediction": 1,
    "probability": 0.87
}


MOCK_MODEL_ERROR_RESPONSE = {
    "error": "Model inference failed"
}


def create_mock_svm_model():

    mock_model = Mock()

    mock_model.predict.return_value = [
        MOCK_SVM_PREDICTION
    ]

    mock_model.predict_proba.return_value = [
        [
            1 - MOCK_SVM_PROBABILITY,
            MOCK_SVM_PROBABILITY
        ]
    ]

    return mock_model


def create_mock_logistic_model():

    mock_model = Mock()

    mock_model.predict.return_value = [
        MOCK_LOGISTIC_PREDICTION
    ]

    mock_model.predict_proba.return_value = [
        [
            1 - MOCK_LOGISTIC_PROBABILITY,
            MOCK_LOGISTIC_PROBABILITY
        ]
    ]

    return mock_model


def create_mock_randomforest_model():

    mock_model = Mock()

    mock_model.predict.return_value = [
        MOCK_RANDOMFOREST_PREDICTION
    ]

    mock_model.predict_proba.return_value = [
        [
            1 - MOCK_RANDOMFOREST_PROBABILITY,
            MOCK_RANDOMFOREST_PROBABILITY
        ]
    ]

    return mock_model


def create_failing_model():

    mock_model = Mock()

    mock_model.predict.side_effect = (
        Exception("Prediction failure")
    )

    return mock_model


MOCK_FEATURE_ORDER = [
    "Age",
    "Gender",
    "Feeling_Down",
    "Interest_Loss",
    "Sleep_Duration"
]


MOCK_FEATURE_VECTOR = [
    22,
    1,
    1,
    1,
    7
]


MOCK_MODEL_INPUT_FRAME = {
    "Age": 22,
    "Gender": 1,
    "Feeling_Down": 1,
    "Interest_Loss": 1,
    "Sleep_Duration": 7
}