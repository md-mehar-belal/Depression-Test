# =========================================
# COMMON RANGE CONSTANTS
# =========================================

BINARY_RANGE = [0, 1]

LIKERT_4_RANGE = [0, 1, 2, 3]


# =========================================
# COMMON NUMERIC RANGES
# =========================================

AGE_RANGE = {
    "min": 18,
    "max": 28
}

ACADEMIC_STATUS_RANGE = {
    "min": 1,
    "max": 4
}

SOCIAL_ECONOMIC_STATUS_RANGE = {
    "min": 1,
    "max": 5
}

SLEEP_DURATION_RANGE = {
    "min": 4,
    "max": 9
}

SOCIAL_MEDIA_HOURS_RANGE = {
    "min": 1,
    "max": 11
}


# =========================================
# COMMON FEATURE RANGE MAP
# =========================================

COMMON_FEATURE_RANGES = {

    # Binary Features

    "Gender": BINARY_RANGE,
    "Smoking": BINARY_RANGE,
    "Alcohol_Consumption": BINARY_RANGE,
    "Has_Debts": BINARY_RANGE,
    "Physical_Activity": BINARY_RANGE,
    "On_Medication": BINARY_RANGE,
    "Work_While_Study": BINARY_RANGE,
    "Significant_Ailments": BINARY_RANGE,
    "Lost_Someone_Recently": BINARY_RANGE,
    "Satisfied_Living_Environment": BINARY_RANGE,

    "Relationship_Status_Divorced": BINARY_RANGE,
    "Relationship_Status_In a Relationship": BINARY_RANGE,
    "Relationship_Status_Married": BINARY_RANGE,
    "Relationship_Status_Single": BINARY_RANGE,

    "Residential_Area_Hall": BINARY_RANGE,
    "Residential_Area_Outside Hall": BINARY_RANGE,
    "Residential_Area_With family": BINARY_RANGE,

    # Likert Features

    "Agitation_Level": LIKERT_4_RANGE,
    "Anhedonia_No_Joy": LIKERT_4_RANGE,
    "Crying_Frequency": LIKERT_4_RANGE,
    "Difficulty_Focusing": LIKERT_4_RANGE,
    "Difficulty_Speaking_Socially": LIKERT_4_RANGE,
    "Easy_Fatigue": LIKERT_4_RANGE,
    "Emotional_Alignment_Frequency": LIKERT_4_RANGE,
    "Fatigue_Frequency": LIKERT_4_RANGE,
    "Fear_Something_Bad": LIKERT_4_RANGE,
    "Feeling_Down": LIKERT_4_RANGE,
    "Feeling_Insignificant": LIKERT_4_RANGE,
    "Feels_Others_Are_Kind": LIKERT_4_RANGE,
    "Feels_Pitied": LIKERT_4_RANGE,
    "Future_Hopelessness": LIKERT_4_RANGE,
    "High_Appetite": LIKERT_4_RANGE,
    "Hopelessness_EndFeeling": LIKERT_4_RANGE,
    "Indecisiveness": LIKERT_4_RANGE,
    "Insomnia": LIKERT_4_RANGE,
    "Interest_Loss": LIKERT_4_RANGE,
    "Irritability": LIKERT_4_RANGE,
    "Isolation_Frequency": LIKERT_4_RANGE,
    "Lack_of_Pleasure": LIKERT_4_RANGE,
    "Life_Feels_Hard": LIKERT_4_RANGE,
    "Loneliness_Frequency": LIKERT_4_RANGE,
    "Low_Appetite": LIKERT_4_RANGE,
    "Low_Concentration": LIKERT_4_RANGE,
    "Meaninglessness": LIKERT_4_RANGE,
    "Melancholic": LIKERT_4_RANGE,
    "No_Support_Frequency": LIKERT_4_RANGE,
    "Performance_Decline": LIKERT_4_RANGE,
    "Presence_Not_Genuine_Frequency": LIKERT_4_RANGE,
    "Recent_Abuse_Experience": LIKERT_4_RANGE,
    "Relationships_Unimportant_Level": LIKERT_4_RANGE,
    "Restlessness": LIKERT_4_RANGE,
    "Self_Confidence_Erosion": LIKERT_4_RANGE,
    "Self_Perceived_Failure": LIKERT_4_RANGE,
    "Share_Feelings_Lack": LIKERT_4_RANGE,
    "Social_LeftOut_Level": LIKERT_4_RANGE,
    "Social_Withdrawal": LIKERT_4_RANGE,
    "Suicidal_Thoughts": LIKERT_4_RANGE,

    # Numeric Features

    "Age": AGE_RANGE,
    "Academic Status": ACADEMIC_STATUS_RANGE,
    "Social Economic Status": SOCIAL_ECONOMIC_STATUS_RANGE,
    "Sleep_Duration": SLEEP_DURATION_RANGE,
    "Social_Media_Hours": SOCIAL_MEDIA_HOURS_RANGE
}