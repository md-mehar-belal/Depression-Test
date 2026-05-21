import pytest

from ml.inference.confidence_analyzer import (
    calculate_agreement_strength,
    calculate_confidence
)


def test_calculate_confidence_returns_float():

    confidence = calculate_confidence(
        [0.91, 0.88, 0.95]
    )

    assert isinstance(
        confidence,
        float
    )


def test_calculate_confidence_returns_expected_average():

    confidence = calculate_confidence(
        [0.90, 0.80, 1.00]
    )

    assert confidence == 0.90


def test_calculate_confidence_handles_single_value():

    confidence = calculate_confidence(
        [0.97]
    )

    assert confidence == 0.97


def test_calculate_confidence_handles_zero_values():

    confidence = calculate_confidence(
        [0.0, 0.0, 0.0]
    )

    assert confidence == 0.0


def test_calculate_confidence_handles_high_confidence():

    confidence = calculate_confidence(
        [0.99, 0.98, 0.97]
    )

    assert confidence >= 0.97


def test_calculate_confidence_raises_error_on_empty_list():

    with pytest.raises(
        (ValueError, ZeroDivisionError)
    ):

        calculate_confidence([])


def test_calculate_agreement_strength_returns_string():

    agreement = calculate_agreement_strength(
        [1, 1, 1]
    )

    assert isinstance(
        agreement,
        str
    )


def test_calculate_agreement_strength_detects_strong_agreement():

    agreement = calculate_agreement_strength(
        [1, 1, 1]
    )

    assert agreement.lower() in [
        "strong",
        "high",
        "strong agreement",
        "high agreement"
    ]


def test_calculate_agreement_strength_detects_partial_agreement():

    agreement = calculate_agreement_strength(
        [1, 1, 0]
    )

    assert agreement.lower() in [
        "moderate",
        "partial",
        "moderate agreement",
        "partial agreement"
    ]


def test_calculate_agreement_strength_detects_low_agreement():

    agreement = calculate_agreement_strength(
        [1, 0, 1, 0]
    )

    assert agreement.lower() in [
        "low",
        "weak",
        "low agreement",
        "weak agreement"
    ]


def test_calculate_agreement_strength_handles_single_prediction():

    agreement = calculate_agreement_strength(
        [1]
    )

    assert isinstance(
        agreement,
        str
    )


def test_calculate_agreement_strength_raises_error_on_empty_list():

    with pytest.raises(
        (ValueError, ZeroDivisionError)
    ):

        calculate_agreement_strength([])