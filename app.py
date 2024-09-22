from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


tasks = [
    {"title": "school homework",
        "description": "solve 5 questions for math", "completed": False},
    {"title": "fastapi", "description": "mini api with fastapi", "completed": True},
    {"title": "art", "description": "draw one picture", "completed": False}



]


@app.get("/tasks")
def show_tasks():
    return tasks


@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.dict())

    return {"message": "Task added successfully", "task": task}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    if task_id >= len(tasks):
        return {"error": "Task not found"}
    tasks[task_id-1] = task.dict()
    return {"message": "Task updated successfully", "task": task}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id >= len(tasks):
        return {"error": "Task not found"}
    removed_task = tasks.pop(task_id-1)
    return {"message": "Task deleted successfully", "task": removed_task}
