import pytest

from flask import Flask
from flask.testing import FlaskClient

from app import create_app
from app.services.jwt_service import create_access_token


# =========================================================
# APP
# =========================================================

@pytest.fixture(scope="session")
def app() -> Flask:

    app = create_app("testing")

    app.config.update({
        "TESTING": True
    })

    yield app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:

    return app.test_client()


# =========================================================
# AUTH FIXTURES
# =========================================================

@pytest.fixture()
def sample_user() -> dict:

    return {
        "name": "Kushal",
        "email": "kushal@test.com",
        "password": "securepassword123"
    }


@pytest.fixture()
def mock_db_user() -> dict:

    return {
        "_id": "mock-user-id",
        "name": "Kushal",
        "email": "kushal@test.com",
        "password": "hashed-password",
        "role": "user",
        "is_verified": True
    }


@pytest.fixture()
def login_payload() -> dict:

    return {
        "email": "kushal@test.com",
        "password": "securepassword123"
    }


@pytest.fixture()
def auth_token() -> str:

    return create_access_token({
        "user_id": "test-user-id",
        "email": "kushal@test.com",
        "role": "user"
    })


@pytest.fixture()
def auth_headers(auth_token: str) -> dict:

    return {
        "Authorization": f"Bearer {auth_token}"
    }


# =========================================================
# PREDICTION FIXTURES
# =========================================================

@pytest.fixture()
def base_prediction_payload() -> dict:
    """
    Full X3-compatible payload.
    Safest default payload for prediction tests.
    """

    return {
        "Academic Status": 3,
        "Age": 22,
        "Agitation_Level": 1,
        "Alcohol_Consumption": 0,
        "Anhedonia_No_Joy": 1,
        "Crying_Frequency": 1,
        "Difficulty_Focusing": 1,
        "Difficulty_Speaking_Socially": 1,
        "Easy_Fatigue": 1,
        "Emotional_Alignment_Frequency": 1,
        "Fatigue_Frequency": 1,
        "Fear_Something_Bad": 1,
        "Feeling_Down": 1,
        "Feeling_Insignificant": 1,
        "Feels_Others_Are_Kind": 1,
        "Feels_Pitied": 1,
        "Financial_Pressure": 2,
        "Future_Hopelessness": 1,
        "Gender": 1,
        "Has_Debts": 0,
        "High_Appetite": 0,
        "Hopelessness_EndFeeling": 1,
        "Indecisiveness": 1,
        "Insomnia": 1,
        "Interest_Loss": 1,
        "Irritability": 1,
        "Isolation_Frequency": 1,
        "Lack_of_Pleasure": 1,
        "Life_Feels_Hard": 1,
        "Loneliness_Frequency": 1,
        "Lost_Someone_Recently": 0,
        "Low_Appetite": 1,
        "Low_Concentration": 1,
        "Meaninglessness": 1,
        "Melancholic": 1,
        "No_Support_Frequency": 1,
        "On_Medication": 0,
        "Performance_Decline": 1,
        "Physical_Activity": 1,
        "Presence_Not_Genuine_Frequency": 1,
        "Recent_Abuse_Experience": 0,
        "Relationship_Status_Divorced": 0,
        "Relationship_Status_In a Relationship": 0,
        "Relationship_Status_Married": 0,
        "Relationship_Status_Single": 1,
        "Relationships_Unimportant_Level": 1,
        "Residential_Area_Hall": 1,
        "Residential_Area_Outside Hall": 0,
        "Residential_Area_With family": 0,
        "Restlessness": 1,
        "Satisfied_Living_Environment": 1,
        "Self_Confidence_Erosion": 1,
        "Self_Perceived_Failure": 1,
        "Share_Feelings_Lack": 1,
        "Significant_Ailments": 0,
        "Sleep_Duration": 7,
        "Smoking": 0,
        "Social Economic Status": 2,
        "Social_LeftOut_Level": 1,
        "Social_Media_Hours": 2,
        "Social_Withdrawal": 1,
        "Suicidal_Thoughts": 0,
        "Work_While_Study": 0,
        "Workload_Academic_Demand": 2
    }


@pytest.fixture()
def invalid_prediction_payload() -> dict:

    return {
        "Age": "twenty-two",
        "Gender": "male"
    }


@pytest.fixture()
def incomplete_prediction_payload() -> dict:

    return {
        "Age": 22
    }


# =========================================================
# TEST CLEANUP
# =========================================================

@pytest.fixture(autouse=True)
def cleanup_test_state():

    yield