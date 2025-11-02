# Task Tracker Web Application

A simple Flask-based web application for managing tasks with priority levels and persistent storage.

## Features

- Add tasks with priority levels (1-5)
- View tasks sorted by priority (highest first)
- Delete tasks
- Automatic persistence to local JSON file
- Responsive web interface

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

3. Use the web interface to:
   - Add new tasks with a name and priority level
   - View all tasks sorted by priority
   - Delete tasks by clicking the Delete button

## API Endpoints

### GET /api/tasks
Returns all tasks as JSON array.

**Response:**
```json
[
  {"name": "Task name", "priority": 5}
]
```

### POST /api/tasks
Creates a new task.

**Request Body:**
```json
{
  "name": "Task name",
  "priority": 3
}
```

**Response:**
```json
{"success": true}
```

### DELETE /api/tasks/<index>
Deletes a task at the specified index.

**Response:**
```json
{"success": true}
```

## Data Storage

Tasks are automatically saved to `tasks.json` in the application directory. The file is created automatically on first use and persists between application restarts.

## Project Structure

```
code/
├── app.py              # Flask backend application
├── templates/
│   └── index.html      # Frontend interface
├── requirements.txt    # Python dependencies
├── tasks.json         # Task data storage (auto-generated)
└── README.md          # This file
```

## Classes

### Task
Represents a single task with name and priority.

**Attributes:**
- `name` (str): Task description
- `priority` (int): Priority level (1-5, defaults to 1 if invalid)

### TaskManager
Manages task collection with file persistence.

**Methods:**
- `load_tasks()`: Loads tasks from JSON file
- `save_tasks()`: Saves tasks to JSON file
- `add_task(name, priority)`: Adds and sorts tasks
- `get_tasks()`: Returns tasks as dictionaries
- `remove_task(index)`: Removes task at index
