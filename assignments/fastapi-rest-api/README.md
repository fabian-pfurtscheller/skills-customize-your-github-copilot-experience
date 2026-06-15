# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a simple REST API using the FastAPI framework. You will practice creating endpoints, handling request/response data, and implementing basic API behavior for create, read, update, and delete operations.

## 📝 Tasks

### 🛠️	Set Up a FastAPI App and Core Endpoints

#### Description
Create a FastAPI application and implement foundational endpoints so the service can be started and tested in the browser or with API tools.

#### Requirements
Completed program should:

- Define a FastAPI app instance in `starter-code.py`.
- Implement a `GET /` endpoint that returns a JSON welcome message.
- Implement a `GET /health` endpoint that returns a JSON status (for example, `{ "status": "ok" }`).
- Run successfully with `uvicorn starter-code:app --reload` without startup errors.


### 🛠️	Implement In-Memory CRUD Endpoints

#### Description
Build REST endpoints to manage a small in-memory collection of items (for example, tasks). Add endpoints to create, list, update, and delete entries.

#### Requirements
Completed program should:

- Implement `POST /tasks` to create a new task and return the created object.
- Implement `GET /tasks` to return all stored tasks as JSON.
- Implement `PUT /tasks/{task_id}` to update an existing task by ID.
- Implement `DELETE /tasks/{task_id}` to remove a task by ID and return a clear confirmation message.
- Return an appropriate error response when a task ID does not exist (for example, status code `404`).
