# backend/tests/repositories/test_prediction_repository.py

from unittest.mock import MagicMock
from bson import ObjectId

from app.repositories.prediction_repository import (
    save_prediction,
    get_prediction_history,
    get_prediction_by_id
)


class MockInsertResult:
    def __init__(self, inserted_id):
        self.inserted_id = inserted_id


def test_save_prediction(monkeypatch):

    mock_collection = MagicMock()

    inserted_id = ObjectId()

    mock_collection.insert_one.return_value = (
        MockInsertResult(inserted_id)
    )

    monkeypatch.setattr(
        "app.repositories.prediction_repository.predictions_collection",
        mock_collection
    )

    prediction_data = {
        "user_id": "user123",
        "prediction": 2,
        "confidence": 0.87,
        "model": "svm",
        "recommendation": "Seek support if needed."
    }

    result = save_prediction(
        prediction_data
    )

    assert result["id"] == str(inserted_id)

    mock_collection.insert_one.assert_called_once()


def test_get_prediction_by_id_found(monkeypatch):

    mock_collection = MagicMock()

    prediction_id = ObjectId()

    mock_collection.find_one.return_value = {
        "_id": prediction_id,
        "user_id": "user123",
        "prediction": 1,
        "confidence": 0.75
    }

    monkeypatch.setattr(
        "app.repositories.prediction_repository.predictions_collection",
        mock_collection
    )

    result = get_prediction_by_id(
        str(prediction_id)
    )

    assert result is not None
    assert result["id"] == str(prediction_id)
    assert result["prediction"] == 1


def test_get_prediction_by_id_not_found(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.find_one.return_value = None

    monkeypatch.setattr(
        "app.repositories.prediction_repository.predictions_collection",
        mock_collection
    )

    result = get_prediction_by_id(
        str(ObjectId())
    )

    assert result is None


def test_get_prediction_history(monkeypatch):

    mock_collection = MagicMock()

    prediction_1 = {
        "_id": ObjectId(),
        "user_id": "user123",
        "prediction": 0,
        "confidence": 0.91
    }

    prediction_2 = {
        "_id": ObjectId(),
        "user_id": "user123",
        "prediction": 2,
        "confidence": 0.67
    }

    mock_collection.find.return_value.sort.return_value = [
        prediction_1,
        prediction_2
    ]

    monkeypatch.setattr(
        "app.repositories.prediction_repository.predictions_collection",
        mock_collection
    )

    result = get_prediction_history(
        user_id="user123"
    )

    assert len(result) == 2

    assert result[0]["prediction"] == 0
    assert result[1]["prediction"] == 2

    assert "id" in result[0]
    assert "id" in result[1]


def test_get_prediction_history_empty(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.find.return_value.sort.return_value = []

    monkeypatch.setattr(
        "app.repositories.prediction_repository.predictions_collection",
        mock_collection
    )

    result = get_prediction_history(
        user_id="unknown-user"
    )

    assert result == []