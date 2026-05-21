import pytest

from ml.inference.ensemble_predictor import (
    aggregate_predictions,
    generate_ensemble_output,
    run_all_models
)


MODEL_OUTPUTS = {
    "svm": {
        "prediction": 1,
        "confidence_score": 0.82
    },
    "logistic": {
        "prediction": 1,
        "confidence_score": 0.79
    },
    "randomforest": {
        "prediction": 0,
        "confidence_score": 0.71
    }
}


VALID_INPUT = {
    "Age": 22,
    "Gender": 1,
    "Sleep_Duration": 7,
    "Feeling_Down": 1,
    "Interest_Loss": 1,
    "Melancholic": 1
}


def test_aggregate_predictions_returns_dictionary():
    """
    Aggregation should return dictionary.
    """

    result = aggregate_predictions(
        MODEL_OUTPUTS
    )

    assert isinstance(
        result,
        dict
    )


def test_aggregate_predictions_contains_required_fields():
    """
    Ensemble response structure validation.
    """

    result = aggregate_predictions(
        MODEL_OUTPUTS
    )

    expected_fields = {
        "prediction",
        "confidence_score"
    }

    assert expected_fields.issubset(
        result.keys()
    )


def test_aggregate_predictions_prediction_type():
    """
    Ensemble prediction should be integer.
    """

    result = aggregate_predictions(
        MODEL_OUTPUTS
    )

    assert isinstance(
        result["prediction"],
        int
    )


def test_aggregate_predictions_confidence_type():
    """
    Ensemble confidence should be float.
    """

    result = aggregate_predictions(
        MODEL_OUTPUTS
    )

    assert isinstance(
        result["confidence_score"],
        float
    )


def test_aggregate_predictions_confidence_range():
    """
    Ensemble confidence must stay
    between 0 and 1.
    """

    result = aggregate_predictions(
        MODEL_OUTPUTS
    )

    confidence = result[
        "confidence_score"
    ]

    assert 0.0 <= confidence <= 1.0


def test_majority_vote_behavior():
    """
    Majority vote should determine output.
    """

    result = aggregate_predictions(
        MODEL_OUTPUTS
    )

    assert result["prediction"] == 1


def test_generate_ensemble_output_returns_dictionary():
    """
    Ensemble generator should return dictionary.
    """

    aggregated = aggregate_predictions(
        MODEL_OUTPUTS
    )

    result = generate_ensemble_output(
        aggregated
    )

    assert isinstance(
        result,
        dict
    )


def test_generate_ensemble_output_contains_metadata():
    """
    Ensemble output should contain metadata.
    """

    aggregated = aggregate_predictions(
        MODEL_OUTPUTS
    )

    result = generate_ensemble_output(
        aggregated
    )

    expected_fields = {
        "prediction",
        "confidence_score",
        "severity",
        "model_used"
    }

    assert expected_fields.issubset(
        result.keys()
    )


def test_generate_ensemble_output_severity_type():
    """
    Severity label should be string.
    """

    aggregated = aggregate_predictions(
        MODEL_OUTPUTS
    )

    result = generate_ensemble_output(
        aggregated
    )

    assert isinstance(
        result["severity"],
        str
    )


def test_generate_ensemble_output_model_used_type():
    """
    model_used should be string.
    """

    aggregated = aggregate_predictions(
        MODEL_OUTPUTS
    )

    result = generate_ensemble_output(
        aggregated
    )

    assert isinstance(
        result["model_used"],
        str
    )


def test_generate_ensemble_output_prediction_type():
    """
    Final prediction should be integer.
    """

    aggregated = aggregate_predictions(
        MODEL_OUTPUTS
    )

    result = generate_ensemble_output(
        aggregated
    )

    assert isinstance(
        result["prediction"],
        int
    )


def test_generate_ensemble_output_confidence_type():
    """
    Final confidence should be float.
    """

    aggregated = aggregate_predictions(
        MODEL_OUTPUTS
    )

    result = generate_ensemble_output(
        aggregated
    )

    assert isinstance(
        result["confidence_score"],
        float
    )


def test_run_all_models_returns_complete_output():
    """
    Full orchestration should return
    all model outputs.
    """

    result = run_all_models(
        VALID_INPUT
    )

    expected_keys = {
        "svm",
        "logistic",
        "randomforest",
        "ensemble"
    }

    assert expected_keys.issubset(
        result.keys()
    )


def test_run_all_models_ensemble_structure():
    """
    Ensemble result should contain
    expected schema.
    """

    result = run_all_models(
        VALID_INPUT
    )

    ensemble = result["ensemble"]

    expected_fields = {
        "prediction",
        "confidence_score"
    }

    assert expected_fields.issubset(
        ensemble.keys()
    )


def test_run_all_models_model_structure():
    """
    Each model output should contain
    prediction and confidence score.
    """

    result = run_all_models(
        VALID_INPUT
    )

    for model_name in [
        "svm",
        "logistic",
        "randomforest"
    ]:

        assert "prediction" in result[
            model_name
        ]

        assert "confidence_score" in (
            result[model_name]
        )


def test_run_all_models_prediction_types():
    """
    Model predictions should be integers.
    """

    result = run_all_models(
        VALID_INPUT
    )

    assert isinstance(
        result["svm"]["prediction"],
        int
    )

    assert isinstance(
        result["logistic"]["prediction"],
        int
    )

    assert isinstance(
        result["randomforest"]["prediction"],
        int
    )


def test_run_all_models_confidence_ranges():
    """
    All confidence scores must remain valid.
    """

    result = run_all_models(
        VALID_INPUT
    )

    for model_name in [
        "svm",
        "logistic",
        "randomforest"
    ]:

        confidence = result[
            model_name
        ]["confidence_score"]

        assert 0.0 <= confidence <= 1.0


def test_run_all_models_ensemble_confidence_range():
    """
    Ensemble confidence must remain valid.
    """

    result = run_all_models(
        VALID_INPUT
    )

    confidence = result[
        "ensemble"
    ]["confidence_score"]

    assert 0.0 <= confidence <= 1.0


def test_aggregate_predictions_rejects_empty_input():
    """
    Empty model outputs should fail safely.
    """

    with pytest.raises(Exception):

        aggregate_predictions({})


def test_aggregate_predictions_single_model():
    """
    Single model prediction should
    still aggregate correctly.
    """

    single_model = {
        "svm": {
            "prediction": 1,
            "confidence_score": 0.91
        }
    }

    result = aggregate_predictions(
        single_model
    )

    assert result["prediction"] == 1

    assert (
        result["confidence_score"]
        == 0.91
    )


def test_aggregate_predictions_complete_disagreement():
    """
    Ensemble should safely handle
    complete disagreement.
    """

    disagreement_outputs = {
        "svm": {
            "prediction": 0,
            "confidence_score": 0.90
        },
        "logistic": {
            "prediction": 1,
            "confidence_score": 0.88
        },
        "randomforest": {
            "prediction": 2,
            "confidence_score": 0.86
        }
    }

    result = aggregate_predictions(
        disagreement_outputs
    )

    assert "prediction" in result

    assert "confidence_score" in (
        result
    )


def test_aggregate_predictions_is_deterministic():
    """
    Same model outputs should produce
    deterministic ensemble results.
    """

    result_one = aggregate_predictions(
        MODEL_OUTPUTS
    )

    result_two = aggregate_predictions(
        MODEL_OUTPUTS
    )

    assert result_one == result_two


def test_run_all_models_handles_partial_input():
    """
    Partial input should not crash
    orchestration layer.
    """

    partial_input = {
        "Age": 22,
        "Gender": 1,
        "Feeling_Down": 1
    }

    result = run_all_models(
        partial_input
    )

    assert isinstance(
        result,
        dict
    )


def test_run_all_models_rejects_invalid_input():
    """
    Invalid payload should fail safely.
    """

    invalid_input = {
        "Age": "invalid",
        "Gender": None
    }

    with pytest.raises(Exception):

        run_all_models(
            invalid_input
        )