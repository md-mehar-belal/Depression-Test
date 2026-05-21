import pytest

from app import app


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


PREDICTION_PAYLOAD = {
    "Gender": 1,
    "Relationship_Status_Divorced": 0,
    "Relationship_Status_In a Relationship": 0,
    "Relationship_Status_Married": 0,
    "Relationship_Status_Single": 1,
    "Age": 22,
    "Academic Status": 3,
    "Work_While_Study": 0,
    "Residential_Area_Hall": 1,
    "Residential_Area_With family": 0,
    "Residential_Area_Outside Hall": 0,
    "Social Economic Status": 3,
    "Financial_Pressure": 1,
    "Has_Debts": 0,
    "Satisfied_Living_Environment": 1,
    "Lost_Someone_Recently": 0,
    "Physical_Activity": 1,
    "Significant_Ailments": 0,
    "On_Medication": 0,
    "Smoking": 0,
    "Alcohol_Consumption": 0,
    "Sleep_Duration": 7,
    "Social_Media_Hours": 3,
    "Workload_Academic_Demand": 1,
    "Melancholic": 1,
    "Future_Hopelessness": 1,
    "Self_Perceived_Failure": 1,
    "Interest_Loss": 1,
    "Meaninglessness": 1,
    "Hopelessness_EndFeeling": 1,
    "Feeling_Insignificant": 1,
    "Self_Confidence_Erosion": 1,
    "Suicidal_Thoughts": 0,
    "Crying_Frequency": 1,
    "Agitation_Level": 1,
    "Social_Withdrawal": 1,
    "Indecisiveness": 1,
    "Anhedonia_No_Joy": 1,
    "Fatigue_Frequency": 1,
    "Insomnia": 1,
    "Irritability": 1,
    "Low_Appetite": 1,
    "Difficulty_Focusing": 1,
    "Easy_Fatigue": 1,
    "Low_Concentration": 1,
    "Difficulty_Speaking_Socially": 1,
    "High_Appetite": 1,
    "Restlessness": 1,
    "Life_Feels_Hard": 1,
    "Fear_Something_Bad": 1,
    "Recent_Abuse_Experience": 0,
    "Feels_Pitied": 1,
    "Lack_of_Pleasure": 1,
    "Feeling_Down": 1,
    "Feels_Others_Are_Kind": 1,
    "Performance_Decline": 1,
    "Share_Feelings_Lack": 1,
    "Social_LeftOut_Level": 1,
    "Isolation_Frequency": 1,
    "No_Support_Frequency": 1,
    "Loneliness_Frequency": 1,
    "Emotional_Alignment_Frequency": 1,
    "Presence_Not_Genuine_Frequency": 1,
    "Relationships_Unimportant_Level": 1
}


def test_complete_user_journey(client):

    # =========================
    # STEP 1 — SIGNUP
    # =========================

    signup_payload = {
        "name": "Kushal",
        "email": "kushal@example.com",
        "password": "StrongPassword123"
    }

    signup_response = client.post(
        "/auth/signup",
        json=signup_payload
    )

    assert signup_response.status_code == 201

    signup_data = signup_response.get_json()

    assert "token" in signup_data

    assert signup_data["user"]["email"] == (
        "kushal@example.com"
    )

    # =========================
    # STEP 2 — LOGIN
    # =========================

    login_payload = {
        "email": "kushal@example.com",
        "password": "StrongPassword123"
    }

    login_response = client.post(
        "/auth/login",
        json=login_payload
    )

    assert login_response.status_code == 200

    login_data = login_response.get_json()

    assert "token" in login_data

    jwt_token = login_data["token"]

    # =========================
    # STEP 3 — ACCESS /auth/me
    # =========================

    me_response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {jwt_token}"
            )
        }
    )

    assert me_response.status_code == 200

    me_data = me_response.get_json()

    assert me_data["user"]["email"] == (
        "kushal@example.com"
    )

    # =========================
    # STEP 4 — PREDICTION REQUEST
    # =========================

    prediction_response = client.post(
        "/predict",
        json=PREDICTION_PAYLOAD
    )

    assert prediction_response.status_code == 200

    prediction_data = (
        prediction_response.get_json()
    )

    assert "prediction" in prediction_data

    assert "confidence_score" in (
        prediction_data
    )

    assert "mental_health_tip" in (
        prediction_data
    )

    # =========================
    # STEP 5 — RESPONSE VALIDATION
    # =========================

    assert isinstance(
        prediction_data["prediction"],
        int
    )

    assert isinstance(
        prediction_data["confidence_score"],
        float
    )

    assert isinstance(
        prediction_data["mental_health_tip"],
        str
    )

    assert (
        0.0
        <= prediction_data[
            "confidence_score"
        ]
        <= 1.0
    )


def test_user_journey_with_invalid_login(client):

    signup_payload = {
        "name": "Test User",
        "email": "invalidlogin@example.com",
        "password": "CorrectPassword123"
    }

    client.post(
        "/auth/signup",
        json=signup_payload
    )

    invalid_login_payload = {
        "email": "invalidlogin@example.com",
        "password": "WrongPassword"
    }

    response = client.post(
        "/auth/login",
        json=invalid_login_payload
    )

    assert response.status_code == 401

    response_data = response.get_json()

    assert (
        response_data["error"]
        == "Invalid credentials"
    )


def test_user_journey_protected_route_without_token(client):

    response = client.get(
        "/auth/me"
    )

    assert response.status_code == 401

    response_data = response.get_json()

    assert (
        response_data["error"]
        == "Authorization token missing"
    )


def test_user_journey_duplicate_signup(client):

    payload = {
        "name": "Duplicate User",
        "email": "duplicate@example.com",
        "password": "Password123"
    }

    first_response = client.post(
        "/auth/signup",
        json=payload
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/auth/signup",
        json=payload
    )

    assert second_response.status_code == 409

    response_data = second_response.get_json()

    assert (
        response_data["error"]
        == "User already exists"
    )