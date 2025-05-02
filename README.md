# Collaborative Task Manager

A simple, full-stack web application for managing your daily tasks. Built with Flask, SQLAlchemy, and Flask-Login, this project lets users register, log in, and securely create, update, or delete their own tasks-all from a clean web interface.

## Features

- User registration and login
- Secure password hashing
- Add, edit, and delete your own tasks
- Mark tasks as completed or pending
- Simple dashboard
- Automated tests for core features

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/collab-task-manager.git
   cd collab-task-manager
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Open your browser and go to**
   ```
   http://127.0.0.1:5000/ #or any other local configuration
   ```

## Usage

- **Register** for a new account or log in with an existing one.
- **Add tasks** using the form at the bottom of the dashboard.
- **Edit or delete tasks** directly in the task list.
- **Mark tasks** as completed or pending from the dashboard.

## Project Structure
```
Collab-Task-Manager/
├── app/
│   ├── __init__.py
│   └── templates/
│       ├── dashboard.html
│       ├── login.html
│       └── register.html
├── run.py
├── requirements.txt
└── tests/
    └── test_app.py
```

## Testing

Automated tests cover user registration, login, logout, and task CRUD operations.

**To run tests:**
```bash
pytest
```

- The test suite uses a temporary in-memory SQLite database, so it won’t affect your real data.
- All tests are located in `tests/test_app.py`.

---

## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug
- Pytest

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## License

This project is open source and free to use for learning, portfolio, or as a starting point for your own projects.

---

## Acknowledgements

Inspired by the Flask community and open source task manager examples.

---

**Enjoy organizing your tasks! If you find this useful, feel free to star the repo or use it as a template for your own projects.**
