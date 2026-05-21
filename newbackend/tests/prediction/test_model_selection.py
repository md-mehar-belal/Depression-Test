import pytest

from ml.inference.ensemble_predictor import (
    run_all_models
)

from ml.preprocessing.feature_selector import (
    select_x1_features,
    select_x3_features
)


VALID_INPUT = {
    "Age": 22,
    "Gender": 1,
    "Academic Status": 3,
    "Sleep_Duration": 7,
    "Melancholic": 1,
    "Feeling_Down": 1,
    "Interest_Loss": 1,
    "Self_Perceived_Failure": 1,
    "Isolation_Frequency": 1,
    "Loneliness_Frequency": 1
}


def test_select_x1_features_returns_dictionary():
    """
    X1 selector should return dictionary.
    """

    result = select_x1_features(
        VALID_INPUT
    )

    assert isinstance(
        result,
        dict
    )


def test_select_x3_features_returns_dictionary():
    """
    X3 selector should return dictionary.
    """

    result = select_x3_features(
        VALID_INPUT
    )

    assert isinstance(
        result,
        dict
    )


def test_select_x1_features_not_empty():
    """
    X1 features should not be empty.
    """

    result = select_x1_features(
        VALID_INPUT
    )

    assert len(result) > 0


def test_select_x3_features_not_empty():
    """
    X3 features should not be empty.
    """

    result = select_x3_features(
        VALID_INPUT
    )

    assert len(result) > 0


def test_x1_feature_contains_age():
    """
    X1 feature selection should preserve Age.
    """

    result = select_x1_features(
        VALID_INPUT
    )

    assert "Age" in result


def test_x3_feature_contains_psychological_features():
    """
    X3 selection should preserve
    mental-health features.
    """

    result = select_x3_features(
        VALID_INPUT
    )

    assert "Feeling_Down" in result


def test_x3_contains_more_features_than_x1():
    """
    X3 feature set should be larger.
    """

    x1_features = select_x1_features(
        VALID_INPUT
    )

    x3_features = select_x3_features(
        VALID_INPUT
    )

    assert len(x3_features) >= len(
        x1_features
    )


def test_run_all_models_returns_dictionary():
    """
    Ensemble output should return dictionary.
    """

    result = run_all_models(
        VALID_INPUT
    )

    assert isinstance(
        result,
        dict
    )


def test_run_all_models_contains_required_keys():
    """
    Ensemble output structure validation.
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


def test_model_predictions_are_numeric():
    """
    Predictions should be numeric.
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


def test_model_confidence_scores_are_valid():
    """
    Confidence scores must stay within bounds.
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


def test_ensemble_output_exists():
    """
    Ensemble prediction should exist.
    """

    result = run_all_models(
        VALID_INPUT
    )

    assert "prediction" in result[
        "ensemble"
    ]

    assert "confidence_score" in (
        result["ensemble"]
    )


def test_ensemble_confidence_score_valid():
    """
    Ensemble confidence should stay
    within valid range.
    """

    result = run_all_models(
        VALID_INPUT
    )

    confidence = result[
        "ensemble"
    ]["confidence_score"]

    assert 0.0 <= confidence <= 1.0


def test_model_selection_handles_missing_optional_fields():
    """
    Optional features should not
    crash routing.
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


def test_model_selection_rejects_invalid_input():
    """
    Invalid payload should fail safely.
    """

    invalid_input = {
        "Age": "invalid",
        "Gender": 99
    }

    with pytest.raises(Exception):

        run_all_models(
            invalid_input
        )


def test_ensemble_contains_prediction():
    """
    Ensemble output must contain
    final prediction.
    """

    result = run_all_models(
        VALID_INPUT
    )

    assert isinstance(
        result["ensemble"]["prediction"],
        int
    )


def test_ensemble_contains_confidence_score():
    """
    Ensemble output must contain
    confidence score.
    """

    result = run_all_models(
        VALID_INPUT
    )

    assert isinstance(
        result["ensemble"][
            "confidence_score"
        ],
        float
    )


def test_model_outputs_have_consistent_structure():
    """
    All model outputs should expose
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


def test_feature_selectors_handle_empty_input():
    """
    Feature selectors should fail safely
    or return empty dictionaries.
    """

    empty_input = {}

    x1_result = select_x1_features(
        empty_input
    )

    x3_result = select_x3_features(
        empty_input
    )

    assert isinstance(
        x1_result,
        dict
    )

    assert isinstance(
        x3_result,
        dict
    )


def test_run_all_models_is_deterministic():
    """
    Same input should produce
    deterministic structure.
    """

    result_one = run_all_models(
        VALID_INPUT
    )

    result_two = run_all_models(
        VALID_INPUT
    )

    assert result_one.keys() == (
        result_two.keys()
    )