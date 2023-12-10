# Task Manager API Documentation

## Authentication

### Obtain Token

To access the API endpoints, users need to authenticate using a token:

- **Endpoint:** `/login/`
  - **Method:** POST
  - **Request Body:** `{ "username": "<your-username>", "password": "<your-password>" }`
  - **Response:** `{ "token": "<your-token>", "user_id": "<user-id>", "username": "<username>" }`

### User Registration

For new users to register:

- **Endpoint:** `/register/`
  - **Method:** POST
  - **Request Body:** `{ "username": "<new-username>", "password": "<new-password>" }`
  - **Response:** `{ "token": "<new-user-token>" }`

**Note:** Include the `Authorization` header in subsequent requests with the format `Authorization: Token <your-token>`.

## Endpoints

### Tasks

#### List all tasks

- **Endpoint:** `/task_manager/tasks/`
  - **Method:** GET
  - **Authentication:** Token required

#### Create a new task

- **Endpoint:** `/task_manager/tasks/`
  - **Method:** POST
  - **Authentication:** Token required
  - **Request Body:** `{ "title": "<task-title>", "description": "<task-description>", "due_date": "<due-date>", "status": "<task-status>" }`

#### Retrieve a specific task

- **Endpoint:** `/task_manager/tasks/{task_id}/`
  - **Method:** GET
  - **Authentication:** Token required

#### Update a specific task

- **Endpoint:** `/task_manager/tasks/{task_id}/`
  - **Method:** PUT / PATCH
  - **Authentication:** Token required
  - **Request Body:** `{ "title": "<updated-title>", "description": "<updated-description>", "due_date": "<updated-due-date>", "status": "<updated-status>" }`

#### Delete a specific task

- **Endpoint:** `/task_manager/tasks/{task_id}/`
  - **Method:** DELETE
  - **Authentication:** Token required

## Error Handling

The API returns standard HTTP status codes:

- `200 OK`, `201 Created`: Successful requests.
- `400 Bad Request`: Invalid requests or missing parameters.
- `401 Unauthorized`: Unauthorized access or invalid tokens.
- `403 Forbidden`: Insufficient permissions.
- `404 Not Found`: Resource not found.

## Usage

1. **Token:** After authentication, use the obtained token in the `Authorization` header: `Authorization: Token <your-token>`.
2. **Requests:** Use appropriate methods and endpoints with valid request bodies to interact with the API.

## Contributing

Contributions, issues, and pull requests are welcome! Please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This API is licensed under the [MIT License](LICENSE).
