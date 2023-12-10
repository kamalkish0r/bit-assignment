# Task Manager API

This Django-based RESTful API enables CRUD operations for task management. Users can perform various actions like creating, reading, updating, and deleting tasks.

## Features

- **Task Model:** Allows users to manage tasks with fields for title, description, due date, and status.
- **API Endpoints:** Supports CRUD operations for tasks, including listing, retrieval, creation, updating, and deletion.
- **Authentication:** Implements token-based authentication for secure access to API endpoints.
- **Permissions:** Ensures users can only modify tasks they own through proper permission handling.
- **Unit Tests:** Includes comprehensive unit tests for API views to ensure functionality.

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Usage

### Authentication

- To obtain a token, use the `/login/` endpoint with your username and password.
- Register a new user via the `/register/` endpoint.

### Endpoints

- `/task_manager/tasks/`: List all tasks (GET), create a new task (POST).
- `/task_manager/tasks/{task_id}/`: Retrieve (GET), update (PUT/PATCH), delete (DELETE) a specific task.

### Error Handling

The API returns standard HTTP status codes to indicate success or failure:

- `200 OK`, `201 Created`: Successful requests.
- `400 Bad Request`, `401 Unauthorized`: Invalid requests or unauthorized access.
- `403 Forbidden`: No permission to perform an action.
- `404 Not Found`: Requested resource doesn't exist.

## Testing

Run unit tests using the command:

```bash
python manage.py test
```

## Documentation
[API Documentation](api-documentation.md): Detailed documentation for using the API, including endpoints, authentication methods, error handling, and usage instructions.
