# API Testing Documentation

## 1. User Registration

### Endpoint

```
POST http://127.0.0.1:5000/auth/signup
```

### Request Body

```json
{
    "name": "Kusha1",
    "email": "kushal1@test.com",
    "password": "Password@1123"
}
```

### Response

```json
{
    "success": true,
    "message": "Signup successful",
    "data": {
        "token": "<JWT_TOKEN>",
        "user": {
            "id": "6a2133ec47e00909cc1b45ec",
            "name": "Kusha1",
            "email": "kushal1@test.com",
            "role": "user",
            "is_verified": true,
            "created_at": "2026-06-04T08:14:36.115316+00:00",
            "updated_at": "2026-06-04T08:14:36.115316+00:00"
        }
    }
}
```

---

## 2. User Login

### Endpoint

```
POST http://127.0.0.1:5000/auth/login
```

### Request Body

```json
{
    "email": "kushal@test.com",
    "password": "Password@123"
}
```

### Response

```json
{
    "success": true,
    "message": "Login successful",
    "data": {
        "token": "<JWT_TOKEN>",
        "user": {
            "id": "6a0fbdd3f44271e38acb2903",
            "name": "Kushal",
            "email": "kushal@test.com",
            "role": "user",
            "is_verified": true,
            "created_at": "2026-05-22T02:22:11.363239+00:00",
            "updated_at": "2026-05-22T02:22:11.363239+00:00"
        }
    }
}
```

---

## 3. Depression Prediction

### Endpoint

```
POST http://127.0.0.1:5000/predictions/predict
```

### Authentication

```
Authorization: Bearer <JWT_TOKEN>
```

### Request Body

```json
{
    "Gender": 0,
    "Relationship_Status_Single": 1,
    "Relationship_Status_In a Relationship": 0,
    "Relationship_Status_Married": 0,
    "Relationship_Status_Divorced": 0,
    "Age": 21,
    "Academic Status": 4,
    "Work_While_Study": 1,
    "Residential_Area_Hall": 1,
    "Residential_Area_Outside Hall": 0,
    "Residential_Area_With family": 0,
    "Social Economic Status": 4,
    "Financial_Pressure": 1,
    "Has_Debts": 1,
    "Satisfied_Living_Environment": 0,
    "Lost_Someone_Recently": 1,
    "Physical_Activity": 1,
    "Significant_Ailments": 1,
    "On_Medication": 0,
    "Smoking": 0,
    "Alcohol_Consumption": 1,
    "Sleep_Duration": 4,
    "Social_Media_Hours": 3,
    "Workload_Academic_Demand": 1,
    "Melancholic": 2,
    "Future_Hopelessness": 1,
    "Self_Perceived_Failure": 1,
    "Interest_Loss": 2,
    "Meaninglessness": 2,
    "Hopelessness_EndFeeling": 1,
    "Feeling_Insignificant": 1,
    "Self_Confidence_Erosion": 3,
    "Crying_Frequency": 3,
    "Agitation_Level": 3,
    "Social_Withdrawal": 1,
    "Indecisiveness": 1,
    "Anhedonia_No_Joy": 0,
    "Fatigue_Frequency": 0,
    "Insomnia": 2,
    "Irritability": 2,
    "Low_Appetite": 0,
    "Difficulty_Focusing": 0,
    "Easy_Fatigue": 1,
    "Low_Concentration": 1,
    "Difficulty_Speaking_Socially": 1,
    "High_Appetite": 2,
    "Restlessness": 1,
    "Life_Feels_Hard": 1,
    "Fear_Something_Bad": 1,
    "Recent_Abuse_Experience": 1,
    "Feels_Pitied": 1,
    "Lack_of_Pleasure": 1,
    "Feeling_Down": 1,
    "Feels_Others_Are_Kind": 1,
    "Performance_Decline": 1,
    "Share_Feelings_Lack": 1,
    "Social_LeftOut_Level": 2,
    "Isolation_Frequency": 2,
    "No_Support_Frequency": 2,
    "Loneliness_Frequency": 2,
    "Emotional_Alignment_Frequency": 2,
    "Presence_Not_Genuine_Frequency": 2,
    "Relationships_Unimportant_Level": 2,
    "Suicidal_Thoughts": 1
}
```

### Response

```json
{
    "success": true,
    "message": "Prediction generated successfully",
    "data": {
        "phq9": {
            "score": 2,
            "confidence": 51.5
        },
        "bdi": {
            "score": 2,
            "confidence": 97.0
        },
        "cesd": {
            "score": 2,
            "confidence": 76.51
        }
    }
}
```

---

## 4. Dashboard

### Endpoint

```
GET http://127.0.0.1:5000/dashboard
```

### Authentication

```
Authorization: Bearer <JWT_TOKEN>
```

### Response

```json
{
    "success": true,
    "data": {
        "user": {
            "id": "6a0fbdd3f44271e38acb2903",
            "name": "Kushal",
            "email": "kushal@test.com"
        },
        "history": [
            {
                "date": "2026-06-04T08:05:03.766761+00:00",
                "prediction_value": {
                    "phq9": {
                        "score": 2,
                        "confidence": 51.5
                    },
                    "bdi": {
                        "score": 2,
                        "confidence": 97.0
                    },
                    "cesd": {
                        "score": 2,
                        "confidence": 76.51
                    }
                },
                "recommendation": "Based on the predictions, we recommend consulting a mental health professional for a comprehensive evaluation and personalized treatment plan."
            }
        ]
    }
}
```

---

## API Workflow

```
1. User Signup/Login
          ↓
2. Receive JWT Token
          ↓
3. Submit Prediction Request
          ↓
4. Prediction Saved to History
          ↓
5. Retrieve Dashboard Data
          ↓
6. View User Profile + Prediction History
```
