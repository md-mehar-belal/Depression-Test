# app/schemas/prediction_schema.py

def serialize_model_output(
    prediction: int,
    confidence: float,
    model_name: str
) -> dict:
    """
    Serialize raw model output.
    """

    return {
        "model": model_name,
        "prediction": prediction,
        "confidence": round(confidence, 4)
    }


def serialize_prediction_response(
    prediction: int,
    confidence_score: float,
    severity: str,
    recommendation: str | None = None,
    agreement_strength: str | None = None,
    model_results: list[dict] | dict | None = None,
    **extra_fields
) -> dict:
    """
    Serialize API prediction response.
    """

    response = {
        "prediction": prediction,
        "confidence_score": round(confidence_score, 4),
        "severity": severity
    }

    if recommendation:
        response["recommendation"] = recommendation

    # CONTRACT ISSUE:
    # prediction_service passed ensemble metadata into this serializer,
    # but the serializer accepted only prediction, confidence, severity,
    # and recommendation. That dropped service-layer inference context
    # and caused TypeError when unexpected keyword arguments were used.
    #
    # Legacy narrower serializer ended after recommendation handling.
    if agreement_strength:
        response["agreement_strength"] = agreement_strength

    if model_results is not None:
        response["model_results"] = model_results

    response.update(extra_fields)

    return response
