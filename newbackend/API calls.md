API calls 

=========================================================================================================================================

/auth/signup



POST http://127.0.0.1:5000/auth/signup



Body: 

{

&#x20; "name": "Kusha1",

&#x20; "email": "kushal1@test.com",

&#x20; "password": "Password@1123"

}





Output: 

{

&#x20;   "data": {

&#x20;       "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmEyMTMzZWM0N2UwMDkwOWNjMWI0NWVjIiwiZW1haWwiOiJrdXNoYWwxQHRlc3QuY29tIiwicHVycG9zZSI6ImFjY2VzcyIsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE3ODA1NjA4NzksImV4cCI6MTc4MDU2MjY3OX0.hY-dwOGwpj6Xj0TOVWxEuLR5T0jU42tdRkl31-rXZC4",

&#x20;       "user": {

&#x20;           "created\_at": "2026-06-04T08:14:36.115316+00:00",

&#x20;           "email": "kushal1@test.com",

&#x20;           "id": "6a2133ec47e00909cc1b45ec",

&#x20;           "is\_verified": true,

&#x20;           "name": "Kusha1",

&#x20;           "role": "user",

&#x20;           "updated\_at": "2026-06-04T08:14:36.115316+00:00"

&#x20;       }

&#x20;   },

&#x20;   "message": "Signup successful",

&#x20;   "success": true

}







=========================================================================================================================================

/auth/login



POST http://127.0.0.1:5000/auth/login



Body: 

{

&#x20; "email": "kushal@test.com",

&#x20; "password": "Password@123"

}



Output: 

{

&#x20;   "data": {

&#x20;       "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmEwZmJkZDNmNDQyNzFlMzhhY2IyOTAzIiwiZW1haWwiOiJrdXNoYWxAdGVzdC5jb20iLCJwdXJwb3NlIjoiYWNjZXNzIiwidHlwZSI6ImFjY2VzcyIsImlhdCI6MTc4MDU2MDI4NCwiZXhwIjoxNzgwNTYyMDg0fQ.r6vMhlF7R1QlExG4bmQ39WcTL2t9cCoO8cpX\_RhSbok",

&#x20;       "user": {

&#x20;           "created\_at": "2026-05-22T02:22:11.363239+00:00",

&#x20;           "email": "kushal@test.com",

&#x20;           "id": "6a0fbdd3f44271e38acb2903",

&#x20;           "is\_verified": true,

&#x20;           "name": "Kushal",

&#x20;           "role": "user",

&#x20;           "updated\_at": "2026-05-22T02:22:11.363239+00:00"

&#x20;       }

&#x20;   },

&#x20;   "message": "Login successful",

&#x20;   "success": true

}





=========================================================================================================================================

/predictions/predict



POST http://localhost:5000/predictions/predict



Body: 

{

&#x20; "Gender": 0,

&#x20; "Relationship\_Status\_Single": 1,

&#x20; "Relationship\_Status\_In a Relationship": 0,

&#x20; "Relationship\_Status\_Married": 0,

&#x20; "Relationship\_Status\_Divorced": 0,

&#x20; "Age": 21,

&#x20; "Academic Status": 4,

&#x20; "Work\_While\_Study": 1,

&#x20; "Residential\_Area\_Hall": 1,

&#x20; "Residential\_Area\_Outside Hall": 0,

&#x20; "Residential\_Area\_With family": 0,

&#x20; "Social Economic Status": 4,

&#x20; "Financial\_Pressure": 1,

&#x20; "Has\_Debts": 1,

&#x20; "Satisfied\_Living\_Environment": 0,

&#x20; "Lost\_Someone\_Recently": 1,

&#x20; "Physical\_Activity": 1,

&#x20; "Significant\_Ailments": 1,

&#x20; "On\_Medication": 0,

&#x20; "Smoking": 0,

&#x20; "Alcohol\_Consumption": 1,

&#x20; "Sleep\_Duration": 4,

&#x20; "Social\_Media\_Hours": 3,

&#x20; "Workload\_Academic\_Demand": 1,

&#x20; "Melancholic": 2,

&#x20; "Future\_Hopelessness": 1,

&#x20; "Self\_Perceived\_Failure": 1,

&#x20; "Interest\_Loss": 2,

&#x20; "Meaninglessness": 2,

&#x20; "Hopelessness\_EndFeeling": 1,

&#x20; "Feeling\_Insignificant": 1,

&#x20; "Self\_Confidence\_Erosion": 3,

&#x20; "Crying\_Frequency": 3,

&#x20; "Agitation\_Level": 3,

&#x20; "Social\_Withdrawal": 1,

&#x20; "Indecisiveness": 1,

&#x20; "Anhedonia\_No\_Joy": 0,

&#x20; "Fatigue\_Frequency": 0,

&#x20; "Insomnia": 2,

&#x20; "Irritability": 2,

&#x20; "Low\_Appetite": 0,

&#x20; "Difficulty\_Focusing": 0,

&#x20; "Easy\_Fatigue": 1,

&#x20; "Low\_Concentration": 1,

&#x20; "Difficulty\_Speaking\_Socially": 1,

&#x20; "High\_Appetite": 2,

&#x20; "Restlessness": 1,

&#x20; "Life\_Feels\_Hard": 1,

&#x20; "Fear\_Something\_Bad": 1,

&#x20; "Recent\_Abuse\_Experience": 1,

&#x20; "Feels\_Pitied": 1,

&#x20; "Lack\_of\_Pleasure": 1,

&#x20; "Feeling\_Down": 1,

&#x20; "Feels\_Others\_Are\_Kind": 1,

&#x20; "Performance\_Decline": 1,

&#x20; "Share\_Feelings\_Lack": 1,

&#x20; "Social\_LeftOut\_Level": 2,

&#x20; "Isolation\_Frequency": 2,

&#x20; "No\_Support\_Frequency": 2,

&#x20; "Loneliness\_Frequency": 2,

&#x20; "Emotional\_Alignment\_Frequency": 2,

&#x20; "Presence\_Not\_Genuine\_Frequency": 2,

&#x20; "Relationships\_Unimportant\_Level": 2,

&#x20; "Suicidal\_Thoughts": 1

}



Output: 

{

&#x20;   "data": {

&#x20;       "bdi": {

&#x20;           "confidence": 97.0,

&#x20;           "score": 2

&#x20;       },

&#x20;       "cesd": {

&#x20;           "confidence": 76.51,

&#x20;           "score": 2

&#x20;       },

&#x20;       "phq9": {

&#x20;           "confidence": 51.5,

&#x20;           "score": 2

&#x20;       }

&#x20;   },

&#x20;   "message": "Prediction generated successfully",

&#x20;   "success": true

}

=========================================================================================================================================

/dashboard



GET http://127.0.0.1:5000/dashboard





Output: 

{

&#x20;   "data": {

&#x20;       "history": \[

&#x20;           {

&#x20;               "date": "2026-06-04T08:05:03.766761+00:00",

&#x20;               "prediction\_value": {

&#x20;                   "bdi": {

&#x20;                       "confidence": 97.0,

&#x20;                       "score": 2

&#x20;                   },

&#x20;                   "cesd": {

&#x20;                       "confidence": 76.51,

&#x20;                       "score": 2

&#x20;                   },

&#x20;                   "phq9": {

&#x20;                       "confidence": 51.5,

&#x20;                       "score": 2

&#x20;                   }

&#x20;               },

&#x20;               "recommendation": "Based on the predictions, we recommend consulting a mental health professional for a comprehensive evaluation and personalized treatment plan."

&#x20;           },

&#x20;           {

&#x20;               "date": "2026-06-04T08:03:35.798648+00:00",

&#x20;               "prediction\_value": {

&#x20;                   "bdi": {

&#x20;                       "confidence": 97.0,

&#x20;                       "score": 2

&#x20;                   },

&#x20;                   "cesd": {

&#x20;                       "confidence": 76.51,

&#x20;                       "score": 2

&#x20;                   },

&#x20;                   "phq9": {

&#x20;                       "confidence": 51.5,

&#x20;                       "score": 2

&#x20;                   }

&#x20;               },

&#x20;               "recommendation": "Based on the predictions, we recommend consulting a mental health professional for a comprehensive evaluation and personalized treatment plan."

&#x20;           },

&#x20;           {

&#x20;               "date": "2026-06-04T08:00:26.056419+00:00",

&#x20;               "prediction\_value": {

&#x20;                   "bdi": {

&#x20;                       "confidence": 97.0,

&#x20;                       "score": 2

&#x20;                   },

&#x20;                   "cesd": {

&#x20;                       "confidence": 76.51,

&#x20;                       "score": 2

&#x20;                   },

&#x20;                   "phq9": {

&#x20;                       "confidence": 51.5,

&#x20;                       "score": 2

&#x20;                   }

&#x20;               },

&#x20;               "recommendation": "Based on the predictions, we recommend consulting a mental health professional for a comprehensive evaluation and personalized treatment plan."

&#x20;           }

&#x20;       ],

&#x20;       "user": {

&#x20;           "email": "kushal@test.com",

&#x20;           "id": "6a0fbdd3f44271e38acb2903",

&#x20;           "name": "Kushal"

&#x20;       }

&#x20;   },

&#x20;   "success": true

}





















































