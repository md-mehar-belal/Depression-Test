MODEL_NAMES = {
    "CESD": "svm_x3_cesd",
    "BDI": "logistic_x1_bdi",
    "PHQ9": "randomforest_x3_phq9"
}
SEVERITY_LABELS = {
    0: "low",
    1: "mild",
    2: "moderate",
    3: "high"
}
JWT_ALGORITHM = "HS256"
DEFAULT_RATE_LIMIT = 60
SUPPORTED_TEST_TYPES = [
    "CESD",
    "BDI",
    "PHQ9"
]
RATE_LIMIT_MAX_REQUESTS = 100
RATE_LIMIT_WINDOW_SECONDS = 60

# RUNTIME BUG:
# email_service imports these constants as part of the email boundary,
# but they were not defined here. That made the service fail during
# import and broke the dependency contract between services and shared
# constants.
EMAIL_VERIFICATION_SUBJECT = "Verify your email"
RESET_PASSWORD_SUBJECT = "Reset your password"
FRONTEND_BASE_URL = "http://localhost:3000"
