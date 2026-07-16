# FOOD - Turkish Regional Food Platform

FOOD is an actively developed Django application designed to map, explore, and preserve Turkey's rich regional culinary heritage. The project is currently in its alpha stage and is not ready for production deployment.

## Overview

This project aims to provide the highest quality regional food platform in Turkey. Built on the principles of **Clean Architecture**, it separates concerns strictly to maintain long-term scalability, security, and performance.

## Tech Stack

- **Framework**: Django 6.0
- **Language**: Python 3.14
- **Database**: PostgreSQL
- **Linting & Formatting**: Ruff
- **Type Checking**: Mypy & Pyright
- **Testing**: Pytest & pytest-django

## Architecture & Code Rules

The project strictly follows a layered architecture to keep components decoupled:

1. **Models**: Defines database structure and indexes. Only models live here.
2. **Selectors**: Read-only operations. All database queries must go through selectors.
3. **Services**: Business logic and write operations. The only layer allowed to change state.
4. **Validators**: Input validation rules.
5. **Views/URLs**: Handlers for HTTP requests and routing.

*See the `docs/` directory for full documentation including architecture, deployment, and security guidelines.*

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python 3.14 installed.
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```
4. Install the application in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Development Commands

- **Linting & Formatting**:
  ```bash
  ruff check .
  ruff format .
  ```
- **Type Checking**:
  ```bash
  mypy .
  pyright
  ```
- **Testing**:
  ```bash
  pytest
  ```

## License

Proprietary - All rights reserved by the FOOD Project.
