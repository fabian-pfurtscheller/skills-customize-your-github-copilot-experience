import os
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, status

app = FastAPI(title="FastAPI Authentication Basics")

# Keep this simple for students; they can replace it with a stronger secret.
API_KEY = os.getenv("API_KEY", "classroom-secret")


def require_api_key(x_api_key: Annotated[str | None, Header()] = None) -> None:
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome! This is a public endpoint."}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/profile", dependencies=[Depends(require_api_key)])
def profile() -> dict[str, str]:
    return {"username": "student", "role": "api-user"}


@app.get("/notes", dependencies=[Depends(require_api_key)])
def notes() -> dict[str, list[str]]:
    return {"items": ["Finish FastAPI homework", "Test protected routes"]}
