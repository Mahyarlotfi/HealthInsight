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
- Follow the existing project style instead of introducing new patterns.

---

# Naming Conventions

## Files

Use **snake_case**.

Examples:

- `user.py`
- `daily_record.py`
- `medication_repository.py`

---

## Directories

Use **snake_case**.

Examples:

- `models`
- `repositories`
- `database`
- `config`

---

## Classes

Use **PascalCase**.

Examples:

- `User`
- `Medication`
- `DailyRecord`
- `MedicationRepository`

---

## Functions

Use **snake_case**.

Examples:

- `create_user()`
- `find_by_user()`
- `calculate_bmi()`

---

## Variables

Use **snake_case**.

Examples:

- `daily_record`
- `target_weight`
- `blood_pressure`

---

## Constants

Use **UPPER_CASE**.

Examples:

- `DATABASE_URL`
- `DEFAULT_PAGE_SIZE`

---

# Project Structure

The project follows a layered architecture.

```text
Configuration
      │
Database
      │
Models
      │
Repositories
      │
Future Service Layer
      │
Future API / UI Layer
```

Each layer should depend only on the layer directly below it.

---

# Imports

Import order:

1. Python Standard Library
2. Third-party Packages
3. Local Project Imports

Example:

```python
from datetime import date

from sqlalchemy import select

from healthinsight.models.user import User
```

Imports are automatically organized by **Ruff**.

---

# Formatting

Formatting is handled by **Ruff Formatter**.

Run:

```bash
ruff format .
```

Do not manually reformat code unless necessary.

---

# Linting

Linting is handled by **Ruff**.

Run:

```bash
ruff check . --fix
```

Requirements:

- Fix all reported issues.
- Review automatic fixes before committing.
- Do not ignore warnings without a good reason.

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

Public modules, classes, and functions should include docstrings.

Example:

```python
def create_user(name: str) -> None:
    """Create a new user."""
```

---

# Comments

Write comments only when they improve understanding.

Avoid comments that explain obvious code.

Prefer descriptive names over explanatory comments.

---

# Testing

Testing is performed using **pytest**.

Rules:

- Every new feature should include tests.
- Tests must be independent.
- Test names should clearly describe the expected behavior.
- Existing tests must continue to pass.

Run:

```bash
pytest
```

---

# Git Workflow

Before every commit:

- Review all changes.
- Run:

```bash
ruff check . --fix
ruff format .
pytest
```

- Verify `git status`.
- Review `git diff`.
- Ensure only intended files are included.
- Update documentation if necessary.

Commit messages should follow the Conventional Commits specification.

Examples:

```text
feat(repository): implement MedicationRepository
feat(models): implement DailyRecord model
fix(database): resolve relationship loading issue
refactor(repository): simplify query methods
test(repository): add MedicationRepository tests
docs: update project conventions
build: add pyproject configuration
```

---

# Documentation

Keep documentation synchronized with the codebase.

Review and update when necessary:

- `README.md`
- `docs/roadmap.md`
- `docs/features.md`
- `docs/database-design.md`
- `docs/architecture.md`
- `docs/user-flow.md`

---

# Dependency Management

Project dependencies are managed using **uv**.

Install project dependencies:

```bash
uv sync
```

Install development dependencies:

```bash
uv sync --extra dev
```

---

# Project Quality Checklist

Before pushing any changes:

- [ ] Feature is complete.
- [ ] Ruff passes successfully.
- [ ] Code is formatted.
- [ ] Tests pass.
- [ ] Documentation is updated if required.
- [ ] No temporary or generated files are included.
- [ ] No secrets or sensitive information are committed.
- [ ] `git status` is clean except for intended changes.

---

# Future Changes

These conventions may evolve as the project grows.

Any significant changes should be documented in this file.