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
