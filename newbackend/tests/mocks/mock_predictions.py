from datetime import datetime, UTC


MOCK_PREDICTION_REQUEST = {
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


MOCK_INVALID_PREDICTION_REQUEST = {
    "Age": "invalid-age",
    "Gender": None
}


MOCK_PREDICTION_RESPONSE = {
    "prediction": 1,
    "confidence_score": 0.87,
    "mental_health_tip": (
        "Take proper rest and maintain "
        "regular social interaction."
    )
}


MOCK_LOW_CONFIDENCE_RESPONSE = {
    "prediction": 1,
    "confidence_score": 0.42,
    "mental_health_tip": (
        "Model confidence is low. "
        "Consider retaking the assessment."
    )
}


MOCK_HIGH_RISK_RESPONSE = {
    "prediction": 3,
    "confidence_score": 0.96,
    "mental_health_tip": (
        "Please consider reaching out "
        "to a trusted person or professional."
    )
}


MOCK_PREDICTION_HISTORY = [
    {
        "id": "pred_001",
        "prediction": 1,
        "confidence_score": 0.82,
        "created_at": datetime.now(
            UTC
        ).isoformat()
    },
    {
        "id": "pred_002",
        "prediction": 0,
        "confidence_score": 0.91,
        "created_at": datetime.now(
            UTC
        ).isoformat()
    }
]


MOCK_MODEL_OUTPUT = {
    "svm_prediction": 1,
    "svm_probability": 0.84,
    "logistic_prediction": 1,
    "logistic_probability": 0.79,
    "randomforest_prediction": 0,
    "randomforest_probability": 0.61
}


MOCK_ENSEMBLE_OUTPUT = {
    "final_prediction": 1,
    "agreement_strength": 0.67,
    "confidence_score": 0.81
}


MOCK_CONFIDENCE_ANALYSIS = {
    "confidence_score": 0.81,
    "confidence_level": "high",
    "agreement_strength": 0.67
}