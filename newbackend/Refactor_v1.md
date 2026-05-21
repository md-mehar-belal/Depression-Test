# Backend Refactor & API Stabilization Documentation

Source reviewed: `ARCHITECTURE_REFERENCE_v1.md` 

---

# 1. Critical Runtime Wiring Fixes

## 1.1 Application Factory Is Incomplete

### Files

* `app/__init__.py`
* `run.py`

### Current Problem

The application factory only loads configuration and does not assemble the runtime system.

Missing:

* Blueprint registration
* Middleware registration
* Error handler registration
* Database initialization
* ML initialization
* Logging initialization

### Required Changes

`create_app()` must:

1. Create Flask app
2. Load config/env
3. Initialize logger
4. Connect MongoDB
5. Initialize ML models
6. Register middleware
7. Register error handlers
8. Register blueprints
9. Return fully initialized app

### Required Registrations

#### Blueprints

* auth routes
* prediction routes
* history routes

#### Middleware

Before request:

1. logging middleware
2. sanitize middleware
3. rate limit middleware
4. authentication middleware

After request:

1. response logging
2. security headers

#### Error Handlers

* validation errors
* authentication errors
* generic server errors

### Runtime Risk

HIGH

### Impact If Unfixed

* 404 routes
* middleware not executed
* prediction failures
* auth bypass
* DB unavailable
* startup instability

---

# 2. ML Initialization Is Not Wired

## Files

* `app/__init__.py`
* `ml/inference/model_loader.py`
* `app/services/prediction_service.py`

### Current Problem

`initialize_ml_models()` exists but is never called during startup.

### Required Changes

Call:

```python
initialize_ml_models()
```

during application startup.

### Additional Requirements

* Fail startup if model loading fails
* Validate model registry contents
* Validate feature order files exist

### Runtime Risk

HIGH

### Impact If Unfixed

* `/predict` crashes
* empty model registry
* inference failures

---

# 3. Signup Validation Contract Mismatch

## Files

* `app/validators/auth_validator.py`
* `app/services/auth_service.py`

### Current Problem

Validator and service use incompatible return contracts.

Current behavior:

* validator returns list
* service expects dict

### Required Changes

Standardize validator return format.

Recommended contract:

```python
{
    "valid": bool,
    "errors": list[str]
}
```

### Additional Requirement

All validators must follow identical structure.

### Runtime Risk

HIGH

### Impact If Unfixed

* signup failures
* malformed validation responses
* inconsistent error handling

---

# 4. Email Verification / Password Reset Token System Is Broken

## Files

* `app/services/auth_service.py`
* `app/services/email_service.py`
* `app/services/jwt_service.py`

### Current Problem

Random opaque tokens are generated but later verified using JWT verification.

This is architecturally incompatible.

### Required Changes

Choose ONE system only.

---

## Option A (Recommended): JWT-based tokens

### Flow

* generate JWT
* email JWT
* verify JWT directly

### Advantages

* stateless
* scalable
* cleaner architecture

---

## Option B: Database-backed opaque tokens

### Flow

* generate random token
* store hash in DB
* verify against DB

### Requirements

* expiration storage
* cleanup mechanism
* revocation support

---

### Runtime Risk

HIGH

### Impact If Unfixed

* reset password flow fails
* email verification fails

---

# 5. Sanitization Middleware Is Ineffective

## Files

* `app/middleware/security_middleware.py`
* `app/controllers/*.py`

### Current Problem

Middleware stores:

```python
request.sanitized_json
```

Controllers ignore it and call:

```python
request.get_json()
```

### Required Changes

Controllers must use:

```python
request.sanitized_json
```

with fallback logic.

### Runtime Risk

MEDIUM

### Security Risk

HIGH

### Impact If Unfixed

* XSS sanitization bypass
* SQL injection filtering bypass

---

# 6. Response Contract Ownership Is Split

## Files

* `app/controllers/*.py`
* `app/services/*.py`
* `app/utils/response.py`

### Current Problem

Both services and controllers build response envelopes.

Can produce:

```json
{
  "success": true,
  "data": {
      "success": true
  }
}
```

### Required Changes

Define strict ownership.

Recommended:

* services return raw business data
* controllers build HTTP responses

### Runtime Risk

MEDIUM

### Impact If Unfixed

* inconsistent API contracts
* frontend integration confusion

---

# 7. Repository Contract Is Loose

## Files

* `app/services/google_auth_service.py`
* `app/repositories/user_repository.py`

### Current Problem

Repository accepts compatibility kwargs.

Current usage:

```python
create_user(name=..., email=..., password=None)
```

Canonical repository contract expects:

```python
create_user(user_data: dict)
```

### Required Changes

* remove compatibility kwargs
* enforce strict repository API
* update Google auth service

### Runtime Risk

MEDIUM

### Impact If Unfixed

* future refactor breakage
* hidden coupling

---

# 8. Serialization Responsibility Is Duplicated

## Files

* `app/repositories/user_repository.py`
* `app/repositories/prediction_repository.py`
* `app/schemas/*.py`

### Current Problem

Repositories serialize documents while schemas also serialize them.

### Required Changes

Repositories:

* return raw DB documents only

Schemas:

* own API serialization completely

### Runtime Risk

MEDIUM

### Impact If Unfixed

* schema drift
* inconsistent response shapes

---

# 9. Prediction Validation Is Not ML-Aware

## Files

* `app/validators/prediction_validator.py`
* `ml/inference/model_loader.py`
* `ml/preprocessing/feature_mapper.py`

### Current Problem

Validation uses static assumptions while ML feature order is dynamic.

### Required Changes

* validators must validate against loaded feature order artifacts
* avoid hardcoded assumptions

### Runtime Risk

MEDIUM

### Impact If Unfixed

* valid requests fail during inference
* hidden ML contract mismatch

---

# 10. JWT Configuration Must Be Mandatory

## Files

* `app/config.py`
* `.env`
* `app/services/jwt_service.py`

### Required Environment Variables

```env
JWT_SECRET_KEY=
JWT_ACCESS_TOKEN_EXPIRES=
JWT_REFRESH_TOKEN_EXPIRES=

MONGO_URI=
DATABASE_NAME=
```

### Recommended Additional Variables

```env
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

SMTP_HOST=
SMTP_PORT=
SMTP_USERNAME=
SMTP_PASSWORD=
MAIL_FROM=
```

### Required Changes

* fail startup if missing
* validate config during app boot

### Runtime Risk

HIGH

### Security Risk

HIGH

### Impact If Unfixed

* broken auth
* insecure JWT generation
* startup instability

---

# 11. Database Lifecycle Is Incomplete

## Files

* `app/database/database.py`
* `app/__init__.py`

### Required Changes

* connect DB during startup
* close DB cleanly during shutdown
* fail startup if DB unavailable

### Runtime Risk

HIGH

### Impact If Unfixed

* runtime DB failures
* unstable API behavior

---

# 12. Middleware Registration Order Must Be Controlled

## Files

* `app/__init__.py`

### Required Before Request Order

1. logging
2. sanitize
3. rate limit
4. auth

### Required After Request Order

1. response logging
2. security headers

### Runtime Risk

MEDIUM

### Impact If Unfixed

* inconsistent request handling
* logging gaps
* auth inconsistencies

---

# 13. Protected Routes Must Use JWT Consistently

## Files

* `app/routes/*.py`

### Required Protected Endpoints

* `/predict`
* `/history`
* `/me`
* `/logout`

### Required Changes

Use JWT decorators consistently.

### Security Risk

HIGH

### Impact If Unfixed

* unauthorized access

---

# 14. Prediction Pipeline Needs Defensive Failure Handling

## Files

* `app/services/prediction_service.py`
* `ml/inference/*.py`

### Required Changes

Handle:

* missing models
* empty ensembles
* invalid feature order
* inference exceptions
* preprocessing failures

### Required Behavior

Return controlled API errors.

### Runtime Risk

HIGH

### Impact If Unfixed

* 500 server crashes

---

# 15. Duplicate Validators Exist Inside Tests

## Files

* `tests/validators/*.py`

### Current Problem

Test validators duplicate production validators.

### Required Changes

Tests must import production validators directly.

### Runtime Risk

LOW

### Maintenance Risk

MEDIUM

### Impact If Unfixed

* false-positive tests
* stale validation logic

---

# 16. ML Test Contracts May Be Stale

## Files

* `tests/ml/*.py`
* `tests/prediction/*.py`

### Current Problem

Some tests target old return shapes and pre-refactor contracts.

### Required Changes

* align tests with current service contracts
* remove outdated assertions
* ensure real integration flow coverage

### Maintenance Risk

MEDIUM

### Impact If Unfixed

* misleading test coverage
* unstable CI

---

# 17. Final Required Architecture State

The final runtime flow must become:

```text
Flask App
    ↓
Middleware
    ↓
Routes
    ↓
Controllers
    ↓
Services
    ↓
Validators / ML / Repositories / External APIs
    ↓
Schemas
    ↓
HTTP Response
```

---

# 18. Highest Priority Fix Order

Implement in this order:

1. Application factory wiring
2. DB initialization
3. ML initialization
4. JWT/token flow fix
5. Signup validator contract fix
6. Response contract cleanup
7. Sanitization integration
8. Repository/schema separation
9. ML-aware validation
10. Test cleanup

---

# Final Assessment

## Current State

* Strong layered architecture foundation
* Good modular separation
* Major runtime composition gaps remain

## Production Readiness

NOT production ready yet.

## Highest Risks

1. incomplete startup composition
2. broken auth token lifecycle
3. unloaded ML registry
4. validator contract mismatch
5. ineffective sanitization
