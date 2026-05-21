from ml.inference.model_loader import (
    get_model,
    get_feature_order
)

from ml.inference.svm_predictor import (
    predict_svm,
    predict_svm_probability
)

from ml.inference.logistic_predictor import (
    predict_logistic,
    predict_logistic_probability
)

from ml.inference.randomforest_predictor import (
    predict_randomforest,
    predict_randomforest_probability
)

from ml.inference.confidence_analyzer import (
    calculate_confidence,
    calculate_agreement_strength
)


SUPPORTED_MODELS = {
    "svm": {
        "predict": predict_svm,
        "probability": (
            predict_svm_probability
        )
    },

    "logistic_regression": {
        "predict": predict_logistic,
        "probability": (
            predict_logistic_probability
        )
    },

    "random_forest": {
        "predict": predict_randomforest,
        "probability": (
            predict_randomforest_probability
        )
    }
}


def run_all_models(
    input_data: dict,
    feature_set: str,
    test_type: str,
    model_types: list[str]
) -> list[dict]:
    """
    Run multiple models against
    the same input payload.
    """

    results = []

    feature_order = get_feature_order(
        feature_set=feature_set,
        test_type=test_type
    )

    if not feature_order:
        return []

    for model_type in model_types:

        model = get_model(
            model_type=model_type,
            feature_set=feature_set,
            test_type=test_type
        )

        if not model:
            continue

        if model_type not in SUPPORTED_MODELS:
            continue

        predictor = (
            SUPPORTED_MODELS[model_type]
        )

        prediction = predictor[
            "predict"
        ](
            model=model,
            feature_order=feature_order,
            input_data=input_data
        )

        probability = predictor[
            "probability"
        ](
            model=model,
            feature_order=feature_order,
            input_data=input_data
        )

        confidence = calculate_confidence(
            probability
        )

        results.append({
            "model_type": model_type,
            "prediction": prediction,
            "confidence": confidence
        })

    return results


def aggregate_predictions(
    model_results: list[dict]
) -> dict:
    """
    Aggregate prediction outputs.
    """

    predictions = [
        result["prediction"]
        for result in model_results
    ]

    confidence_scores = [
        result["confidence"]["score"]
        for result in model_results
    ]

    agreement = (
        calculate_agreement_strength(
            predictions
        )
    )

    # RUNTIME BUG:
    # Aggregation divided by the number of confidence scores without
    # guarding the no-models case. Missing model artifacts or unsupported
    # model_types could therefore crash the service layer.
    #
    # Legacy risky calculation:
    # average_confidence = sum(confidence_scores) / len(confidence_scores)
    average_confidence = (
        sum(confidence_scores)
        / len(confidence_scores)
        if confidence_scores
        else 0.0
    )

    return {
        "final_prediction": agreement[
            "final_prediction"
        ],

        "agreement_strength": agreement[
            "agreement_strength"
        ],

        "agreement_ratio": agreement[
            "agreement_ratio"
        ],

        "prediction_distribution": agreement[
            "prediction_distribution"
        ],

        "average_confidence": round(
            average_confidence,
            4
        )
    }


def generate_ensemble_output(
    input_data: dict,
    feature_set: str,
    test_type: str,
    model_types: list[str]
) -> dict:
    """
    Complete ensemble prediction flow.
    """

    model_results = run_all_models(
        input_data=input_data,
        feature_set=feature_set,
        test_type=test_type,
        model_types=model_types
    )

    aggregated_result = (
        aggregate_predictions(
            model_results
        )
    )

    return {
        "individual_models": model_results,
        "ensemble_result": aggregated_result
    }
