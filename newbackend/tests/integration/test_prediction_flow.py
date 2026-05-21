import pytest

from app import app


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


VALID_PAYLOAD = {
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


def test_prediction_endpoint_success(client):

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD
    )

    assert response.status_code == 200

    response_data = response.get_json()

    assert "prediction" in response_data

    assert "confidence_score" in response_data

    assert "mental_health_tip" in response_data


def test_prediction_response_types(client):

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD
    )

    response_data = response.get_json()

    assert isinstance(
        response_data["prediction"],
        int
    )

    assert isinstance(
        response_data["confidence_score"],
        float
    )

    assert isinstance(
        response_data["mental_health_tip"],
        str
    )


def test_prediction_confidence_range(client):

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD
    )

    response_data = response.get_json()

    confidence = response_data[
        "confidence_score"
    ]

    assert 0.0 <= confidence <= 1.0


def test_prediction_missing_feature(client):

    invalid_payload = VALID_PAYLOAD.copy()

    invalid_payload.pop("Age")

    response = client.post(
        "/predict",
        json=invalid_payload
    )

    assert response.status_code == 400

    response_data = response.get_json()

    assert "Missing feature" in (
        response_data["error"]
    )


def test_prediction_empty_payload(client):

    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 400

    response_data = response.get_json()

    assert "Missing feature" in (
        response_data["error"]
    )


def test_prediction_invalid_content_type(client):

    response = client.post(
        "/predict",
        data="plain text payload",
        content_type="text/plain"
    )

    assert response.status_code in [400, 415]


def test_prediction_endpoint_returns_json(client):

    response = client.post(
        "/predict",
        json=VALID_PAYLOAD
    )

    assert response.content_type.startswith(
        "application/json"
    )