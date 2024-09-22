# FastAPI Task Manager

A simple task management API built with FastAPI to perform CRUD (Create, Read, Update, Delete) operations on tasks.

## Features

- **View Tasks:** Fetch all tasks using a `GET` request.
- **Add Task:** Add a new task using a `POST` request.
- **Update Task:** Update an existing task using a `PUT` request.
- **Delete Task:** Delete a task using a `DELETE` request.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the app)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-task-manager.git
   cd fastapi-task-manager
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux
   .\venv\Scripts\activate    # On Windows
   ```

3. Install the required packages:

   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

To run the FastAPI app using Uvicorn, execute the following command:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Get All Tasks

- **Method:** `GET`
- **URL:** `/tasks`
- **Description:** Fetches the list of all tasks.

### Add a New Task

- **Method:** `POST`
- **URL:** `/tasks`
- **Body:**
  ```json
  {
    "title": "New Task",
    "description": "Description of the new task",
    "completed": false
  }
  ```
- **Description:** Adds a new task to the list.

### Update a Task

- **Method:** `PUT`
- **URL:** `/tasks/{task_id}`
- **Body:**
  ```json
  {
    "title": "Updated Task",
    "description": "Updated description",
    "completed": true
  }
  ```
- **Description:** Updates a task based on its `task_id`.

### Delete a Task

- **Method:** `DELETE`
- **URL:** `/tasks/{task_id}`
- **Description:** Deletes a task based on its `task_id`.

## Example

### Adding a Task:

To add a new task, send a `POST` request to `/tasks` with a JSON body like this:

```json
{
  "title": "Learn FastAPI",
  "description": "Build a simple API using FastAPI",
  "completed": false
}
```

### Response:

```json
{
  "message": "Task added successfully",
  "task": {
    "title": "Learn FastAPI",
    "description": "Build a simple API using FastAPI",
    "completed": false
  }
}
```
