VALID_PREDICTION_PAYLOAD = {
    "Gender": 1,
    "Relationship_Status_Single": 1,
    "Age": 22,
    "Academic Status": 3,
    "Financial_Pressure": 1,
    "Physical_Activity": 1,
    "Sleep_Duration": 7,
    "Social_Media_Hours": 3,
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


LOW_RISK_PREDICTION_PAYLOAD = {
    **VALID_PREDICTION_PAYLOAD,
    "Melancholic": 0,
    "Future_Hopelessness": 0,
    "Self_Perceived_Failure": 0,
    "Interest_Loss": 0,
    "Feeling_Down": 0,
    "Suicidal_Thoughts": 0
}


HIGH_RISK_PREDICTION_PAYLOAD = {
    **VALID_PREDICTION_PAYLOAD,
    "Melancholic": 3,
    "Future_Hopelessness": 3,
    "Self_Perceived_Failure": 3,
    "Interest_Loss": 3,
    "Feeling_Down": 3,
    "Suicidal_Thoughts": 1,
    "Insomnia": 3,
    "Fatigue_Frequency": 3
}


INVALID_PREDICTION_PAYLOADS = {
    "missing_gender": {
        **VALID_PREDICTION_PAYLOAD
    },

    "missing_age": {
        **VALID_PREDICTION_PAYLOAD
    },

    "invalid_age_type": {
        **VALID_PREDICTION_PAYLOAD,
        "Age": "twenty two"
    },

    "negative_sleep_duration": {
        **VALID_PREDICTION_PAYLOAD,
        "Sleep_Duration": -5
    },

    "invalid_social_media_hours": {
        **VALID_PREDICTION_PAYLOAD,
        "Social_Media_Hours": "many"
    },

    "invalid_suicidal_thoughts": {
        **VALID_PREDICTION_PAYLOAD,
        "Suicidal_Thoughts": "yes"
    }
}


INVALID_PREDICTION_PAYLOADS["missing_gender"].pop(
    "Gender"
)

INVALID_PREDICTION_PAYLOADS["missing_age"].pop(
    "Age"
)