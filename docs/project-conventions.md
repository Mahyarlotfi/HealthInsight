# Project Conventions

## Purpose

This document defines the coding standards and development conventions used throughout the HealthInsight project.

Following these conventions helps maintain a clean, consistent, and maintainable codebase.

---

# General Principles

- Keep the code simple.
- Write readable code.
- Prefer clarity over cleverness.
- Avoid duplicated code.
- Keep functions small and focused.
- Each module should have a single responsibility.

---

# Naming Conventions

## Files

Use **snake_case**.

Examples:

- `user_service.py`
- `database.py`
- `daily_record.py`

---

## Directories

Use **snake_case**.

Examples:

- `models`
- `repositories`
- `services`

---

## Classes

Use **PascalCase**.

Examples:

- `User`
- `Medication`
- `DailyRecord`

---

## Functions

Use **snake_case**.

Examples:

- `create_user()`
- `add_medication()`
- `calculate_whr()`

---

## Variables

Use **snake_case**.

Examples:

- `blood_pressure`
- `daily_record`
- `target_weight`

---

## Constants

Use **UPPER_CASE**.

Examples:

- `DEFAULT_DATABASE`
- `MAX_NAME_LENGTH`

---

# Project Structure

The project follows a Layered Architecture.

```text
Presentation
    ↓
Services
    ↓
Repositories
    ↓
Database
```

Each layer communicates only with the next layer.

---

# Imports

Import order:

1. Python Standard Library
2. Third-party Packages
3. Local Project Imports

Example:

```python
from pathlib import Path

from sqlalchemy import create_engine

from healthinsight.database.session import SessionLocal
```

Imports should be automatically sorted using **isort**.

---

# Formatting

Code formatting is handled by **Black**.

Rules:

- Do not manually format code unnecessarily.
- Run Black before committing.

Command:

```bash
black .
```

---

# Import Sorting

Import sorting is handled by **isort**.

Command:

```bash
isort .
```

---

# Code Quality

Static analysis is performed using **Pylint**.

Command:

```bash
pylint src
```

Requirements:

- Fix all errors.
- Address important warnings.
- Review remaining warnings before committing.

---

# Type Hints

Use type hints whenever practical.

Example:

```python
def calculate_bmi(weight: float, height: float) -> float:
    ...
```

---

# Docstrings

Public classes and public functions should include docstrings.

Module docstrings are optional.

Example:

```python
def create_user(name: str) -> None:
    """Create a new user."""
```

---

# Comments

Write comments only when they improve understanding.

Avoid explaining obvious code.

Prefer self-explanatory code over excessive comments.

---

# Testing

Tests should be written using **pytest**.

Rules:

- Add tests for new features.
- Keep tests independent.
- Use descriptive test names.

---

# Git

Before every commit:

- Review changes.
- Run isort.
- Run Black.
- Run Pylint.
- Run pytest.
- Review documentation.

Commit messages should be short and meaningful.

Examples:

- Add medication repository
- Implement user model
- Update database design
- Fix validation logic

---

# Documentation

Whenever the project changes, update documentation if necessary.

Update the following documents when applicable:

- README.md
- roadmap.md
- features.md
- architecture.md
- database-design.md

---

# Future Changes

These conventions may evolve as the project grows.

Any significant changes should be documented in this file.