# Architecture Reference v1

Generated from a recursive scan of every current backend `.py` file. Placeholder modules are marked explicitly; tests are documented as test/support architecture, not production runtime code.

# =========================
# APPLICATION ENTRYPOINTS
# =========================

run.py

* Responsibility:
  Entrypoint that loads environment variables, creates the Flask app, and starts the server when executed directly.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  None.

* Classes:
  None.

app/__init__.py

* Responsibility:
  Application factory. It creates Flask and loads config; current code does not register routes, middleware, database hooks, or ML initialization.

* Connected Layers:
  Runtime composition root -> config; expected to wire routes/middleware/database/ML.

* Functions:
  create_app()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.

* Classes:
  None.

app/config.py

* Responsibility:
  Configuration boundary sourced from environment variables.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  load_config()
  * Loads or exposes runtime configuration/artifact state.

* Classes:
  None.

app/environments/dev.py

* Responsibility:
  Configuration boundary sourced from environment variables.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  None.

* Classes:
  DevelopmentConfig
  * Class physically present in this file.

app/environments/prod.py

* Responsibility:
  Configuration boundary sourced from environment variables.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  None.

* Classes:
  ProductionConfig
  * Class physically present in this file.

# =========================
# HTTP ROUTES
# =========================

app/routes/auth_routes.py

* Responsibility:
  Route registration layer. It declares Flask Blueprint endpoints and delegates to controllers.

* Connected Layers:
  Flask Blueprint -> controller.

* Endpoints:
  auth_blueprint.route('/signup', methods=['POST'])
  * delegates through signup().
  auth_blueprint.route('/login', methods=['POST'])
  * delegates through login().
  auth_blueprint.route('/google', methods=['GET'])
  * delegates through google_login().
  auth_blueprint.route('/google/callback', methods=['POST'])
  * delegates through google_callback().
  auth_blueprint.route('/forgot-password', methods=['POST'])
  * delegates through forgot_password().
  auth_blueprint.route('/reset-password', methods=['POST'])
  * delegates through reset_password().
  auth_blueprint.route('/verify-email', methods=['POST'])
  * delegates through verify_email().
  auth_blueprint.route('/me', methods=['GET'])
  * delegates through get_current_user().
  auth_blueprint.route('/logout', methods=['GET'])
  * delegates through logout().

* Functions:
  signup()
  * Function physically present in the current codebase.
  login()
  * Function physically present in the current codebase.
  google_login()
  * Function physically present in the current codebase.
  google_callback()
  * Function physically present in the current codebase.
  forgot_password()
  * Function physically present in the current codebase.
  reset_password()
  * Function physically present in the current codebase.
  verify_email()
  * Updates, persists, or verifies data at the file boundary.
  get_current_user()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  logout()
  * Function physically present in the current codebase.
  register_auth_routes()
  * Registers this blueprint on a Flask app.

* Classes:
  None.

app/routes/history_routes.py

* Responsibility:
  Route registration layer. It declares Flask Blueprint endpoints and delegates to controllers.

* Connected Layers:
  Flask Blueprint -> controller.

* Endpoints:
  history_blueprint.route('/history', methods=['GET'])
  * delegates through get_prediction_history().

* Functions:
  get_prediction_history()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  register_history_routes()
  * Registers this blueprint on a Flask app.

* Classes:
  None.

app/routes/prediction_routes.py

* Responsibility:
  Route registration layer. It declares Flask Blueprint endpoints and delegates to controllers.

* Connected Layers:
  Flask Blueprint -> controller.

* Endpoints:
  prediction_blueprint.route('/predict', methods=['POST'])
  * delegates through predict().

* Functions:
  predict()
  * Function physically present in the current codebase.
  register_prediction_routes()
  * Registers this blueprint on a Flask app.

* Classes:
  None.

# =========================
# CONTROLLERS
# =========================

app/controllers/auth_controller.py

* Responsibility:
  HTTP controller layer. It reads Flask request/context data, delegates to services, and wraps responses.

* Connected Layers:
  Route -> controller -> service -> response utility.

* Functions:
  signup_controller()
  * HTTP controller function that delegates business work to services.
  login_controller()
  * HTTP controller function that delegates business work to services.
  google_login_controller()
  * HTTP controller function that delegates business work to services.
  google_callback_controller()
  * HTTP controller function that delegates business work to services.
  forgot_password_controller()
  * HTTP controller function that delegates business work to services.
  reset_password_controller()
  * HTTP controller function that delegates business work to services.
  verify_email_controller()
  * HTTP controller function that delegates business work to services.
  get_current_user_controller()
  * HTTP controller function that delegates business work to services.
  logout_controller()
  * HTTP controller function that delegates business work to services.

* Classes:
  None.

app/controllers/history_controller.py

* Responsibility:
  HTTP controller layer. It reads Flask request/context data, delegates to services, and wraps responses.

* Connected Layers:
  Route -> controller -> service -> response utility.

* Functions:
  get_prediction_history_controller()
  * HTTP controller function that delegates business work to services.

* Classes:
  None.

app/controllers/prediction_controller.py

* Responsibility:
  HTTP controller layer. It reads Flask request/context data, delegates to services, and wraps responses.

* Connected Layers:
  Route -> controller -> service -> response utility.

* Functions:
  predict_controller()
  * Runs model-specific prediction or probability inference.

* Classes:
  None.

# =========================
# MIDDLEWARE AND DECORATORS
# =========================

app/decorators/jwt_decorator.py

* Responsibility:
  Route decorator boundary for authentication or authorization checks.

* Connected Layers:
  Route wrapper -> JWT/role service/context checks.

* Functions:
  jwt_required()
  * Function physically present in the current codebase.
  optional_jwt()
  * Function physically present in the current codebase.
  decorator()
  * Function physically present in the current codebase.
  decorator()
  * Function physically present in the current codebase.
  wrapper()
  * Function physically present in the current codebase.
  wrapper()
  * Function physically present in the current codebase.

* Classes:
  None.

app/decorators/role_decorator.py

* Responsibility:
  Route decorator boundary for authentication or authorization checks.

* Connected Layers:
  Route wrapper -> JWT/role service/context checks.

* Functions:
  role_required()
  * Function physically present in the current codebase.
  decorator()
  * Function physically present in the current codebase.
  wrapper()
  * Function physically present in the current codebase.

* Classes:
  None.

app/middleware/auth_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Functions:
  authenticate_request()
  * Function physically present in the current codebase.
  attach_current_user()
  * Function physically present in the current codebase.

* Classes:
  None.

app/middleware/error_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Functions:
  handle_validation_error()
  * Handles an error or lifecycle event and returns a response.
  handle_auth_error()
  * Handles an error or lifecycle event and returns a response.
  handle_server_error()
  * Handles an error or lifecycle event and returns a response.

* Classes:
  None.

app/middleware/logging_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Functions:
  log_response()
  * Records request, response, error, auth, or prediction activity.
  log_request_middleware()
  * Records request, response, error, auth, or prediction activity.
  log_response_middleware()
  * Records request, response, error, auth, or prediction activity.

* Classes:
  None.

app/middleware/rate_limit_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Functions:
  rate_limit_middleware()
  * Function physically present in the current codebase.

* Classes:
  None.

app/middleware/security_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Functions:
  apply_security_headers()
  * Function physically present in the current codebase.
  sanitize_request()
  * Function physically present in the current codebase.

* Classes:
  None.

tests/middleware/test_auth_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Endpoints:
  app.route('/protected')
  * delegates through protected_route().

* Functions:
  create_test_app()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  test_missing_authorization_header()
  * Test function asserting behavior or a contract in this file scope.
  test_invalid_authorization_format()
  * Test function asserting behavior or a contract in this file scope.
  test_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_valid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_authenticated_user_attached()
  * Test function asserting behavior or a contract in this file scope.
  test_empty_bearer_token()
  * Test function asserting behavior or a contract in this file scope.
  protected_route()
  * Function physically present in the current codebase.

* Classes:
  None.

tests/middleware/test_error_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Functions:
  create_test_app()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  test_handle_validation_error()
  * Test function asserting behavior or a contract in this file scope.
  test_handle_auth_error()
  * Test function asserting behavior or a contract in this file scope.
  test_handle_server_error()
  * Test function asserting behavior or a contract in this file scope.
  test_validation_error_response_type()
  * Test function asserting behavior or a contract in this file scope.
  test_auth_error_response_type()
  * Test function asserting behavior or a contract in this file scope.
  test_server_error_hides_internal_details()
  * Test function asserting behavior or a contract in this file scope.
  test_server_error_response_type()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  MockValidationError
  * Class physically present in this file.
  MockAuthError
  * Class physically present in this file.

tests/middleware/test_logging_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Endpoints:
  app.route('/health')
  * delegates through health_check().

* Functions:
  create_test_app()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  test_log_request_called()
  * Test function asserting behavior or a contract in this file scope.
  test_log_response_called()
  * Test function asserting behavior or a contract in this file scope.
  test_log_response_returns_response()
  * Test function asserting behavior or a contract in this file scope.
  test_request_logging_does_not_crash()
  * Test function asserting behavior or a contract in this file scope.
  test_response_logging_does_not_crash()
  * Test function asserting behavior or a contract in this file scope.
  test_request_logging_with_headers()
  * Test function asserting behavior or a contract in this file scope.
  test_response_logging_status_code()
  * Test function asserting behavior or a contract in this file scope.
  health_check()
  * Function physically present in the current codebase.

* Classes:
  None.

tests/middleware/test_rate_limit_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Endpoints:
  app.route('/predict')
  * delegates through predict().

* Functions:
  create_test_app()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  test_request_allowed()
  * Test function asserting behavior or a contract in this file scope.
  test_request_blocked()
  * Test function asserting behavior or a contract in this file scope.
  test_rate_limit_uses_client_ip()
  * Test function asserting behavior or a contract in this file scope.
  test_rate_limit_response_is_json()
  * Test function asserting behavior or a contract in this file scope.
  test_rate_limit_allows_multiple_valid_requests()
  * Test function asserting behavior or a contract in this file scope.
  test_rate_limit_handles_missing_ip()
  * Test function asserting behavior or a contract in this file scope.
  test_rate_limit_middleware_does_not_modify_successful_requests()
  * Test function asserting behavior or a contract in this file scope.
  predict()
  * Function physically present in the current codebase.

* Classes:
  None.

tests/middleware/test_security_middleware.py

* Responsibility:
  Flask request lifecycle middleware that affects request/response processing before or after controller execution.

* Connected Layers:
  Flask lifecycle -> middleware -> service or utility -> response/context.

* Endpoints:
  app.route('/health')
  * delegates through health().

* Functions:
  create_test_app()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  test_apply_security_headers()
  * Test function asserting behavior or a contract in this file scope.
  test_security_headers_return_response()
  * Test function asserting behavior or a contract in this file scope.
  test_sanitize_request_safe_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_sanitize_request_script_injection()
  * Test function asserting behavior or a contract in this file scope.
  test_sanitize_request_sql_injection()
  * Test function asserting behavior or a contract in this file scope.
  test_sanitize_request_handles_empty_json()
  * Test function asserting behavior or a contract in this file scope.
  test_sanitize_request_handles_missing_json()
  * Test function asserting behavior or a contract in this file scope.
  test_security_headers_do_not_remove_existing_headers()
  * Test function asserting behavior or a contract in this file scope.
  test_security_headers_content_type()
  * Test function asserting behavior or a contract in this file scope.
  test_sanitize_request_nested_payload()
  * Test function asserting behavior or a contract in this file scope.
  health()
  * Function physically present in the current codebase.

* Classes:
  None.

# =========================
# SERVICES
# =========================

app/services/auth_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  signup_user()
  * Function physically present in the current codebase.
  login_user()
  * Function physically present in the current codebase.
  get_current_user()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  logout_user()
  * Function physically present in the current codebase.
  forgot_password()
  * Function physically present in the current codebase.
  reset_password()
  * Function physically present in the current codebase.
  verify_email()
  * Updates, persists, or verifies data at the file boundary.
  authenticate_access_token()
  * Function physically present in the current codebase.

* Classes:
  None.

app/services/email_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  send_email()
  * Builds or sends an outbound email/message/response payload.
  build_verification_email_body()
  * Builds or sends an outbound email/message/response payload.
  build_reset_password_email_body()
  * Builds or sends an outbound email/message/response payload.
  send_verification_email()
  * Builds or sends an outbound email/message/response payload.
  send_reset_password_email()
  * Builds or sends an outbound email/message/response payload.

* Classes:
  None.

app/services/google_auth_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  generate_google_auth_url()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  verify_google_token()
  * Updates, persists, or verifies data at the file boundary.
  process_google_login()
  * Function physically present in the current codebase.

* Classes:
  None.

app/services/jwt_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  create_access_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  create_refresh_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  decode_token()
  * Function physically present in the current codebase.
  verify_token()
  * Updates, persists, or verifies data at the file boundary.
  extract_token()
  * Function physically present in the current codebase.

* Classes:
  None.

app/services/logging_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  log_request()
  * Records request, response, error, auth, or prediction activity.
  log_error()
  * Records request, response, error, auth, or prediction activity.
  log_auth_event()
  * Records request, response, error, auth, or prediction activity.
  log_prediction()
  * Records request, response, error, auth, or prediction activity.

* Classes:
  None.

app/services/prediction_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  generate_prediction()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  process_prediction()
  * Function physically present in the current codebase.
  build_prediction_response()
  * Builds or sends an outbound email/message/response payload.
  save_prediction_history()
  * Updates, persists, or verifies data at the file boundary.
  get_user_prediction_history()
  * Retrieves data from context, configuration, repository, external API, or ML registry.

* Classes:
  None.

app/services/rate_limit_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  get_client_ip()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  cleanup_expired_requests()
  * Function physically present in the current codebase.
  check_rate_limit()
  * Function physically present in the current codebase.
  update_rate_limit()
  * Updates, persists, or verifies data at the file boundary.

* Classes:
  None.

tests/services/test_auth_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  test_signup_success()
  * Test function asserting behavior or a contract in this file scope.
  test_signup_validation_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_signup_existing_user()
  * Test function asserting behavior or a contract in this file scope.
  test_login_success()
  * Test function asserting behavior or a contract in this file scope.
  test_login_validation_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_login_user_not_found()
  * Test function asserting behavior or a contract in this file scope.
  test_login_wrong_password()
  * Test function asserting behavior or a contract in this file scope.
  test_get_current_user_success()
  * Test function asserting behavior or a contract in this file scope.
  test_get_current_user_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_logout_user()
  * Test function asserting behavior or a contract in this file scope.
  test_forgot_password_success()
  * Test function asserting behavior or a contract in this file scope.
  test_forgot_password_user_not_found()
  * Test function asserting behavior or a contract in this file scope.
  test_reset_password_success()
  * Test function asserting behavior or a contract in this file scope.
  test_reset_password_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_email_success()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_email_invalid_token()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/services/test_email_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  test_send_email_success()
  * Test function asserting behavior or a contract in this file scope.
  test_send_email_missing_email()
  * Test function asserting behavior or a contract in this file scope.
  test_send_email_missing_subject()
  * Test function asserting behavior or a contract in this file scope.
  test_send_email_missing_body()
  * Test function asserting behavior or a contract in this file scope.
  test_send_email_transport_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_build_verification_email_body()
  * Test function asserting behavior or a contract in this file scope.
  test_build_reset_password_email_body()
  * Test function asserting behavior or a contract in this file scope.
  test_send_verification_email_success()
  * Test function asserting behavior or a contract in this file scope.
  test_send_verification_email_missing_email()
  * Test function asserting behavior or a contract in this file scope.
  test_send_verification_email_missing_token()
  * Test function asserting behavior or a contract in this file scope.
  test_send_reset_password_email_success()
  * Test function asserting behavior or a contract in this file scope.
  test_send_reset_password_email_missing_email()
  * Test function asserting behavior or a contract in this file scope.
  test_send_reset_password_email_missing_token()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/services/test_google_auth_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  test_generate_google_auth_url()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_google_token_success()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_google_token_missing_auth_code()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_google_token_exchange_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_google_token_exception()
  * Test function asserting behavior or a contract in this file scope.
  test_process_google_login_missing_auth_code()
  * Test function asserting behavior or a contract in this file scope.
  test_process_google_login_failed_auth()
  * Test function asserting behavior or a contract in this file scope.
  test_process_google_login_invalid_google_data()
  * Test function asserting behavior or a contract in this file scope.
  test_process_google_login_existing_user()
  * Test function asserting behavior or a contract in this file scope.
  test_process_google_login_new_user()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/services/test_jwt_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  test_create_access_token()
  * Test function asserting behavior or a contract in this file scope.
  test_create_refresh_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_valid_access_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_valid_refresh_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_malformed_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_empty_token()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_valid_access_token()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_valid_refresh_token()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_wrong_token_type()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_empty_token()
  * Test function asserting behavior or a contract in this file scope.
  test_extract_token_success()
  * Test function asserting behavior or a contract in this file scope.
  test_extract_token_missing_header()
  * Test function asserting behavior or a contract in this file scope.
  test_extract_token_invalid_prefix()
  * Test function asserting behavior or a contract in this file scope.
  test_extract_token_empty_bearer()
  * Test function asserting behavior or a contract in this file scope.
  test_extract_token_whitespace_bearer()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/services/test_logging_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  test_log_request_success()
  * Test function asserting behavior or a contract in this file scope.
  test_log_request_logger_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_log_error_success()
  * Test function asserting behavior or a contract in this file scope.
  test_log_error_logger_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_log_auth_event_success()
  * Test function asserting behavior or a contract in this file scope.
  test_log_auth_event_logger_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_log_prediction_success()
  * Test function asserting behavior or a contract in this file scope.
  test_log_prediction_logger_failure()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/services/test_prediction_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  test_generate_prediction_success()
  * Test function asserting behavior or a contract in this file scope.
  test_process_prediction_success()
  * Test function asserting behavior or a contract in this file scope.
  test_build_prediction_response_success()
  * Test function asserting behavior or a contract in this file scope.
  test_save_prediction_history_success()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_prediction_mapping_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_prediction_model_failure()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/services/test_rate_limit_service.py

* Responsibility:
  Service/use-case layer. It orchestrates validators, repositories, schemas, utilities, external adapters, or ML modules according to the workflow.

* Connected Layers:
  Controller/middleware -> service -> lower-level validators/repositories/schemas/utilities/external adapters/ML.

* Functions:
  setup_function()
  * Function physically present in the current codebase.
  test_get_client_ip_from_forwarded_header()
  * Test function asserting behavior or a contract in this file scope.
  test_get_client_ip_from_remote_addr()
  * Test function asserting behavior or a contract in this file scope.
  test_cleanup_expired_requests()
  * Test function asserting behavior or a contract in this file scope.
  test_check_rate_limit_initially_true()
  * Test function asserting behavior or a contract in this file scope.
  test_check_rate_limit_exceeded()
  * Test function asserting behavior or a contract in this file scope.
  test_check_rate_limit_unknown_ip()
  * Test function asserting behavior or a contract in this file scope.
  test_update_rate_limit()
  * Test function asserting behavior or a contract in this file scope.
  test_update_rate_limit_unknown_ip()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

# =========================
# REPOSITORIES AND DATABASE
# =========================

app/database/collections.py

* Responsibility:
  Database infrastructure boundary for MongoDB client, database, or collection access.

* Connected Layers:
  Repository -> database infrastructure -> Flask config/PyMongo.

* Functions:
  users_collection()
  * Function physically present in the current codebase.
  predictions_collection()
  * Function physically present in the current codebase.

* Classes:
  None.

app/database/database.py

* Responsibility:
  Database infrastructure boundary for MongoDB client, database, or collection access.

* Connected Layers:
  Repository -> database infrastructure -> Flask config/PyMongo.

* Functions:
  connect_database()
  * Function physically present in the current codebase.
  get_db()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  close_database()
  * Function physically present in the current codebase.

* Classes:
  None.

app/repositories/prediction_repository.py

* Responsibility:
  Repository/persistence adapter. It owns MongoDB collection access and persistence document serialization.

* Connected Layers:
  Service -> repository -> database collection accessor -> MongoDB.

* Database Operations:
  collection.find({'user_id': user_id}).sort
  * repository-owned database operation.
  collection.find_one
  * repository-owned database operation.
  collection.insert_one
  * repository-owned database operation.

* Functions:
  _get_predictions_collection()
  * Function physically present in the current codebase.
  save_prediction()
  * Updates, persists, or verifies data at the file boundary.
  get_prediction_history()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  get_prediction_by_id()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  serialize_prediction()
  * Serializes internal data into an API-safe dictionary shape.

* Classes:
  None.

app/repositories/user_repository.py

* Responsibility:
  Repository/persistence adapter. It owns MongoDB collection access and persistence document serialization.

* Connected Layers:
  Service -> repository -> database collection accessor -> MongoDB.

* Database Operations:
  collection.find_one
  * repository-owned database operation.
  collection.insert_one
  * repository-owned database operation.
  collection.update_one
  * repository-owned database operation.

* Functions:
  _get_users_collection()
  * Function physically present in the current codebase.
  create_user()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  find_user_by_email()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  find_user_by_id()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  update_user()
  * Updates, persists, or verifies data at the file boundary.
  verify_user_email()
  * Updates, persists, or verifies data at the file boundary.
  serialize_user()
  * Serializes internal data into an API-safe dictionary shape.

* Classes:
  None.

tests/repositories/test_prediction_repository.py

* Responsibility:
  Repository/persistence adapter. It owns MongoDB collection access and persistence document serialization.

* Connected Layers:
  Service -> repository -> database collection accessor -> MongoDB.

* Database Operations:
  mock_collection.insert_one.assert_called_once
  * repository-owned database operation.

* Functions:
  test_save_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_by_id_found()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_by_id_not_found()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_empty()
  * Test function asserting behavior or a contract in this file scope.
  __init__()
  * Function physically present in the current codebase.

* Classes:
  MockInsertResult
  * Class physically present in this file.
  * Methods: __init__()

tests/repositories/test_user_repository.py

* Responsibility:
  Repository/persistence adapter. It owns MongoDB collection access and persistence document serialization.

* Connected Layers:
  Service -> repository -> database collection accessor -> MongoDB.

* Database Operations:
  mock_collection.insert_one.assert_called_once
  * repository-owned database operation.

* Functions:
  test_create_user()
  * Test function asserting behavior or a contract in this file scope.
  test_find_user_by_email_found()
  * Test function asserting behavior or a contract in this file scope.
  test_find_user_by_email_not_found()
  * Test function asserting behavior or a contract in this file scope.
  test_find_user_by_id_found()
  * Test function asserting behavior or a contract in this file scope.
  test_find_user_by_id_not_found()
  * Test function asserting behavior or a contract in this file scope.
  test_update_user_success()
  * Test function asserting behavior or a contract in this file scope.
  test_update_user_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_user_email_success()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_user_email_failure()
  * Test function asserting behavior or a contract in this file scope.
  __init__()
  * Function physically present in the current codebase.
  __init__()
  * Function physically present in the current codebase.

* Classes:
  MockInsertResult
  * Class physically present in this file.
  * Methods: __init__()
  MockUpdateResult
  * Class physically present in this file.
  * Methods: __init__()

# =========================
# SCHEMAS
# =========================

app/schemas/auth_schema.py

* Responsibility:
  Serialization boundary for API-facing response shapes.

* Connected Layers:
  Service/repository output -> schema -> API response payload.

* Functions:
  serialize_user()
  * Serializes internal data into an API-safe dictionary shape.
  serialize_auth_response()
  * Serializes internal data into an API-safe dictionary shape.

* Classes:
  None.

app/schemas/history_schema.py

* Responsibility:
  Serialization boundary for API-facing response shapes.

* Connected Layers:
  Service/repository output -> schema -> API response payload.

* Functions:
  serialize_prediction_history()
  * Serializes internal data into an API-safe dictionary shape.

* Classes:
  None.

app/schemas/prediction_schema.py

* Responsibility:
  Serialization boundary for API-facing response shapes.

* Connected Layers:
  Service/repository output -> schema -> API response payload.

* Functions:
  serialize_model_output()
  * Serializes internal data into an API-safe dictionary shape.
  serialize_prediction_response()
  * Serializes internal data into an API-safe dictionary shape.

* Classes:
  None.

# =========================
# VALIDATORS
# =========================

app/validators/auth_validator.py

* Responsibility:
  Validation boundary defining request/data contract checks and expected error shapes.

* Connected Layers:
  Service -> validator -> list/dict validation result.

* Functions:
  validate_signup_data()
  * Validates data and returns contract-specific validation errors/result.
  validate_login_data()
  * Validates data and returns contract-specific validation errors/result.
  validate_email()
  * Validates data and returns contract-specific validation errors/result.
  validate_password()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

app/validators/normalization_validator.py

* Responsibility:
  Validation boundary defining request/data contract checks and expected error shapes.

* Connected Layers:
  Service -> validator -> list/dict validation result.

* Functions:
  validate_normalized_input()
  * Validates data and returns contract-specific validation errors/result.
  validate_feature_scaling()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

app/validators/prediction_validator.py

* Responsibility:
  Validation boundary defining request/data contract checks and expected error shapes.

* Connected Layers:
  Service -> validator -> list/dict validation result.

* Functions:
  validate_prediction_input()
  * Validates data and returns contract-specific validation errors/result.
  validate_required_features()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

app/validators/range_validator.py

* Responsibility:
  Validation boundary defining request/data contract checks and expected error shapes.

* Connected Layers:
  Service -> validator -> list/dict validation result.

* Functions:
  validate_feature_ranges()
  * Validates data and returns contract-specific validation errors/result.
  validate_score_limits()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

app/validators/type_validator.py

* Responsibility:
  Validation boundary defining request/data contract checks and expected error shapes.

* Connected Layers:
  Service -> validator -> list/dict validation result.

* Functions:
  validate_input_types()
  * Validates data and returns contract-specific validation errors/result.
  validate_numeric_fields()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

# =========================
# UTILITIES AND EXTERNAL ADAPTERS
# =========================

app/external_apis/email_client.py

* Responsibility:
  External adapter boundary for third-party service communication.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  connect_smtp_server()
  * Function physically present in the current codebase.
  send_email_message()
  * Builds or sends an outbound email/message/response payload.

* Classes:
  None.

app/external_apis/google_oauth.py

* Responsibility:
  External adapter boundary for third-party service communication.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  get_google_provider_config()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  exchange_auth_code()
  * Function physically present in the current codebase.
  get_google_user_info()
  * Retrieves data from context, configuration, repository, external API, or ML registry.

* Classes:
  None.

app/utils/constants.py

* Responsibility:
  Shared utility/infrastructure module used across layers.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  None.

* Classes:
  None.

app/utils/helpers.py

* Responsibility:
  Shared utility/infrastructure module used across layers.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  generate_uuid()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  get_current_timestamp()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  format_datetime()
  * Function physically present in the current codebase.

* Classes:
  None.

app/utils/logger.py

* Responsibility:
  Shared utility/infrastructure module used across layers.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  setup_logger()
  * Function physically present in the current codebase.
  get_logger()
  * Retrieves data from context, configuration, repository, external API, or ML registry.

* Classes:
  None.

app/utils/response.py

* Responsibility:
  Shared utility/infrastructure module used across layers.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  success_response()
  * Function physically present in the current codebase.
  error_response()
  * Function physically present in the current codebase.

* Classes:
  None.

app/utils/security.py

* Responsibility:
  Shared utility/infrastructure module used across layers.

* Connected Layers:
  Connected according to current imports and layer ownership.

* Functions:
  hash_password()
  * Function physically present in the current codebase.
  verify_password()
  * Updates, persists, or verifies data at the file boundary.
  generate_secure_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  sanitize_input()
  * Function physically present in the current codebase.

* Classes:
  None.

# =========================
# ML FILES
# =========================

ml/explainability/consensus_explainer.py

* Responsibility:
  Placeholder ML explainability module; physically present but no active production code.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  None.

* Classes:
  None.

ml/explainability/feature_importance.py

* Responsibility:
  Placeholder ML explainability module; physically present but no active production code.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  None.

* Classes:
  None.

ml/explainability/severity_explainer.py

* Responsibility:
  Placeholder ML explainability module; physically present but no active production code.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  None.

* Classes:
  None.

ml/inference/confidence_analyzer.py

* Responsibility:
  ML inference module for model loading, model-specific prediction, ensemble aggregation, or confidence analysis.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* ML Calls:
  prediction_counts.most_common
  * inference or artifact-loading call detected in current code.

* Functions:
  calculate_confidence()
  * Function physically present in the current codebase.
  calculate_agreement_strength()
  * Function physically present in the current codebase.

* Classes:
  None.

ml/inference/ensemble_predictor.py

* Responsibility:
  ML inference module for model loading, model-specific prediction, ensemble aggregation, or confidence analysis.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* ML Calls:
  aggregate_predictions
  * inference or artifact-loading call detected in current code.
  predictor['predict']
  * inference or artifact-loading call detected in current code.
  predictor['probability']
  * inference or artifact-loading call detected in current code.

* Functions:
  run_all_models()
  * Function physically present in the current codebase.
  aggregate_predictions()
  * Function physically present in the current codebase.
  generate_ensemble_output()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.

* Classes:
  None.

ml/inference/logistic_predictor.py

* Responsibility:
  ML inference module for model loading, model-specific prediction, ensemble aggregation, or confidence analysis.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* ML Calls:
  model.predict
  * inference or artifact-loading call detected in current code.
  model.predict_proba
  * inference or artifact-loading call detected in current code.
  model.predict_proba(dataframe).max
  * inference or artifact-loading call detected in current code.

* Functions:
  predict_logistic()
  * Runs model-specific prediction or probability inference.
  predict_logistic_probability()
  * Runs model-specific prediction or probability inference.

* Classes:
  None.

ml/inference/model_loader.py

* Responsibility:
  ML inference module for model loading, model-specific prediction, ensemble aggregation, or confidence analysis.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* ML Calls:
  joblib.load
  * inference or artifact-loading call detected in current code.
  load_models
  * inference or artifact-loading call detected in current code.

* Functions:
  _build_model_key()
  * Function physically present in the current codebase.
  load_models()
  * Loads or exposes runtime configuration/artifact state.
  load_feature_orders()
  * Loads or exposes runtime configuration/artifact state.
  get_model()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  get_feature_order()
  * Retrieves data from context, configuration, repository, external API, or ML registry.
  get_loaded_models()
  * Loads or exposes runtime configuration/artifact state.
  initialize_ml_models()
  * Loads or exposes runtime configuration/artifact state.

* Classes:
  None.

ml/inference/randomforest_predictor.py

* Responsibility:
  ML inference module for model loading, model-specific prediction, ensemble aggregation, or confidence analysis.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* ML Calls:
  model.predict
  * inference or artifact-loading call detected in current code.
  model.predict_proba
  * inference or artifact-loading call detected in current code.
  model.predict_proba(dataframe).max
  * inference or artifact-loading call detected in current code.

* Functions:
  predict_randomforest()
  * Runs model-specific prediction or probability inference.
  predict_randomforest_probability()
  * Runs model-specific prediction or probability inference.

* Classes:
  None.

ml/inference/svm_predictor.py

* Responsibility:
  ML inference module for model loading, model-specific prediction, ensemble aggregation, or confidence analysis.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* ML Calls:
  model.predict
  * inference or artifact-loading call detected in current code.
  model.predict_proba
  * inference or artifact-loading call detected in current code.
  model.predict_proba(dataframe).max
  * inference or artifact-loading call detected in current code.

* Functions:
  predict_svm()
  * Runs model-specific prediction or probability inference.
  predict_svm_probability()
  * Runs model-specific prediction or probability inference.

* Classes:
  None.

ml/models/__init__.py

* Responsibility:
  ML artifact path marker/registry for trained models or feature order files.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  None.

* Classes:
  None.

ml/models/feature_orders/__init__.py

* Responsibility:
  ML artifact path marker/registry for trained models or feature order files.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  None.

* Classes:
  None.

ml/models/trained_models/__init__.py

* Responsibility:
  ML artifact path marker/registry for trained models or feature order files.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  None.

* Classes:
  None.

ml/preprocessing/feature_mapper.py

* Responsibility:
  ML preprocessing module for feature mapping, selection, alignment, or normalization.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  map_features()
  * Function physically present in the current codebase.
  align_feature_order()
  * Function physically present in the current codebase.

* Classes:
  None.

ml/preprocessing/feature_selector.py

* Responsibility:
  ML preprocessing module for feature mapping, selection, alignment, or normalization.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  select_x1_features()
  * Function physically present in the current codebase.
  select_x3_features()
  * Function physically present in the current codebase.

* Classes:
  None.

ml/preprocessing/normalizer.py

* Responsibility:
  ML preprocessing module for feature mapping, selection, alignment, or normalization.

* Connected Layers:
  prediction_service/ensemble_predictor -> ML preprocessing/inference/artifact registry.

* ML Role:
  Explains model artifact/preprocessing/inference support in the prediction pipeline; placeholder files have no active inference role.

* Functions:
  normalize_features()
  * Function physically present in the current codebase.
  scale_features()
  * Function physically present in the current codebase.

* Classes:
  None.

# =========================
# TEST SUITE FILES
# =========================

tests/auth/test_email_verification.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_verify_email_route_exists()
  * Test function asserting behavior or a contract in this file scope.
  test_verify_email_invalid_token()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/auth/test_google_auth.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_google_auth_missing_token()
  * Test function asserting behavior or a contract in this file scope.
  test_google_auth_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_google_auth_route_exists()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/auth/test_jwt.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_generate_access_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_valid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_decode_tampered_token()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/auth/test_login.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_login_success()
  * Test function asserting behavior or a contract in this file scope.
  test_login_wrong_password()
  * Test function asserting behavior or a contract in this file scope.
  test_login_nonexistent_user()
  * Test function asserting behavior or a contract in this file scope.
  test_login_missing_email()
  * Test function asserting behavior or a contract in this file scope.
  test_login_missing_password()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/auth/test_logout.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_logout_success()
  * Test function asserting behavior or a contract in this file scope.
  test_logout_without_token()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/auth/test_me.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_get_current_user_success()
  * Test function asserting behavior or a contract in this file scope.
  test_get_current_user_missing_token()
  * Test function asserting behavior or a contract in this file scope.
  test_get_current_user_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_get_current_user_expired_token()
  * Test function asserting behavior or a contract in this file scope.
  test_get_current_user_user_not_found()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/auth/test_password_reset.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_forgot_password_success()
  * Test function asserting behavior or a contract in this file scope.
  test_forgot_password_invalid_email()
  * Test function asserting behavior or a contract in this file scope.
  test_reset_password_route_exists()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/auth/test_signup.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_signup_success()
  * Test function asserting behavior or a contract in this file scope.
  test_signup_duplicate_email()
  * Test function asserting behavior or a contract in this file scope.
  test_signup_invalid_email()
  * Test function asserting behavior or a contract in this file scope.
  test_signup_weak_password()
  * Test function asserting behavior or a contract in this file scope.
  test_signup_missing_fields()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/conftest.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  app()
  * Pytest fixture used by related tests.
  client()
  * Pytest fixture used by related tests.
  sample_user()
  * Pytest fixture used by related tests.
  mock_db_user()
  * Pytest fixture used by related tests.
  login_payload()
  * Pytest fixture used by related tests.
  auth_token()
  * Pytest fixture used by related tests.
  auth_headers()
  * Pytest fixture used by related tests.
  base_prediction_payload()
  * Pytest fixture used by related tests.
  invalid_prediction_payload()
  * Pytest fixture used by related tests.
  incomplete_prediction_payload()
  * Pytest fixture used by related tests.
  cleanup_test_state()
  * Function physically present in the current codebase.

* Classes:
  None.

tests/fixtures/auth_payloads.py

* Responsibility:
  Test fixture data module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  None.

* Classes:
  None.

tests/fixtures/model_fixtures.py

* Responsibility:
  Test fixture data module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  None.

* Classes:
  None.

tests/fixtures/prediction_payloads.py

* Responsibility:
  Test fixture data module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  None.

* Classes:
  None.

tests/fixtures/token_fixtures.py

* Responsibility:
  Test fixture data module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  None.

* Classes:
  None.

tests/fixtures/user_fixtures.py

* Responsibility:
  Test fixture data module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  None.

* Classes:
  None.

tests/integration/test_auth_flow.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  client()
  * Pytest fixture used by related tests.
  test_complete_auth_flow()
  * Test function asserting behavior or a contract in this file scope.
  test_duplicate_signup_rejected()
  * Test function asserting behavior or a contract in this file scope.
  test_login_with_invalid_password()
  * Test function asserting behavior or a contract in this file scope.
  test_access_protected_route_without_token()
  * Test function asserting behavior or a contract in this file scope.
  test_forgot_password_flow()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/integration/test_database_integration.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  sample_user()
  * Pytest fixture used by related tests.
  sample_prediction()
  * Pytest fixture used by related tests.
  test_create_user_in_database()
  * Test function asserting behavior or a contract in this file scope.
  test_find_user_by_email()
  * Test function asserting behavior or a contract in this file scope.
  test_find_nonexistent_user()
  * Test function asserting behavior or a contract in this file scope.
  test_save_prediction_to_database()
  * Test function asserting behavior or a contract in this file scope.
  test_multiple_users_can_be_created()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_document_structure()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/integration/test_full_user_journey.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  client()
  * Pytest fixture used by related tests.
  test_complete_user_journey()
  * Test function asserting behavior or a contract in this file scope.
  test_user_journey_with_invalid_login()
  * Test function asserting behavior or a contract in this file scope.
  test_user_journey_protected_route_without_token()
  * Test function asserting behavior or a contract in this file scope.
  test_user_journey_duplicate_signup()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/integration/test_prediction_flow.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  client()
  * Pytest fixture used by related tests.
  test_prediction_endpoint_success()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_types()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_confidence_range()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_missing_feature()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_empty_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_invalid_content_type()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_endpoint_returns_json()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_confidence_analyzer.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_calculate_confidence_returns_float()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_returns_expected_average()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_handles_single_value()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_handles_zero_values()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_handles_high_confidence()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_raises_error_on_empty_list()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_returns_string()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_detects_strong_agreement()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_detects_partial_agreement()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_detects_low_agreement()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_handles_single_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_raises_error_on_empty_list()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_ensemble_predictor.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_run_all_models_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_contains_expected_keys()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_majority_vote_positive()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_majority_vote_negative()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_contains_expected_keys()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_high_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_low_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_calls_all_predictors()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_raises_error_on_empty_input()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_payload_scenarios()
  * Test function asserting behavior or a contract in this file scope.
  test_mock_model_response_structure()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_feature_mapper.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_map_features_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_map_features_preserves_values()
  * Test function asserting behavior or a contract in this file scope.
  test_align_feature_order_returns_list()
  * Test function asserting behavior or a contract in this file scope.
  test_align_feature_order_matches_feature_order()
  * Test function asserting behavior or a contract in this file scope.
  test_align_feature_order_raises_key_error()
  * Test function asserting behavior or a contract in this file scope.
  test_map_features_missing_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_align_feature_order_with_full_payload()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_feature_selector.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_select_x1_features_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x1_features_contains_expected_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x1_features_excludes_unrelated_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x3_features_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x3_features_contains_expected_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x3_features_preserves_values()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x1_features_returns_subset()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x3_features_returns_subset()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x1_features_handles_missing_feature()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x3_features_handles_missing_feature()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_logistic_predictor.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_predict_logistic_returns_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_probability_returns_float()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_probability_returns_expected_value()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_handles_low_risk_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_handles_high_risk_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_probability_handles_low_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_probability_handles_high_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_raises_key_error()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_calls_model_predict()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_logistic_probability_calls_predict_proba()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_model_loader.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_load_models_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_load_models_contains_expected_models()
  * Test function asserting behavior or a contract in this file scope.
  test_load_feature_orders_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_load_feature_orders_contains_expected_keys()
  * Test function asserting behavior or a contract in this file scope.
  test_get_loaded_models_returns_combined_data()
  * Test function asserting behavior or a contract in this file scope.
  test_load_models_raises_file_not_found()
  * Test function asserting behavior or a contract in this file scope.
  test_load_feature_orders_raises_file_not_found()
  * Test function asserting behavior or a contract in this file scope.
  test_load_models_calls_joblib_multiple_times()
  * Test function asserting behavior or a contract in this file scope.
  test_load_feature_orders_calls_joblib_multiple_times()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_normalizer.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_normalize_features_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_normalize_features_preserves_keys()
  * Test function asserting behavior or a contract in this file scope.
  test_normalize_features_returns_numeric_values()
  * Test function asserting behavior or a contract in this file scope.
  test_scale_features_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_scale_features_preserves_keys()
  * Test function asserting behavior or a contract in this file scope.
  test_scale_features_returns_numeric_values()
  * Test function asserting behavior or a contract in this file scope.
  test_normalize_features_handles_low_risk_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_normalize_features_handles_high_risk_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_scale_features_handles_empty_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_normalize_features_handles_invalid_input()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_randomforest_predictor.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_predict_randomforest_returns_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_probability_returns_float()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_probability_returns_expected_value()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_handles_low_risk_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_handles_high_risk_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_probability_handles_low_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_probability_handles_high_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_raises_key_error()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_calls_model_predict()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_randomforest_probability_calls_predict_proba()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/ml/test_svm_predictor.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_predict_svm_returns_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_probability_returns_float()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_probability_returns_expected_value()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_handles_low_risk_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_handles_high_risk_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_probability_handles_low_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_probability_handles_high_risk()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_raises_key_error()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_calls_model_predict()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_svm_probability_calls_predict_proba()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/mocks/mock_models.py

* Responsibility:
  Test mock/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  create_mock_svm_model()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  create_mock_logistic_model()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  create_mock_randomforest_model()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  create_failing_model()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.

* Classes:
  None.

tests/mocks/mock_predictions.py

* Responsibility:
  Test mock/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  None.

* Classes:
  None.

tests/mocks/mock_tokens.py

* Responsibility:
  Test mock/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  generate_valid_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  generate_expired_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  generate_refresh_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.

* Classes:
  None.

tests/mocks/mock_users.py

* Responsibility:
  Test mock/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  generate_mock_jwt_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.

* Classes:
  None.

tests/prediction/test_confidence_analysis.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_calculate_confidence_returns_float()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_within_valid_range()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_high_probability()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_low_probability()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_single_class_probability()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_rejects_empty_probabilities()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_rejects_invalid_types()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_handles_zero_probabilities()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_precision()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_confidence_is_deterministic()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_returns_float()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_full_agreement()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_partial_agreement()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_complete_disagreement()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_rejects_empty_predictions()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_single_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_with_all_negative_predictions()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_returns_valid_range()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_rejects_invalid_types()
  * Test function asserting behavior or a contract in this file scope.
  test_calculate_agreement_strength_is_deterministic()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/prediction/test_ensemble_predictor.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_aggregate_predictions_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_contains_required_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_prediction_type()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_confidence_type()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_confidence_range()
  * Test function asserting behavior or a contract in this file scope.
  test_majority_vote_behavior()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_contains_metadata()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_severity_type()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_model_used_type()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_prediction_type()
  * Test function asserting behavior or a contract in this file scope.
  test_generate_ensemble_output_confidence_type()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_returns_complete_output()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_ensemble_structure()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_model_structure()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_prediction_types()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_confidence_ranges()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_ensemble_confidence_range()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_rejects_empty_input()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_single_model()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_complete_disagreement()
  * Test function asserting behavior or a contract in this file scope.
  test_aggregate_predictions_is_deterministic()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_handles_partial_input()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_rejects_invalid_input()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/prediction/test_model_selection.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_select_x1_features_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x3_features_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x1_features_not_empty()
  * Test function asserting behavior or a contract in this file scope.
  test_select_x3_features_not_empty()
  * Test function asserting behavior or a contract in this file scope.
  test_x1_feature_contains_age()
  * Test function asserting behavior or a contract in this file scope.
  test_x3_feature_contains_psychological_features()
  * Test function asserting behavior or a contract in this file scope.
  test_x3_contains_more_features_than_x1()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_returns_dictionary()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_contains_required_keys()
  * Test function asserting behavior or a contract in this file scope.
  test_model_predictions_are_numeric()
  * Test function asserting behavior or a contract in this file scope.
  test_model_confidence_scores_are_valid()
  * Test function asserting behavior or a contract in this file scope.
  test_ensemble_output_exists()
  * Test function asserting behavior or a contract in this file scope.
  test_ensemble_confidence_score_valid()
  * Test function asserting behavior or a contract in this file scope.
  test_model_selection_handles_missing_optional_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_model_selection_rejects_invalid_input()
  * Test function asserting behavior or a contract in this file scope.
  test_ensemble_contains_prediction()
  * Test function asserting behavior or a contract in this file scope.
  test_ensemble_contains_confidence_score()
  * Test function asserting behavior or a contract in this file scope.
  test_model_outputs_have_consistent_structure()
  * Test function asserting behavior or a contract in this file scope.
  test_feature_selectors_handle_empty_input()
  * Test function asserting behavior or a contract in this file scope.
  test_run_all_models_is_deterministic()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/prediction/test_predict_endpoint.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_predict_endpoint_success()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_response_types()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_confidence_range()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_missing_feature()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_invalid_type()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_invalid_range()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_empty_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_null_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_without_authentication()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_expired_token()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_response_structure()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_content_types()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_large_values()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_negative_values()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_extra_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_returns_json()
  * Test function asserting behavior or a contract in this file scope.
  test_predict_endpoint_is_deterministic_structure()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/prediction/test_prediction_history.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_get_prediction_history_success()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_requires_authentication()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_empty()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_response_structure()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_prediction_type()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_confidence_range()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_created_at_type()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_multiple_records()
  * Test function asserting behavior or a contract in this file scope.
  test_get_prediction_history_user_isolation()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/prediction/test_prediction_response.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_prediction_response_contains_required_fields()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_prediction_type()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_confidence_type()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_confidence_range()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_severity_type()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_valid_severity()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_model_used_type()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_model_used_not_empty()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_optional_recommendation()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_prediction_not_negative()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_confidence_precision()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_response_serializable()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/prediction/test_prediction_validation.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_validate_prediction_input_success()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_required_features_success()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_empty_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_missing_required_feature()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_invalid_gender()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_age_below_minimum()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_age_above_maximum()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_invalid_sleep_duration_low()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_invalid_sleep_duration_high()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_invalid_social_media_hours()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_invalid_binary_field()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_invalid_scale_value()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_string_in_numeric_field()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_none_value()
  * Test function asserting behavior or a contract in this file scope.
  test_validate_prediction_input_float_for_integer_field()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/security/test_input_sanitization.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  sanitize_input()
  * Function physically present in the current codebase.
  test_remove_script_tags()
  * Test function asserting behavior or a contract in this file scope.
  test_remove_html_tags()
  * Test function asserting behavior or a contract in this file scope.
  test_trim_whitespace()
  * Test function asserting behavior or a contract in this file scope.
  test_email_normalization()
  * Test function asserting behavior or a contract in this file scope.
  test_none_input_returns_empty_string()
  * Test function asserting behavior or a contract in this file scope.
  test_safe_plain_text_remains_unchanged()
  * Test function asserting behavior or a contract in this file scope.
  test_nested_html_removed()
  * Test function asserting behavior or a contract in this file scope.
  test_sql_like_input_not_executed()
  * Test function asserting behavior or a contract in this file scope.
  test_javascript_event_attributes_removed()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/security/test_password_hashing.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_password_is_hashed()
  * Test function asserting behavior or a contract in this file scope.
  test_password_hash_verification_success()
  * Test function asserting behavior or a contract in this file scope.
  test_password_hash_verification_failure()
  * Test function asserting behavior or a contract in this file scope.
  test_same_password_generates_different_hashes()
  * Test function asserting behavior or a contract in this file scope.
  test_hashes_still_validate_for_same_password()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/security/test_protected_routes.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  create_test_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  verify_protected_route()
  * Updates, persists, or verifies data at the file boundary.
  test_protected_route_without_token()
  * Test function asserting behavior or a contract in this file scope.
  test_protected_route_with_invalid_format()
  * Test function asserting behavior or a contract in this file scope.
  test_protected_route_with_valid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_protected_route_with_tampered_token()
  * Test function asserting behavior or a contract in this file scope.
  test_protected_route_with_expired_token()
  * Test function asserting behavior or a contract in this file scope.
  test_protected_route_with_empty_bearer_token()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/security/test_token_security.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  generate_token()
  * Creates runtime data, token, app object, mock object, or ML output depending on file scope.
  test_jwt_token_generation()
  * Test function asserting behavior or a contract in this file scope.
  test_jwt_token_decoding()
  * Test function asserting behavior or a contract in this file scope.
  test_expired_jwt_token()
  * Test function asserting behavior or a contract in this file scope.
  test_invalid_secret_key()
  * Test function asserting behavior or a contract in this file scope.
  test_tampered_jwt_token()
  * Test function asserting behavior or a contract in this file scope.
  test_bearer_token_extraction()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/test_security.py

* Responsibility:
  Pytest module verifying backend behavior, layer contracts, or integration flows.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  test_protected_route_without_token()
  * Test function asserting behavior or a contract in this file scope.
  test_protected_route_with_invalid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_protected_route_with_valid_token()
  * Test function asserting behavior or a contract in this file scope.
  test_security_headers_exist()
  * Test function asserting behavior or a contract in this file scope.
  test_content_type_is_json()
  * Test function asserting behavior or a contract in this file scope.
  test_invalid_http_method_on_predict()
  * Test function asserting behavior or a contract in this file scope.
  test_invalid_http_method_on_signup()
  * Test function asserting behavior or a contract in this file scope.
  test_large_payload_rejected()
  * Test function asserting behavior or a contract in this file scope.
  test_sql_injection_like_input()
  * Test function asserting behavior or a contract in this file scope.
  test_xss_like_input()
  * Test function asserting behavior or a contract in this file scope.
  test_missing_json_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_empty_json_payload()
  * Test function asserting behavior or a contract in this file scope.
  test_invalid_token_format()
  * Test function asserting behavior or a contract in this file scope.
  test_prediction_endpoint_requires_post()
  * Test function asserting behavior or a contract in this file scope.

* Classes:
  None.

tests/validators/auth_validator.py

* Responsibility:
  Test-local duplicate validator/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  validate_signup_data()
  * Validates data and returns contract-specific validation errors/result.
  validate_login_data()
  * Validates data and returns contract-specific validation errors/result.
  validate_email()
  * Validates data and returns contract-specific validation errors/result.
  validate_password()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

tests/validators/feature_rules.py

* Responsibility:
  Test-local duplicate validator/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  None.

* Classes:
  None.

tests/validators/normalization_validator.py

* Responsibility:
  Test-local duplicate validator/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  validate_normalized_input()
  * Validates data and returns contract-specific validation errors/result.
  validate_feature_scaling()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

tests/validators/prediction_validator.py

* Responsibility:
  Test-local duplicate validator/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  validate_prediction_input()
  * Validates data and returns contract-specific validation errors/result.
  validate_required_features()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

tests/validators/range_validator.py

* Responsibility:
  Test-local duplicate validator/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  validate_feature_ranges()
  * Validates data and returns contract-specific validation errors/result.
  validate_score_limits()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

tests/validators/type_validator.py

* Responsibility:
  Test-local duplicate validator/helper module; not active production code.

* Connected Layers:
  Pytest -> production module, fixture, or mock target under test.

* Functions:
  validate_input_types()
  * Validates data and returns contract-specific validation errors/result.
  validate_numeric_fields()
  * Validates data and returns contract-specific validation errors/result.

* Classes:
  None.

# =========================
# ARCHITECTURE VIOLATIONS
# =========================

Application factory does not assemble production runtime

* Affected files: app/__init__.py, run.py
* Why it violates the architecture: create_app() only loads config; blueprints, middleware, error handlers, DB lifecycle, and ML initialization are not registered.
* Runtime/maintenance risks: Valid isolated layers can be absent at runtime, causing 404s, missing auth/security/rate-limit behavior, and unloaded models.
* Architectural impact: Composition root is incomplete.

Signup validator contract mismatch

* Affected files: app/validators/auth_validator.py, app/services/auth_service.py
* Why it violates the architecture: signup_user() expects a dict with valid/errors, but validate_signup_data() returns a list and extends it with validate_password() dict data.
* Runtime/maintenance risks: Signup can fail at runtime or return malformed validation errors.
* Architectural impact: Service-validator boundary remains partially unresolved.

Google signup relies on repository compatibility kwargs

* Affected files: app/services/google_auth_service.py, app/repositories/user_repository.py
* Why it violates the architecture: process_google_login() calls create_user(name=..., email=..., password=None) while the repository contract is a user_data dict.
* Runtime/maintenance risks: Future removal of compatibility kwargs would break Google signup.
* Architectural impact: Service-to-repository contract remains loose.

Repository serialization overlaps schemas

* Affected files: app/repositories/user_repository.py, app/repositories/prediction_repository.py, app/schemas/*.py
* Why it violates the architecture: Repositories serialize documents while schemas also own API serialization.
* Runtime/maintenance risks: Field drift can create inconsistent auth/history/prediction responses.
* Architectural impact: Persistence and presentation concerns are mixed.

Outer and inner response contracts can conflict

* Affected files: app/controllers/*.py, app/services/*.py, app/utils/response.py
* Why it violates the architecture: Services return success/message payloads that controllers wrap in success_response(); auth service failures may be nested under outer success=True.
* Runtime/maintenance risks: API clients must inspect both envelope levels.
* Architectural impact: HTTP contract ownership is split.

Opaque email/reset tokens are verified as JWTs

* Affected files: app/services/auth_service.py, app/services/email_service.py, app/services/jwt_service.py
* Why it violates the architecture: signup_user() and forgot_password() generate random tokens, while verify_email() and reset_password() call verify_token(), which expects JWTs.
* Runtime/maintenance risks: Verification/reset flows can fail even after sending email.
* Architectural impact: Auth token semantics are mixed.

Sanitized payload is not consumed by controllers

* Affected files: app/middleware/security_middleware.py, app/controllers/*.py
* Why it violates the architecture: sanitize_request() stores request.sanitized_json, but controllers call request.get_json().
* Runtime/maintenance risks: Sanitization may not affect service inputs.
* Architectural impact: Middleware lifecycle work is not integrated with controller contracts.

ML registry initialization is not wired

* Affected files: ml/inference/model_loader.py, app/__init__.py, app/services/prediction_service.py
* Why it violates the architecture: initialize_ml_models() exists but is not called by create_app().
* Runtime/maintenance risks: Prediction can run with empty model registries unless initialized elsewhere.
* Architectural impact: ML infrastructure is separated but not composed.

Prediction validator can diverge from artifact feature order

* Affected files: app/validators/prediction_validator.py, ml/inference/model_loader.py, ml/inference/ensemble_predictor.py
* Why it violates the architecture: API validation requires a static subset while loaded feature_order may require additional model features.
* Runtime/maintenance risks: Requests can pass validation and fail inside predictors.
* Architectural impact: API and ML artifact contracts are not unified.

Test-local duplicate validators and stale ML tests

* Affected files: tests/validators/*.py, tests/ml/*.py, tests/prediction/*.py
* Why it violates the architecture: Tests include duplicate validators and several names/assertions that appear to target pre-refactor ML return shapes.
* Runtime/maintenance risks: Tests may pass against duplicate logic or fail because expectations are stale.
* Architectural impact: Test contract ownership needs refactor alignment.

# =========================
# ARCHITECTURE IMPROVEMENTS
# =========================

History controller no longer imports prediction repositories directly; it delegates to prediction_service.

* Improvement achieved in the current refactored codebase.

Prediction controller delegates validation, ML orchestration, persistence, and response shaping to prediction_service.

* Improvement achieved in the current refactored codebase.

Auth middleware delegates token-to-user resolution to auth_service instead of touching repositories directly.

* Improvement achieved in the current refactored codebase.

Repositories now resolve collection accessor functions before PyMongo operations.

* Improvement achieved in the current refactored codebase.

prediction_service now calls generate_ensemble_output() with the current ML signature.

* Improvement achieved in the current refactored codebase.

prediction_schema now accepts ensemble metadata such as agreement_strength and model_results.

* Improvement achieved in the current refactored codebase.

email_service now calls the SMTP adapter with the correct to_email/subject/body contract.

* Improvement achieved in the current refactored codebase.

logging_service/logger contracts now accept file paths and compatible request payloads.

* Improvement achieved in the current refactored codebase.

rate_limit_middleware now treats check_rate_limit() as a boolean instead of unpacking it.

* Improvement achieved in the current refactored codebase.

JWT config aliases and jwt_service fallbacks reduce configuration naming breakage.

* Improvement achieved in the current refactored codebase.

Ensemble aggregation and confidence analysis now guard no-model/empty-list cases.

* Improvement achieved in the current refactored codebase.

Email constants required by email_service now exist in constants.py.

* Improvement achieved in the current refactored codebase.

# =========================
# CONTRACT CONSISTENCY REPORT
# =========================

Validator return contracts

* Partially resolved: prediction/type/range/normalization validators return list[str], login returns dict, but signup remains list-shaped while auth_service expects dict.

Service call signatures

* Partially resolved: reset/verify/Google callback and prediction-to-ML calls are corrected; Google user creation still relies on repository kwargs compatibility.

Repository contracts

* Partially resolved: repositories accept canonical dictionaries plus compatibility kwargs; serialization still leaks API shape from persistence.

Middleware/service contracts

* Mostly resolved: auth, rate limit, and logging middleware now match service contracts; security sanitized_json is not consumed.

JWT/config consistency

* Mostly resolved by aliases and fallbacks; risk remains if secrets are unset and because expiration naming is ambiguous.

Logger contracts

* Resolved: get_logger accepts optional log file paths and logging_service imports cleanly.

ML inference contracts

* Partially resolved: service-to-ensemble signature matches; app startup does not initialize models and feature validation may not match artifacts.

Schema serialization consistency

* Partially resolved: prediction/history schemas handle renamed fields; repository and schema serializers still duplicate responsibilities.

Fully resolved mismatches

* Email adapter keywords, logger path argument, rate-limit unpacking, controller token/code argument extraction, prediction schema metadata acceptance, collection accessor resolution.

Remaining risks

* Composition root wiring, signup validation return shape, opaque-token/JWT mismatch, response envelope nesting, stale test contracts.

# =========================
# DEPENDENCY FLOW SUMMARY
# =========================

Request lifecycle flow

* Intended flow is Flask app -> middleware -> route -> controller -> service -> repository/ML/external adapter -> schema/response. Current app factory does not assemble this flow.

Controller/service/repository direction

* Routes call controllers; controllers call services; services call validators/repositories/schemas/utilities/external adapters/ML; repositories call database accessors.

Middleware execution order

* Expected before_request concerns are logging start, security sanitization, rate limiting, and authentication; expected after_request concerns are response logging and security headers. Registration is absent in create_app().

ML inference pipeline flow

* prediction_service validates input, maps features, normalizes, converts row to dict, calls ensemble_predictor, which gets feature order/models, runs model adapters, calculates confidence/agreement, and aggregates output.

Authentication flow

* Auth routes delegate to auth_controller; auth_service handles validation, user lookup/create/update, password utilities, JWTs, and email service. auth_middleware uses auth_service.authenticate_access_token().

Prediction orchestration flow

* POST /predict delegates to predict_controller, then prediction_service owns validation, preprocessing, ensemble inference, response serialization, optional history persistence, and logging.
