from datetime import datetime, UTC

import pytest

from app.repositories.user_repository import (
    create_user,
    find_user_by_email
)

from app.repositories.prediction_repository import (
    save_prediction
)


@pytest.fixture
def sample_user():

    return {
        "name": "Kushal",
        "email": "kushal@example.com",
        "password": "hashed_password"
    }


@pytest.fixture
def sample_prediction():

    return {
        "input_data": {
            "Age": 22,
            "Gender": 1,
            "Feeling_Down": 1
        },
        "prediction": 1,
        "confidence": 0.82,
        "recommendation": (
            "Take rest and seek support."
        )
    }


def test_create_user_in_database(
    sample_user
):

    created_user = create_user(
        name=sample_user["name"],
        email=sample_user["email"],
        password=sample_user["password"]
    )

    assert created_user is not None

    assert created_user["email"] == (
        sample_user["email"]
    )

    assert "id" in created_user


def test_find_user_by_email(
    sample_user
):

    create_user(
        name=sample_user["name"],
        email=sample_user["email"],
        password=sample_user["password"]
    )

    found_user = find_user_by_email(
        sample_user["email"]
    )

    assert found_user is not None

    assert found_user["email"] == (
        sample_user["email"]
    )

    assert found_user["name"] == (
        sample_user["name"]
    )


def test_find_nonexistent_user():

    user = find_user_by_email(
        "nonexistent@example.com"
    )

    assert user is None


def test_save_prediction_to_database(
    sample_prediction
):

    inserted_id = save_prediction(
        input_data=sample_prediction[
            "input_data"
        ],
        date_time=datetime.now(
            UTC
        ).isoformat(),
        prediction=sample_prediction[
            "prediction"
        ],
        confidence=sample_prediction[
            "confidence"
        ],
        tip=sample_prediction[
            "recommendation"
        ]
    )

    assert inserted_id is not None

    assert isinstance(inserted_id, str)


def test_multiple_users_can_be_created():

    user_one = create_user(
        name="User One",
        email="userone@example.com",
        password="hashed1"
    )

    user_two = create_user(
        name="User Two",
        email="usertwo@example.com",
        password="hashed2"
    )

    assert user_one["email"] != (
        user_two["email"]
    )

    assert user_one["id"] != (
        user_two["id"]
    )


def test_prediction_document_structure(
    sample_prediction
):

    inserted_id = save_prediction(
        input_data=sample_prediction[
            "input_data"
        ],
        date_time=datetime.now(
            UTC
        ).isoformat(),
        prediction=sample_prediction[
            "prediction"
        ],
        confidence=sample_prediction[
            "confidence"
        ],
        tip=sample_prediction[
            "recommendation"
        ]
    )

    assert isinstance(inserted_id, str)

    assert len(inserted_id) > 10