from collections import Counter


def calculate_confidence(
    probability: float
) -> dict:
    """
    Convert raw probability into
    confidence metadata.
    """

    if probability >= 0.90:
        level = "very_high"

    elif probability >= 0.75:
        level = "high"

    elif probability >= 0.60:
        level = "moderate"

    else:
        level = "low"

    return {
        "score": round(probability, 4),
        "level": level
    }


def calculate_agreement_strength(
    predictions: list[int]
) -> dict:
    """
    Analyze prediction agreement
    across multiple models.
    """

    total_models = len(predictions)

    # RUNTIME BUG:
    # Empty prediction lists can occur when no model artifact is loaded.
    # The previous flow immediately indexed most_common(1)[0], which
    # raises IndexError and propagates through the service layer.
    #
    # Legacy risky access:
    # most_common_prediction = prediction_counts.most_common(1)[0]
    if total_models == 0:
        return {
            "final_prediction": None,
            "agreement_ratio": 0.0,
            "agreement_strength": "no_agreement",
            "prediction_distribution": {}
        }

    prediction_counts = Counter(
        predictions
    )

    most_common_prediction = (
        prediction_counts.most_common(1)[0]
    )

    prediction_value = (
        most_common_prediction[0]
    )

    agreement_count = (
        most_common_prediction[1]
    )

    agreement_ratio = (
        agreement_count / total_models
    )

    if agreement_ratio == 1.0:
        strength = "full_agreement"

    elif agreement_ratio >= 0.75:
        strength = "strong_agreement"

    elif agreement_ratio >= 0.50:
        strength = "moderate_agreement"

    else:
        strength = "weak_agreement"

    return {
        "final_prediction": prediction_value,
        "agreement_ratio": round(
            agreement_ratio,
            4
        ),
        "agreement_strength": strength,
        "prediction_distribution": dict(
            prediction_counts
        )
    }
