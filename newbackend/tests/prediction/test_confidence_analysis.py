import pytest

from ml.inference.confidence_analyzer import (
    calculate_confidence,
    calculate_agreement_strength
)


def test_calculate_confidence_returns_float():
    """
    Confidence calculation should return float.
    """

    probabilities = [
        0.12,
        0.88
    ]

    confidence = calculate_confidence(
        probabilities
    )

    assert isinstance(
        confidence,
        float
    )


def test_calculate_confidence_within_valid_range():
    """
    Confidence must remain between 0 and 1.
    """

    probabilities = [
        0.20,
        0.80
    ]

    confidence = calculate_confidence(
        probabilities
    )

    assert 0.0 <= confidence <= 1.0


def test_calculate_confidence_high_probability():
    """
    High probability should produce
    high confidence.
    """

    probabilities = [
        0.01,
        0.99
    ]

    confidence = calculate_confidence(
        probabilities
    )

    assert confidence > 0.9


def test_calculate_confidence_low_probability():
    """
    Weak probabilities should produce
    lower confidence.
    """

    probabilities = [
        0.49,
        0.51
    ]

    confidence = calculate_confidence(
        probabilities
    )

    assert confidence < 0.7


def test_calculate_confidence_single_class_probability():
    """
    Single dominant probability handling.
    """

    probabilities = [
        1.0
    ]

    confidence = calculate_confidence(
        probabilities
    )

    assert confidence == 1.0


def test_calculate_confidence_rejects_empty_probabilities():
    """
    Empty probability input should fail safely.
    """

    with pytest.raises(Exception):

        calculate_confidence([])


def test_calculate_confidence_rejects_invalid_types():
    """
    Invalid probability types should fail.
    """

    probabilities = [
        "invalid",
        None
    ]

    with pytest.raises(Exception):

        calculate_confidence(
            probabilities
        )


def test_calculate_confidence_handles_zero_probabilities():
    """
    Zero probabilities should remain valid.
    """

    probabilities = [
        0.0,
        0.0
    ]

    confidence = calculate_confidence(
        probabilities
    )

    assert isinstance(
        confidence,
        float
    )


def test_calculate_confidence_precision():
    """
    Confidence precision consistency.
    """

    probabilities = [
        0.12345,
        0.87655
    ]

    confidence = calculate_confidence(
        probabilities
    )

    rounded = round(
        confidence,
        4
    )

    assert isinstance(
        rounded,
        float
    )


def test_calculate_confidence_is_deterministic():
    """
    Same probabilities should produce
    same confidence score.
    """

    probabilities = [
        0.25,
        0.75
    ]

    result_one = calculate_confidence(
        probabilities
    )

    result_two = calculate_confidence(
        probabilities
    )

    assert result_one == result_two


def test_calculate_agreement_strength_returns_float():
    """
    Agreement strength should return float.
    """

    predictions = [
        1,
        1,
        1
    ]

    agreement = calculate_agreement_strength(
        predictions
    )

    assert isinstance(
        agreement,
        float
    )


def test_calculate_agreement_strength_full_agreement():
    """
    All models agreeing should produce
    max agreement.
    """

    predictions = [
        1,
        1,
        1
    ]

    agreement = calculate_agreement_strength(
        predictions
    )

    assert agreement == 1.0


def test_calculate_agreement_strength_partial_agreement():
    """
    Partial agreement should reduce score.
    """

    predictions = [
        1,
        1,
        0
    ]

    agreement = calculate_agreement_strength(
        predictions
    )

    assert agreement < 1.0


def test_calculate_agreement_strength_complete_disagreement():
    """
    Strong disagreement should reduce
    agreement score.
    """

    predictions = [
        0,
        1,
        0,
        1
    ]

    agreement = calculate_agreement_strength(
        predictions
    )

    assert agreement <= 0.5


def test_calculate_agreement_strength_rejects_empty_predictions():
    """
    Empty predictions should fail safely.
    """

    with pytest.raises(Exception):

        calculate_agreement_strength(
            []
        )


def test_calculate_agreement_strength_single_prediction():
    """
    Single prediction should return
    full agreement.
    """

    predictions = [1]

    agreement = calculate_agreement_strength(
        predictions
    )

    assert agreement == 1.0


def test_calculate_agreement_strength_with_all_negative_predictions():
    """
    All negative predictions should still
    produce full agreement.
    """

    predictions = [
        0,
        0,
        0
    ]

    agreement = calculate_agreement_strength(
        predictions
    )

    assert agreement == 1.0


def test_calculate_agreement_strength_returns_valid_range():
    """
    Agreement strength should remain
    within valid range.
    """

    predictions = [
        1,
        0,
        1
    ]

    agreement = calculate_agreement_strength(
        predictions
    )

    assert 0.0 <= agreement <= 1.0


def test_calculate_agreement_strength_rejects_invalid_types():
    """
    Invalid prediction values should fail.
    """

    predictions = [
        "invalid",
        None
    ]

    with pytest.raises(Exception):

        calculate_agreement_strength(
            predictions
        )


def test_calculate_agreement_strength_is_deterministic():
    """
    Same predictions should produce
    same agreement score.
    """

    predictions = [
        1,
        1,
        0
    ]

    result_one = (
        calculate_agreement_strength(
            predictions
        )
    )

    result_two = (
        calculate_agreement_strength(
            predictions
        )
    )

    assert result_one == result_two