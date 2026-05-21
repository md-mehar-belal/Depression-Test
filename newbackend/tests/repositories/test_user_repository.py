# backend/tests/repositories/test_user_repository.py

from unittest.mock import MagicMock
from bson import ObjectId

from app.repositories.user_repository import (
    create_user,
    find_user_by_email,
    find_user_by_id,
    update_user,
    verify_user_email
)


class MockInsertResult:
    def __init__(self, inserted_id):
        self.inserted_id = inserted_id


class MockUpdateResult:
    def __init__(self, modified_count):
        self.modified_count = modified_count


def test_create_user(monkeypatch):

    mock_collection = MagicMock()

    inserted_id = ObjectId()

    mock_collection.insert_one.return_value = (
        MockInsertResult(inserted_id)
    )

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    user_data = {
        "name": "Kushal",
        "email": "kushal@test.com",
        "password": "hashed-password"
    }

    result = create_user(user_data)

    assert result["id"] == str(inserted_id)

    mock_collection.insert_one.assert_called_once()


def test_find_user_by_email_found(monkeypatch):

    mock_collection = MagicMock()

    user_id = ObjectId()

    mock_collection.find_one.return_value = {
        "_id": user_id,
        "name": "Kushal",
        "email": "kushal@test.com",
        "password": "hashed-password"
    }

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = find_user_by_email(
        "kushal@test.com"
    )

    assert result is not None
    assert result["id"] == str(user_id)
    assert result["email"] == "kushal@test.com"


def test_find_user_by_email_not_found(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.find_one.return_value = None

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = find_user_by_email(
        "missing@test.com"
    )

    assert result is None


def test_find_user_by_id_found(monkeypatch):

    mock_collection = MagicMock()

    user_id = ObjectId()

    mock_collection.find_one.return_value = {
        "_id": user_id,
        "name": "Kushal",
        "email": "kushal@test.com"
    }

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = find_user_by_id(str(user_id))

    assert result is not None
    assert result["id"] == str(user_id)


def test_find_user_by_id_not_found(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.find_one.return_value = None

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = find_user_by_id(
        str(ObjectId())
    )

    assert result is None


def test_update_user_success(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.update_one.return_value = (
        MockUpdateResult(1)
    )

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = update_user(
        user_id=str(ObjectId()),
        update_data={
            "name": "Updated Name"
        }
    )

    assert result is True


def test_update_user_failure(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.update_one.return_value = (
        MockUpdateResult(0)
    )

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = update_user(
        user_id=str(ObjectId()),
        update_data={
            "name": "Updated Name"
        }
    )

    assert result is False


def test_verify_user_email_success(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.update_one.return_value = (
        MockUpdateResult(1)
    )

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = verify_user_email(
        str(ObjectId())
    )

    assert result is True


def test_verify_user_email_failure(monkeypatch):

    mock_collection = MagicMock()

    mock_collection.update_one.return_value = (
        MockUpdateResult(0)
    )

    monkeypatch.setattr(
        "app.repositories.user_repository.users_collection",
        mock_collection
    )

    result = verify_user_email(
        str(ObjectId())
    )

    assert result is False
    