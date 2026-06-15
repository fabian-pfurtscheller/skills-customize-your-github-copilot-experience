# 📘 Assignment: FastAPI Authentication Basics

## 🎯 Objective

In this assignment, you will secure a FastAPI application with simple API key authentication. You will learn how to protect endpoints, validate credentials, and return proper unauthorized error responses.

## 📝 Tasks

### 🛠️	Add API Key Authentication to FastAPI

#### Description
Set up a FastAPI app that checks for an API key in request headers. Implement reusable authentication logic so protected endpoints can enforce access control.

#### Requirements
Completed program should:

- Define a FastAPI app in `starter-code.py`.
- Read an API key from a constant or environment variable.
- Validate a header (for example, `X-API-Key`) in a reusable dependency function.
- Return `401 Unauthorized` when the API key is missing or invalid.


### 🛠️	Create Public and Protected Endpoints

#### Description
Implement both public and protected routes to demonstrate authentication behavior and access control in the API.

#### Requirements
Completed program should:

- Implement at least one public endpoint (for example, `GET /` or `GET /health`) that does not require authentication.
- Implement at least two protected endpoints (for example, `GET /profile` and `GET /notes`) that require a valid API key.
- Return JSON responses for both success and error cases.
- Include clear success messages so students can verify when authentication works correctly.
