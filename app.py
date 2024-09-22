from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI()

# Define a Pydantic model for a Task, with fields for title, description, and completion status


class Task(BaseModel):
    title: str  # Title of the task
    description: str  # Description of the task
    # Optional: defaults to False if not provided, indicating the task is not yet completed
    completed: bool = False


# Initial in-memory list of tasks for demonstration purposes
tasks = [
    {
        "title": "school homework",
        "description": "solve 5 questions for math",
        "completed": False
    },
    {
        "title": "fastapi",
        "description": "mini api with fastapi",
        "completed": True
    },
    {
        "title": "art",
        "description": "draw one picture",
        "completed": False
    }
]

# GET request to retrieve all tasks


@app.get("/tasks")
def show_tasks():
    """
    Endpoint to fetch the list of all tasks.
    :return: List of tasks
    """
    return tasks

# POST request to add a new task


@app.post("/tasks")
def add_task(task: Task):
    """
    Endpoint to add a new task to the list.
    :param task: Task object passed in the request body
    :return: Message confirming task addition and the added task
    """
    tasks.append(task.dict())
    return {"message": "Task added successfully", "task": task}

# PUT request to update an existing task by its task_id


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    if task_id >= len(tasks):
        return {"error": "Task not found"}

    tasks[task_id-1] = task.dict()
    return {"message": "Task updated successfully", "task": task}

# DELETE request to remove a task by its task_id


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id >= len(tasks):
        return {"error": "Task not found"}

    removed_task = tasks.pop(task_id-1)
    return {"message": "Task deleted successfully", "task": removed_task}
