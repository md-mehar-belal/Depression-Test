from unittest.mock import MagicMock, patch

import pytest

from ml.inference.model_loader import (
    get_loaded_models,
    load_feature_orders,
    load_models
)


@patch("ml.inference.model_loader.joblib.load")
def test_load_models_returns_dictionary(
    mock_joblib_load
):

    mock_joblib_load.side_effect = [
        MagicMock(name="svm_model"),
        MagicMock(name="logistic_model"),
        MagicMock(name="rf_model")
    ]

    loaded_models = load_models()

    assert isinstance(
        loaded_models,
        dict
    )


@patch("ml.inference.model_loader.joblib.load")
def test_load_models_contains_expected_models(
    mock_joblib_load
):

    mock_joblib_load.side_effect = [
        MagicMock(name="svm_model"),
        MagicMock(name="logistic_model"),
        MagicMock(name="rf_model")
    ]

    loaded_models = load_models()

    assert "svm_model" in loaded_models
    assert "logistic_model" in loaded_models
    assert "randomforest_model" in loaded_models


@patch("ml.inference.model_loader.joblib.load")
def test_load_feature_orders_returns_dictionary(
    mock_joblib_load
):

    mock_joblib_load.side_effect = [
        ["feature_1", "feature_2"],
        ["feature_1", "feature_2"],
        ["feature_1", "feature_2"]
    ]

    feature_orders = load_feature_orders()

    assert isinstance(
        feature_orders,
        dict
    )


@patch("ml.inference.model_loader.joblib.load")
def test_load_feature_orders_contains_expected_keys(
    mock_joblib_load
):

    mock_joblib_load.side_effect = [
        ["feature_1"],
        ["feature_1"],
        ["feature_1"]
    ]

    feature_orders = load_feature_orders()

    assert "svm_features" in feature_orders
    assert "logistic_features" in feature_orders
    assert "randomforest_features" in feature_orders


@patch("ml.inference.model_loader.load_models")
@patch("ml.inference.model_loader.load_feature_orders")
def test_get_loaded_models_returns_combined_data(
    mock_load_feature_orders,
    mock_load_models
):

    mock_load_models.return_value = {
        "svm_model": MagicMock(),
        "logistic_model": MagicMock(),
        "randomforest_model": MagicMock()
    }

    mock_load_feature_orders.return_value = {
        "svm_features": ["a"],
        "logistic_features": ["b"],
        "randomforest_features": ["c"]
    }

    loaded_resources = get_loaded_models()

    assert isinstance(
        loaded_resources,
        dict
    )

    assert "models" in loaded_resources
    assert "feature_orders" in loaded_resources


@patch("ml.inference.model_loader.joblib.load")
def test_load_models_raises_file_not_found(
    mock_joblib_load
):

    mock_joblib_load.side_effect = (
        FileNotFoundError
    )

    with pytest.raises(
        FileNotFoundError
    ):

        load_models()


@patch("ml.inference.model_loader.joblib.load")
def test_load_feature_orders_raises_file_not_found(
    mock_joblib_load
):

    mock_joblib_load.side_effect = (
        FileNotFoundError
    )

    with pytest.raises(
        FileNotFoundError
    ):

        load_feature_orders()


@patch("ml.inference.model_loader.joblib.load")
def test_load_models_calls_joblib_multiple_times(
    mock_joblib_load
):

    mock_joblib_load.side_effect = [
        MagicMock(),
        MagicMock(),
        MagicMock()
    ]

    load_models()

    assert (
        mock_joblib_load.call_count == 3
    )


@patch("ml.inference.model_loader.joblib.load")
def test_load_feature_orders_calls_joblib_multiple_times(
    mock_joblib_load
):

    mock_joblib_load.side_effect = [
        ["feature_1"],
        ["feature_1"],
        ["feature_1"]
    ]

    load_feature_orders()

    assert (
        mock_joblib_load.call_count == 3
    )