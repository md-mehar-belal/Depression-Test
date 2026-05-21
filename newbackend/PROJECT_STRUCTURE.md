backend/
│
├── run.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
│
├── app/
│   │
│   ├── __init__.py
│   ├── config.py
│   │
│   ├── environments/
│   │   ├── dev.py
│   │   └── prod.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── prediction_routes.py
│   │   └── history_routes.py
│   │
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── prediction_controller.py
│   │   └── history_controller.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── prediction_service.py
│   │   ├── jwt_service.py
│   │   ├── email_service.py
│   │   ├── google_auth_service.py
│   │   ├── logging_service.py
│   │   └── rate_limit_service.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   └── prediction_repository.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   └── collections.py
│   │
│   ├── middleware/
│   │   ├── auth_middleware.py
│   │   ├── error_middleware.py
│   │   ├── logging_middleware.py
│   │   ├── rate_limit_middleware.py
│   │   └── security_middleware.py
│   │
│   ├── decorators/
│   │   ├── jwt_decorator.py
│   │   └── role_decorator.py
│   │
│   ├── validators/
│   │   ├── auth_validator.py
│   │   ├── prediction_validator.py
│   │   ├── normalization_validator.py
│   │   ├── type_validator.py
│   │   └── range_validator.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── prediction_schema.py
│   │   └── history_schema.py
│   │
│   ├── external_apis/
│   │   ├── google_oauth.py
│   │   └── email_client.py
│   │
│   └── utils/
│       ├── response.py
│       ├── logger.py
│       ├── security.py
│       ├── constants.py
│       └── helpers.py
│
├── ml/
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   │
│   │   ├── feature_orders/
│   │   │   ├── __init__.py
│   │   │   ├── x1_bdi-ii.pkl
│   │   │   ├── x1_ces-d.pkl
│   │   │   ├── x1_phq9.pkl
│   │   │   ├── x2_bdi-ii.pkl
│   │   │   ├── x2_ces-d.pkl
│   │   │   ├── x2_phq9.pkl
│   │   │   ├── x3_bdi-ii.pkl
│   │   │   ├── x3_ces-d.pkl
│   │   │   ├── x3_phq9.pkl
│   │   │   ├── x4_bdi-ii.pkl
│   │   │   ├── x4_ces-d.pkl
│   │   │   └── x4_phq9.pkl
│   │   │
│   │   └── trained_models/
│   │       ├── __init__.py
│   │       │
│   │       ├── logistic_regression_x1_bdi-ii.pkl
│   │       ├── logistic_regression_x1_ces-d.pkl
│   │       ├── logistic_regression_x1_phq9.pkl
│   │       ├── logistic_regression_x2_bdi-ii.pkl
│   │       ├── logistic_regression_x2_ces-d.pkl
│   │       ├── logistic_regression_x2_phq9.pkl
│   │       ├── logistic_regression_x3_bdi-ii.pkl
│   │       ├── logistic_regression_x3_ces-d.pkl
│   │       ├── logistic_regression_x3_phq9.pkl
│   │       ├── logistic_regression_x4_bdi-ii.pkl
│   │       ├── logistic_regression_x4_ces-d.pkl
│   │       ├── logistic_regression_x4_phq9.pkl
│   │       │
│   │       ├── random_forest_x1_bdi-ii.pkl
│   │       ├── random_forest_x1_ces-d.pkl
│   │       ├── random_forest_x1_phq9.pkl
│   │       ├── random_forest_x2_bdi-ii.pkl
│   │       ├── random_forest_x2_ces-d.pkl
│   │       ├── random_forest_x2_phq9.pkl
│   │       ├── random_forest_x3_bdi-ii.pkl
│   │       ├── random_forest_x3_ces-d.pkl
│   │       ├── random_forest_x3_phq9.pkl
│   │       ├── random_forest_x4_bdi-ii.pkl
│   │       ├── random_forest_x4_ces-d.pkl
│   │       ├── random_forest_x4_phq9.pkl
│   │       │
│   │       ├── svm_x1_bdi-ii.pkl
│   │       ├── svm_x1_ces-d.pkl
│   │       ├── svm_x1_phq9.pkl
│   │       ├── svm_x2_bdi-ii.pkl
│   │       ├── svm_x2_ces-d.pkl
│   │       ├── svm_x2_phq9.pkl
│   │       ├── svm_x3_bdi-ii.pkl
│   │       ├── svm_x3_ces-d.pkl
│   │       ├── svm_x3_phq9.pkl
│   │       ├── svm_x4_bdi-ii.pkl
│   │       ├── svm_x4_ces-d.pkl
│   │       └── svm_x4_phq9.pkl
│   │
│   ├── preprocessing/
│   │   ├── feature_mapper.py
│   │   ├── feature_selector.py
│   │   └── normalizer.py
│   │
│   ├── inference/
│   │   ├── model_loader.py
│   │   ├── svm_predictor.py
│   │   ├── logistic_predictor.py
│   │   ├── randomforest_predictor.py
│   │   ├── ensemble_predictor.py
│   │   └── confidence_analyzer.py
│   │
│   ├── explainability/
│   │   ├── consensus_explainer.py
│   │   ├── feature_importance.py
│   │   └── severity_explainer.py
│   │
│   └── training/
│       │
│       ├── notebooks/
│       │   ├── 1_dataProcessing.ipynb
│       │   ├── 2_PHQ-9_Model.ipynb
│       │   ├── 3_BDI-II_Model.ipynb
│       │   └── 4_CES-D_Model.ipynb
│       │
│       ├── datasets/
│       ├── exports/
│       │   ├── feature_weights/
│       │   ├── preprocessing_objects/
│       │   └── trained_models/
│       │
│       ├── docsAndNotes/
│       └── experiments/
│           ├── comparison_reports/
│           ├── confusion_matrices/
│           └── evaluation_results/
│
├── data/
│   ├── logs/
│   │   ├── requests.log
│   │   ├── errors.log
│   │   └── auth.log
│   │
│   └── predictions/
│
└── tests/
    │
    ├── conftest.py
    ├── pytest.ini
    ├── test_security.py
    │
    ├── auth/
    │   ├── test_signup.py
    │   ├── test_login.py
    │   ├── test_logout.py
    │   ├── test_me.py
    │   ├── test_google_auth.py
    │   ├── test_password_reset.py
    │   ├── test_email_verification.py
    │   └── test_jwt.py
    │
    ├── prediction/
    │   ├── test_predict_endpoint.py
    │   ├── test_prediction_validation.py
    │   ├── test_prediction_response.py
    │   ├── test_prediction_history.py
    │   ├── test_model_selection.py
    │   ├── test_confidence_analysis.py
    │   └── test_ensemble_predictor.py
    │
    ├── services/
    │   ├── test_auth_service.py
    │   ├── test_prediction_service.py
    │   ├── test_jwt_service.py
    │   ├── test_email_service.py
    │   ├── test_google_auth_service.py
    │   ├── test_logging_service.py
    │   └── test_rate_limit_service.py
    │
    ├── repositories/
    │   ├── test_user_repository.py
    │   └── test_prediction_repository.py
    │
    ├── middleware/
    │   ├── test_auth_middleware.py
    │   ├── test_error_middleware.py
    │   ├── test_logging_middleware.py
    │   ├── test_rate_limit_middleware.py
    │   └── test_security_middleware.py
    │
    ├── ml/
    │   ├── test_feature_mapper.py
    │   ├── test_feature_selector.py
    │   ├── test_normalizer.py
    │   ├── test_model_loader.py
    │   ├── test_svm_predictor.py
    │   ├── test_logistic_predictor.py
    │   ├── test_randomforest_predictor.py
    │   ├── test_confidence_analyzer.py
    │   └── test_ensemble_predictor.py
    │
    ├── validators/
    │   ├── auth_validator.py
    │   ├── prediction_validator.py
    │   ├── normalization_validator.py
    │   ├── range_validator.py
    │   ├── type_validator.py
    │   └── feature_rules.py
    │
    ├── fixtures/
    │   ├── auth_payloads.py
    │   ├── prediction_payloads.py
    │   ├── user_fixtures.py
    │   ├── token_fixtures.py
    │   └── model_fixtures.py
    │
    ├── mocks/
    │   ├── mock_users.py
    │   ├── mock_tokens.py
    │   ├── mock_predictions.py
    │   └── mock_models.py
    │
    ├── integration/
    │   ├── test_auth_flow.py
    │   ├── test_prediction_flow.py
    │   ├── test_database_integration.py
    │   └── test_full_user_journey.py
    │
    └── security/
        ├── test_password_hashing.py
        ├── test_token_security.py
        ├── test_protected_routes.py
        └── test_input_sanitization.py