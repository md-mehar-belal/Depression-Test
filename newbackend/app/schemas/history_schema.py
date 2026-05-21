# app/schemas/history_schema.py

def serialize_prediction_history(
    history_records: list[dict]
) -> dict:
    """
    Serialize prediction history list.
    """

    serialized_records = []

    for record in history_records:

        # DUPLICATED SERIALIZATION LOGIC:
        # Repository prediction documents use final_prediction and
        # confidence_score, while this schema only read prediction and
        # confidence. That mismatch made persisted records appear empty
        # in the API history response.
        #
        # Legacy narrow field mapping:
        # "prediction": record.get("prediction")
        # "confidence": record.get("confidence", 0.0)
        confidence = record.get(
            "confidence",
            record.get("confidence_score", 0.0)
        )

        serialized_records.append({
            "id": str(record.get("id")),
            "prediction": record.get(
                "prediction",
                record.get("final_prediction")
            ),
            "confidence": round(
                confidence or 0.0,
                4
            ),
            "severity": record.get("severity"),
            "created_at": record.get("created_at")
        })

    return {
        "history": serialized_records
    }
