# =========================

# APPLICATION ENTRYPOINT

# =========================

run.py

* Responsibility:
  Starts the Flask application process. Loads environment variables, creates the Flask app through the application factory, and runs the development server when executed directly.

* Connected Layers:
  Connects the process entrypoint to the app factory in app/__init__.py and environment variables used by Flask runtime configuration.

* Functions:
  None physically present.

* Classes:
  None physically present.

app/__init__.py

* Responsibility:
  Defines the Flask application factory.

* Connected Layers:
  Connects Flask app construction to app/config.py. It currently loads configuration only; route blueprints, middleware, database lifecycle hooks, and error handlers are not registered here.

* Functions:
  create_app()

  * Creates a Flask app instance and applies the selected configuration object.

* Classes:
  None physically present.

app/config.py

* Responsibility:
  Selects the active runtime configuration class based on the ENVIRONMENT variable.

* Connected Layers:
  Connects environment-specific configuration classes from app/environments/dev.py and app/environments/prod.py to the Flask app factory and services that call load_config().

* Functions:
  load_config()

  * Returns DevelopmentConfig or ProductionConfig based on ENVIRONMENT, defaulting to development.

* Classes:
  None physically present.

# =========================

# ENVIRONMENT CONFIGURATION

# =========================

app/environments/dev.py

* Responsibility:
  Defines development configuration values loaded from environment variables.

* Connected Layers:
  Used by app/config.py and indirectly by the Flask app, database layer, JWT layer, rate limiting, and logging.

* Functions:
  None physically present.

* Classes:
  DevelopmentConfig

  * Holds development settings such as DEBUG, HOST, PORT, MONGODB_URI, DATABASE_NAME, JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES, RATE_LIMIT_PER_MINUTE, and LOG_LEVEL.

app/environments/prod.py

* Responsibility:
  Defines production configuration values loaded from environment variables.

* Connected Layers:
  Used by app/config.py and indirectly by the Flask app, database layer, JWT layer, rate limiting, and logging.

* Functions:
  None physically present.

* Classes:
  ProductionConfig

  * Holds production settings such as DEBUG, HOST, PORT, MONGODB_URI, DATABASE_NAME, JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES, RATE_LIMIT_PER_MINUTE, and LOG_LEVEL.

# =========================

# ROUTES

# =========================

app/routes/auth_routes.py

* Responsibility:
  Defines authentication HTTP routes and delegates request handling to auth controllers.

* Connected Layers:
  Connects Flask Blueprint routing to app/controllers/auth_controller.py.

* Endpoints:
  POST /auth/signup
  POST /auth/login
  GET /auth/google
  POST /auth/google/callback
  POST /auth/forgot-password
  POST /auth/reset-password
  POST /auth/verify-email
  GET /auth/me
  GET /auth/logout

* Functions:
  signup()

  * Delegates signup requests to signup_controller().

  login()

  * Delegates login requests to login_controller().

  google_login()

  * Delegates Google OAuth URL generation to google_login_controller().

  google_callback()

  * Delegates Google OAuth callback handling to google_callback_controller().

  forgot_password()

  * Delegates forgot-password requests to forgot_password_controller().

  reset_password()

  * Delegates password reset requests to reset_password_controller().

  verify_email()

  * Delegates email verification requests to verify_email_controller().

  get_current_user()

  * Delegates current-user profile requests to get_current_user_controller().

  logout()

  * Delegates logout requests to logout_controller().

  register_auth_routes()

  * Registers auth_blueprint on a Flask app.

* Classes:
  None physically present.

app/routes/prediction_routes.py

* Responsibility:
  Defines the ML prediction HTTP route and delegates handling to the prediction controller.

* Connected Layers:
  Connects Flask Blueprint routing to app/controllers/prediction_controller.py.

* Endpoints:
  POST /predict

* Functions:
  predict()

  * Delegates prediction requests to predict_controller().

  register_prediction_routes()

  * Registers prediction_blueprint on a Flask app.

* Classes:
  None physically present.

app/routes/history_routes.py

* Responsibility:
  Defines the authenticated prediction-history HTTP route and delegates handling to the history controller.

* Connected Layers:
  Connects Flask Blueprint routing to app/controllers/history_controller.py.

* Endpoints:
  GET /predictions/history

* Functions:
  get_prediction_history()

  * Delegates prediction history requests to get_prediction_history_controller().

  register_history_routes()

  * Registers history_blueprint on a Flask app.

* Classes:
  None physically present.

# =========================

# CONTROLLERS

# =========================

app/controllers/auth_controller.py

* Responsibility:
  Handles HTTP-level authentication request parsing, service calls, and API response formatting.

* Connected Layers:
  Connects Flask request data to app/services/auth_service.py, app/services/google_auth_service.py, and app/utils/response.py.

* Functions:
  signup_controller()

  * Reads signup JSON, calls signup_user(), and returns a success or error response.

  login_controller()

  * Reads login JSON, calls login_user(), and returns a success or error response.

  google_login_controller()

  * Calls generate_google_auth_url() and returns the OAuth URL response.

  google_callback_controller()

  * Reads callback JSON, calls process_google_login(), and returns a success or auth error response.

  forgot_password_controller()

  * Reads forgot-password JSON, calls forgot_password(), and returns a success or validation error response.

  reset_password_controller()

  * Reads reset-password JSON, calls reset_password(), and returns a success or validation error response.

  verify_email_controller()

  * Reads email verification JSON, calls verify_email(), and returns a success or validation error response.

  get_current_user_controller()

  * Reads the Authorization header, calls get_current_user(), and returns the current user response.

  logout_controller()

  * Calls logout_user() and returns a logout response.

* Classes:
  None physically present.

app/controllers/prediction_controller.py

* Responsibility:
  Handles HTTP-level prediction request parsing, prediction validation, ML prediction service invocation, optional history persistence, and API response formatting.

* Connected Layers:
  Connects Flask request/g context to app/validators/prediction_validator.py, app/services/prediction_service.py, and app/utils/response.py.

* Functions:
  predict_controller()

  * Reads prediction JSON, validates it, calls generate_prediction(), optionally saves history for g.current_user, and returns the prediction response.

* Classes:
  None physically present.

app/controllers/history_controller.py

* Responsibility:
  Handles authenticated prediction-history retrieval and response formatting.

* Connected Layers:
  Connects Flask g.current_user directly to app/repositories/prediction_repository.py, app/schemas/history_schema.py, and app/utils/response.py.

* Functions:
  get_prediction_history_controller()

  * Checks authentication context, retrieves prediction history, serializes it, and returns the API response.

* Classes:
  None physically present.

# =========================

# SERVICES

# =========================

app/services/auth_service.py

* Responsibility:
  Coordinates authentication use cases including signup, login, current-user lookup, logout, password reset, and email verification.

* Connected Layers:
  Connects validators, repositories, JWT generation/verification, email service, and password/token security utilities.

* Functions:
  signup_user()

  * Validates signup data, checks existing users, hashes passwords, creates users, sends verification email, and creates an access token.

  login_user()

  * Validates login data, finds user by email, verifies password, and creates an access token.

  get_current_user()

  * Verifies a token and fetches the current user by email.

  logout_user()

  * Returns a successful logout result without server-side token invalidation.

  forgot_password()

  * Finds a user by email, creates a reset token, and sends a reset email.

  reset_password()

  * Verifies a reset token, hashes a new password, and updates the user document.

  verify_email()

  * Verifies an email verification token and marks the user as verified.

* Classes:
  None physically present.

app/services/prediction_service.py

* Responsibility:
  Orchestrates prediction processing from request features through preprocessing, ML inference, confidence analysis, response serialization, and history persistence helper logic.

* Connected Layers:
  Connects app repositories, schemas, logging service, ML preprocessing, ML inference, and ML confidence analysis.

* Functions:
  generate_prediction()

  * Maps input features, normalizes them, runs model inference, aggregates ensemble output, calculates confidence/agreement, and builds the prediction response.

  process_prediction()

  * Converts ensemble output and confidence metadata into response-building arguments.

  build_prediction_response()

  * Calls serialize_prediction_response() to create a standardized API prediction payload.

  save_prediction_history()

  * Persists a prediction through save_prediction() and logs prediction activity.

* Classes:
  None physically present.

app/services/jwt_service.py

* Responsibility:
  Provides JWT creation, decoding, verification, and Authorization header token extraction.

* Connected Layers:
  Connects authentication services, decorators, and middleware to PyJWT and app configuration.

* Functions:
  create_access_token()

  * Creates a JWT access token with type, exp, and iat claims.

  create_refresh_token()

  * Creates a JWT refresh token with type, exp, and iat claims.

  decode_token()

  * Decodes a JWT and returns payload or None for expired/invalid tokens.

  verify_token()

  * Decodes a token and verifies the expected token type.

  extract_token()

  * Extracts a Bearer token from a Flask Request Authorization header.

* Classes:
  None physically present.

app/services/email_service.py

* Responsibility:
  Builds and sends authentication-related emails and logs email outcomes.

* Connected Layers:
  Connects external SMTP client, auth logging, timestamp helper, and email/frontend constants.

* Functions:
  send_email()

  * Sends a generic email through send_email_message() and logs success or failure.

  build_verification_email_body()

  * Builds the body for account verification email.

  build_reset_password_email_body()

  * Builds the body for password reset email.

  send_verification_email()

  * Builds and sends an account verification email.

  send_reset_password_email()

  * Builds and sends a password reset email.

* Classes:
  None physically present.

app/services/google_auth_service.py

* Responsibility:
  Coordinates Google OAuth login/signup flow.

* Connected Layers:
  Connects Google OAuth external API helpers, user repository, and JWT service.

* Functions:
  generate_google_auth_url()

  * Returns the Google OAuth authorization URL base.

  verify_google_token()

  * Exchanges an auth code for an access token and fetches Google user information.

  process_google_login()

  * Validates Google account data, finds or creates a local user, and creates an access token.

* Classes:
  None physically present.

app/services/logging_service.py

* Responsibility:
  Centralizes request, error, authentication, and prediction logging.

* Connected Layers:
  Connects middleware and services to logger creation in app/utils/logger.py.

* Functions:
  log_request()

  * Writes request metadata to the request logger.

  log_error()

  * Writes structured error payloads to the error logger.

  log_auth_event()

  * Writes authentication event details to the auth logger.

  log_prediction()

  * Writes prediction activity to the request logger.

* Classes:
  None physically present.

app/services/rate_limit_service.py

* Responsibility:
  Implements in-memory request counting for rate limiting by client IP.

* Connected Layers:
  Connects rate-limit middleware to rate-limit constants and Flask Request metadata.

* Functions:
  get_client_ip()

  * Resolves the client IP from X-Forwarded-For or request.remote_addr.

  cleanup_expired_requests()

  * Removes timestamps outside the rate-limit window.

  check_rate_limit()

  * Checks whether the current request count is below the configured limit.

  update_rate_limit()

  * Adds the current request timestamp for the client IP.

* Classes:
  None physically present.

# =========================

# REPOSITORIES

# =========================

app/repositories/user_repository.py

* Responsibility:
  Encapsulates persistence operations for user documents.

* Connected Layers:
  Connects auth services and auth middleware to MongoDB users collection access and timestamp helpers.

* Database Operations:
  users insert_one
  users find_one by email
  users find_one by ObjectId
  users update_one by ObjectId
  users update_one for email verification

* Functions:
  create_user()

  * Creates a user document, inserts it into MongoDB, and serializes the inserted user.

  find_user_by_email()

  * Finds a user by email and serializes it with password included.

  find_user_by_id()

  * Finds a user by MongoDB ObjectId and serializes it without password.

  update_user()

  * Applies field updates and updated_at to a user document.

  verify_user_email()

  * Marks a user document as verified.

  serialize_user()

  * Converts a MongoDB user document into an API-safe dictionary, optionally including password.

* Classes:
  None physically present.

app/repositories/prediction_repository.py

* Responsibility:
  Encapsulates persistence operations for prediction-history documents.

* Connected Layers:
  Connects prediction/history service or controller code to MongoDB predictions collection access and timestamp helpers.

* Database Operations:
  predictions insert_one
  predictions find by user_id sorted by created_at descending with limit
  predictions find_one by ObjectId

* Functions:
  save_prediction()

  * Creates and inserts a prediction document, then serializes it.

  get_prediction_history()

  * Retrieves recent prediction documents for a user.

  get_prediction_by_id()

  * Retrieves one prediction document by MongoDB ObjectId.

  serialize_prediction()

  * Converts a MongoDB prediction document into an API-safe dictionary.

* Classes:
  None physically present.

# =========================

# DATABASE

# =========================

app/database/database.py

* Responsibility:
  Manages MongoDB client creation, database retrieval, and client shutdown.

* Connected Layers:
  Connects repository collection helpers to Flask current_app database configuration and PyMongo.

* Functions:
  connect_database()

  * Lazily creates and returns a MongoClient using current_app.config["MONGODB_URI"].

  get_db()

  * Returns the configured MongoDB database from the shared client.

  close_database()

  * Closes and clears the shared MongoDB client.

* Classes:
  None physically present.

app/database/collections.py

* Responsibility:
  Provides named MongoDB collection accessors.

* Connected Layers:
  Connects repositories to get_db() without exposing database selection details.

* Functions:
  users_collection()

  * Returns the users collection from the configured database.

  predictions_collection()

  * Returns the predictions collection from the configured database.

* Classes:
  None physically present.

# =========================

# MIDDLEWARE

# =========================

app/middleware/auth_middleware.py

* Responsibility:
  Authenticates protected requests and attaches the current user to Flask g.

* Connected Layers:
  Connects request lifecycle authentication to JWT service and user repository.

* Request Lifecycle Impact:
  Intended as before_request middleware. It skips public auth routes, rejects missing/invalid tokens, loads the user, and stores g.current_user for downstream controllers/services.

* Functions:
  authenticate_request()

  * Validates protected request tokens and attaches the authenticated user.

  attach_current_user()

  * Stores the user dictionary on g.current_user.

* Classes:
  None physically present.

app/middleware/error_middleware.py

* Responsibility:
  Converts validation, authentication, and server errors into JSON responses while logging them.

* Connected Layers:
  Connects Flask error handling to logging_service.

* Request Lifecycle Impact:
  Intended for Flask errorhandler registration. It standardizes error responses for validation, auth, and unexpected server exceptions.

* Functions:
  handle_validation_error()

  * Logs validation errors and returns a 400 JSON response.

  handle_auth_error()

  * Logs authentication errors and returns a 401 JSON response.

  handle_server_error()

  * Logs unexpected server errors and returns a 500 JSON response.

* Classes:
  None physically present.

app/middleware/logging_middleware.py

* Responsibility:
  Logs inbound request metadata and outbound response metadata.

* Connected Layers:
  Connects Flask request/response lifecycle to logging_service.

* Request Lifecycle Impact:
  Intended as before_request and after_request middleware. It records start time, request metadata, status code, and duration.

* Functions:
  log_request_middleware()

  * Stores request start time and logs incoming request metadata.

  log_response_middleware()

  * Logs response status and request duration, then returns the response.

* Classes:
  None physically present.

app/middleware/rate_limit_middleware.py

* Responsibility:
  Applies global request throttling based on client IP.

* Connected Layers:
  Connects Flask request lifecycle to rate_limit_service.

* Request Lifecycle Impact:
  Intended as before_request middleware. It blocks excessive requests with HTTP 429 and updates the in-memory request counter for allowed requests.

* Functions:
  rate_limit_middleware()

  * Checks whether a client IP is allowed and records the request if allowed.

* Classes:
  None physically present.

app/middleware/security_middleware.py

* Responsibility:
  Adds security headers and sanitizes string values in incoming JSON payloads.

* Connected Layers:
  Connects Flask request/response lifecycle to app/utils/security.py.

* Request Lifecycle Impact:
  sanitize_request() is intended before controllers run. apply_security_headers() is intended after responses are created.

* Functions:
  apply_security_headers()

  * Adds standard security headers to outgoing responses.

  sanitize_request()

  * Creates request.sanitized_json from sanitized string fields in JSON payloads.

* Classes:
  None physically present.

# =========================

# DECORATORS

# =========================

app/decorators/jwt_decorator.py

* Responsibility:
  Provides route decorators for required or optional JWT authentication.

* Connected Layers:
  Connects route functions to JWT extraction/verification and Flask g.current_user.

* Functions:
  jwt_required()

  * Builds a decorator that blocks requests without a valid access token and stores decoded payload on g.current_user.

  optional_jwt()

  * Builds a decorator that stores decoded payload when valid and otherwise allows the request with g.current_user set to None.

* Classes:
  None physically present.

app/decorators/role_decorator.py

* Responsibility:
  Provides route-level role authorization.

* Connected Layers:
  Connects authenticated user context from Flask g to role-protected route execution.

* Functions:
  role_required()

  * Builds a decorator that permits only users whose role is in allowed_roles.

* Classes:
  None physically present.

# =========================

# VALIDATORS

# =========================

app/validators/auth_validator.py

* Responsibility:
  Validates authentication request payloads.

* Connected Layers:
  Used by auth_service before repository and security operations.

* Functions:
  validate_signup_data()

  * Checks required signup fields, email format, and password rules.

  validate_login_data()

  * Checks required login fields.

  validate_email()

  * Validates email syntax using EMAIL_REGEX.

  validate_password()

  * Validates password length rules.

* Classes:
  None physically present.

app/validators/prediction_validator.py

* Responsibility:
  Coordinates prediction input validation.

* Connected Layers:
  Connects prediction_controller to type_validator and range_validator.

* Functions:
  validate_prediction_input()

  * Runs required-feature, numeric-field, and range validation for prediction payloads.

  validate_required_features()

  * Checks that required ML feature keys exist in the payload.

* Classes:
  None physically present.

app/validators/normalization_validator.py

* Responsibility:
  Validates normalized feature values and scaled ranges.

* Connected Layers:
  Intended to support ML preprocessing validation; not currently imported by production prediction flow.

* Functions:
  validate_normalized_input()

  * Detects nonnumeric, NaN, and infinite normalized values.

  validate_feature_scaling()

  * Checks normalized numeric values against configured min/max bounds.

* Classes:
  None physically present.

app/validators/range_validator.py

* Responsibility:
  Validates numeric feature and score bounds.

* Connected Layers:
  Used by prediction_validator for feature ranges and available for confidence/probability score validation.

* Functions:
  validate_feature_ranges()

  * Checks configured feature min/max ranges.

  validate_score_limits()

  * Checks confidence/probability score min/max range.

* Classes:
  None physically present.

app/validators/type_validator.py

* Responsibility:
  Validates input datatypes.

* Connected Layers:
  Used by prediction_validator to validate numeric fields.

* Functions:
  validate_input_types()

  * Validates fields against expected Python types.

  validate_numeric_fields()

  * Ensures configured fields are int or float and rejects bool.

* Classes:
  None physically present.

# =========================

# SCHEMAS

# =========================

app/schemas/auth_schema.py

* Responsibility:
  Serializes authentication-related response payloads.

* Connected Layers:
  Intended to sit between auth services/controllers and API responses; not currently imported by production auth flow.

* Functions:
  serialize_user()

  * Creates a minimal user response dictionary with id, name, and email.

  serialize_auth_response()

  * Creates a response dictionary containing message, token, and serialized user.

* Classes:
  None physically present.

app/schemas/prediction_schema.py

* Responsibility:
  Serializes ML model output and final prediction responses.

* Connected Layers:
  Used by prediction_service to create API-facing prediction payloads.

* Functions:
  serialize_model_output()

  * Serializes one model prediction with confidence and model name.

  serialize_prediction_response()

  * Serializes final prediction, confidence score, severity, and optional recommendation.

* Classes:
  None physically present.

app/schemas/history_schema.py

* Responsibility:
  Serializes prediction-history records.

* Connected Layers:
  Used by history_controller after repository retrieval.

* Functions:
  serialize_prediction_history()

  * Converts prediction records into a history response list.

* Classes:
  None physically present.

# =========================

# EXTERNAL APIS

# =========================

app/external_apis/email_client.py

* Responsibility:
  Encapsulates SMTP connection and low-level email sending.

* Connected Layers:
  Used by email_service to send verification and password reset messages.

* Functions:
  connect_smtp_server()

  * Creates an SMTP connection, starts TLS, and logs into the SMTP server.

  send_email_message()

  * Builds a MIME email message, sends it through SMTP, and closes the server connection.

* Classes:
  None physically present.

app/external_apis/google_oauth.py

* Responsibility:
  Encapsulates Google OAuth provider discovery, token exchange, and userinfo retrieval.

* Connected Layers:
  Used by google_auth_service as the external boundary for Google OAuth.

* Functions:
  get_google_provider_config()

  * Fetches Google's OpenID provider configuration.

  exchange_auth_code()

  * Exchanges an authorization code for a Google access token.

  get_google_user_info()

  * Fetches Google user profile data using an access token.

* Classes:
  None physically present.

# =========================

# UTILITIES

# =========================

app/utils/constants.py

* Responsibility:
  Stores shared constants for model names, severity labels, JWT algorithm, rate limits, and supported test types.

* Connected Layers:
  Used by rate_limit_service and intended for shared configuration-like constants across services.

* Functions:
  None physically present.

* Classes:
  None physically present.

app/utils/helpers.py

* Responsibility:
  Provides small general-purpose helpers for IDs and datetime formatting.

* Connected Layers:
  Used by repositories and email service for timestamps and IDs.

* Functions:
  generate_uuid()

  * Generates a UUID string.

  get_current_timestamp()

  * Returns the current UTC timestamp as an ISO string.

  format_datetime()

  * Formats a datetime as a human-readable string.

* Classes:
  None physically present.

app/utils/logger.py

* Responsibility:
  Creates named Python loggers.

* Connected Layers:
  Used by logging_service to initialize request, error, and auth loggers.

* Functions:
  setup_logger()

  * Configures and returns a named logger with a stream handler.

  get_logger()

  * Returns a configured logger by name.

* Classes:
  None physically present.

app/utils/response.py

* Responsibility:
  Standardizes success and error JSON responses.

* Connected Layers:
  Used by controllers to return consistent Flask responses.

* Functions:
  success_response()

  * Returns a JSON success response with message, data, and status code.

  error_response()

  * Returns a JSON error response with message, errors, and status code.

* Classes:
  None physically present.

app/utils/security.py

* Responsibility:
  Provides password hashing, password verification, secure token generation, and simple string sanitization.

* Connected Layers:
  Used by auth_service and security_middleware.

* Functions:
  hash_password()

  * Hashes a plaintext password with bcrypt.

  verify_password()

  * Verifies a plaintext password against a bcrypt hash.

  generate_secure_token()

  * Generates a random token using secrets.token_hex().

  sanitize_input()

  * Trims surrounding whitespace from string input.

* Classes:
  None physically present.

# =========================

# ML MODELS

# =========================

ml/models/__init__.py

* Responsibility:
  Defines filesystem locations for trained model artifacts and feature-order artifacts.

* Connected Layers:
  Used by ml/inference/model_loader.py.

* Model Purpose / Inference Role:
  Provides artifact paths, not inference logic.

* Functions:
  None physically present.

* Classes:
  None physically present.

ml/models/feature_orders/__init__.py

* Responsibility:
  Defines the feature-orders directory path.

* Connected Layers:
  Supports model_loader artifact discovery.

* Model Purpose / Inference Role:
  Identifies where feature-order pickle files live.

* Functions:
  None physically present.

* Classes:
  None physically present.

ml/models/trained_models/__init__.py

* Responsibility:
  Defines the trained-models directory path.

* Connected Layers:
  Supports model_loader artifact discovery.

* Model Purpose / Inference Role:
  Identifies where trained model pickle files live.

* Functions:
  None physically present.

* Classes:
  None physically present.

# =========================

# ML PREPROCESSING

# =========================

ml/preprocessing/feature_mapper.py

* Responsibility:
  Converts raw API feature input into pandas DataFrame format and aligns columns to model feature order.

* Connected Layers:
  Used by prediction_service and compatible with model feature orders loaded by model_loader.

* Model Purpose / Inference Role:
  Prepares inference input shape and ordering before predictor functions call model.predict().

* Functions:
  map_features()

  * Wraps raw input data as a single-row pandas DataFrame.

  align_feature_order()

  * Validates required columns and returns the DataFrame ordered for the model.

* Classes:
  None physically present.

ml/preprocessing/feature_selector.py

* Responsibility:
  Selects predefined feature subsets from a DataFrame.

* Connected Layers:
  Intended to support ML preprocessing before inference; not currently imported by production prediction flow.

* Model Purpose / Inference Role:
  Provides X1 and X3 feature-set slicing for models trained on different feature groups.

* Functions:
  select_x1_features()

  * Returns a DataFrame containing X1_FEATURES columns.

  select_x3_features()

  * Returns a DataFrame containing X3_FEATURES columns.

* Classes:
  None physically present.

ml/preprocessing/normalizer.py

* Responsibility:
  Applies MinMax scaling to feature DataFrames.

* Connected Layers:
  Used by prediction_service before inference and depends on scikit-learn preprocessing.

* Model Purpose / Inference Role:
  Produces normalized numeric model input and optionally reuses a provided scaler.

* Functions:
  normalize_features()

  * Fits or applies a MinMaxScaler and returns normalized DataFrame plus scaler.

  scale_features()

  * Applies an existing scaler to a DataFrame.

* Classes:
  None physically present.

# =========================

# ML INFERENCE

# =========================

ml/inference/model_loader.py

* Responsibility:
  Loads trained ML models and feature-order metadata from pickle artifacts into in-memory registries.

* Connected Layers:
  Connects filesystem model artifacts under ml/models to ensemble_predictor lookup functions.

* Model Purpose / Inference Role:
  Central model-loading boundary. It performs direct joblib.load() artifact loading outside endpoint/controller code.

* Functions:
  _build_model_key()

  * Builds standardized registry keys from model type, feature set, and test type.

  load_models()

  * Loads all trained model pickle files into MODELS.

  load_feature_orders()

  * Loads all feature-order pickle files into FEATURE_ORDERS.

  get_model()

  * Retrieves a loaded model by model type, feature set, and test type.

  get_feature_order()

  * Retrieves a loaded feature order by feature set and test type.

  get_loaded_models()

  * Returns the loaded model registry.

  initialize_ml_models()

  * Loads all models and feature orders for the inference layer.

* Classes:
  None physically present.

ml/inference/svm_predictor.py

* Responsibility:
  Runs SVM model prediction and probability inference.

* Connected Layers:
  Used by ensemble_predictor after model_loader returns an SVM model and feature order.

* Model Purpose / Inference Role:
  Converts ordered input data to a pandas DataFrame and calls SVM predict/predict_proba.

* Functions:
  predict_svm()

  * Produces an integer SVM prediction.

  predict_svm_probability()

  * Produces the maximum SVM prediction probability.

* Classes:
  None physically present.

ml/inference/logistic_predictor.py

* Responsibility:
  Runs Logistic Regression model prediction and probability inference.

* Connected Layers:
  Used by ensemble_predictor after model_loader returns a logistic regression model and feature order.

* Model Purpose / Inference Role:
  Converts ordered input data to a pandas DataFrame and calls Logistic Regression predict/predict_proba.

* Functions:
  predict_logistic()

  * Produces an integer Logistic Regression prediction.

  predict_logistic_probability()

  * Produces the maximum Logistic Regression prediction probability.

* Classes:
  None physically present.

ml/inference/randomforest_predictor.py

* Responsibility:
  Runs Random Forest model prediction and probability inference.

* Connected Layers:
  Used by ensemble_predictor after model_loader returns a Random Forest model and feature order.

* Model Purpose / Inference Role:
  Converts ordered input data to a pandas DataFrame and calls Random Forest predict/predict_proba.

* Functions:
  predict_randomforest()

  * Produces an integer Random Forest prediction.

  predict_randomforest_probability()

  * Produces the maximum Random Forest prediction probability.

* Classes:
  None physically present.

ml/inference/confidence_analyzer.py

* Responsibility:
  Converts probabilities and model prediction lists into confidence and agreement metadata.

* Connected Layers:
  Used by ensemble_predictor and imported by prediction_service.

* Model Purpose / Inference Role:
  Interprets inference outputs into API-level confidence and ensemble agreement information.

* Functions:
  calculate_confidence()

  * Maps a probability score to rounded score and confidence level.

  calculate_agreement_strength()

  * Calculates majority prediction, agreement ratio, agreement strength, and distribution.

* Classes:
  None physically present.

ml/inference/ensemble_predictor.py

* Responsibility:
  Coordinates running multiple model types and aggregating their predictions.

* Connected Layers:
  Connects model_loader, individual predictor modules, and confidence_analyzer.

* Model Purpose / Inference Role:
  Acts as the ensemble inference orchestrator for SVM, Logistic Regression, and Random Forest models.

* Functions:
  run_all_models()

  * Retrieves feature order and model instances, runs each selected predictor, and returns individual model results.

  aggregate_predictions()

  * Aggregates individual model predictions and confidence scores into final ensemble metadata.

  generate_ensemble_output()

  * Runs all requested models and returns individual results plus aggregate ensemble result.

* Classes:
  None physically present.

# =========================

# ML EXPLAINABILITY

# =========================

ml/explainability/consensus_explainer.py

* Responsibility:
  Placeholder module for consensus explanation behavior.

* Connected Layers:
  Not currently connected to production code.

* Model Purpose / Inference Role:
  No inference or explanation logic is physically present.

* Functions:
  None physically present.

* Classes:
  None physically present.

ml/explainability/feature_importance.py

* Responsibility:
  Placeholder module for feature-importance explanation behavior.

* Connected Layers:
  Not currently connected to production code.

* Model Purpose / Inference Role:
  No inference or explanation logic is physically present.

* Functions:
  None physically present.

* Classes:
  None physically present.

ml/explainability/severity_explainer.py

* Responsibility:
  Placeholder module for severity explanation behavior.

* Connected Layers:
  Not currently connected to production code.

* Model Purpose / Inference Role:
  No inference or explanation logic is physically present.

* Functions:
  None physically present.

* Classes:
  None physically present.

# =========================

# ARCHITECTURE VIOLATIONS

# =========================

Business logic inside routes

* No route file contains verified business logic. The route functions are thin delegators to controllers.

Business logic inside controllers

* app/controllers/prediction_controller.py performs validation and authenticated history persistence orchestration. In a strict clean architecture design, the controller would pass request data to an application service and let that service coordinate validation, prediction generation, and persistence decisions.

Database access inside controllers

* app/controllers/history_controller.py imports get_prediction_history() directly from app/repositories/prediction_repository.py. This bypasses a service/use-case layer and couples the controller to persistence.

Circular imports

* No circular imports were found in the production app/ml import graph.

Duplicated validation or serialization logic

* app/repositories/user_repository.py and app/schemas/auth_schema.py both serialize user data. That creates two user response shapes in different layers.
* app/repositories/prediction_repository.py and app/schemas/history_schema.py both reshape prediction-history data, which mixes persistence serialization and API serialization.

Oversized service files

* No clearly oversized service file was found by file count alone. app/services/auth_service.py is the broadest service and coordinates validation, security, repository access, email, and token generation; it may become oversized as more auth workflows are added.

Mixed concerns

* app/services/auth_service.py mixes validation, password hashing, token creation, email triggering, and persistence orchestration in one module.
* app/services/prediction_service.py mixes preprocessing orchestration, ML inference orchestration, confidence analysis, response serialization, and persistence helper behavior.
* app/middleware/auth_middleware.py directly imports the user repository. Middleware usually should verify request identity through an auth service instead of touching persistence.
* app/database/collections.py exposes collection accessors as functions, but repositories use users_collection.insert_one and predictions_collection.insert_one as if they were collection objects. This is a boundary/interface mismatch at the persistence layer.

Direct model loading inside endpoints

* No direct model loading was found inside route or controller endpoints. Model loading is centralized in ml/inference/model_loader.py through joblib.load().

Additional contract issues affecting architecture boundaries

* app/services/jwt_service.py expects config attributes JWT_SECRET, JWT_ALGORITHM, JWT_ACCESS_EXPIRATION, and JWT_REFRESH_EXPIRATION, but the environment config classes define JWT_SECRET_KEY and JWT_ACCESS_TOKEN_EXPIRES.
* app/services/logging_service.py calls get_logger() with a log-file path argument, but app/utils/logger.py defines get_logger(name) with one parameter.
* app/middleware/logging_middleware.py calls log_request() with a dictionary, but app/services/logging_service.py defines log_request(method, endpoint, ip_address, status_code).
* app/middleware/rate_limit_middleware.py expects check_rate_limit() to return is_allowed and retry_after, but app/services/rate_limit_service.py returns only a boolean.
* app/services/auth_service.py expects validate_signup_data() and validate_login_data() to return dictionaries with a valid key, but app/validators/auth_validator.py returns lists of errors.
* app/controllers/reset_password_controller() and verify_email_controller() pass request JSON dictionaries into service functions that physically expect token/new_password or token arguments.
* app/services/email_service.py imports EMAIL_VERIFICATION_SUBJECT, RESET_PASSWORD_SUBJECT, and FRONTEND_BASE_URL, but app/utils/constants.py does not define those constants.
* app/services/prediction_service.py calls run_all_models(), generate_ensemble_output(), calculate_confidence(), calculate_agreement_strength(), serialize_prediction_response(), save_prediction(), and log_prediction() with argument shapes that do not match the physically present function signatures.
