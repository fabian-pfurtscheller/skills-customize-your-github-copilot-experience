from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API Assignment")


class TaskIn(BaseModel):
    title: str
    done: bool = False


class Task(TaskIn):
    id: int


tasks: list[Task] = []
next_id = 1


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI assignment API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return tasks


@app.post("/tasks", response_model=Task)
def create_task(payload: TaskIn) -> Task:
    global next_id
    task = Task(id=next_id, **payload.model_dump())
    tasks.append(task)
    next_id += 1
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskIn) -> Task:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated = Task(id=task_id, **payload.model_dump())
            tasks[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
