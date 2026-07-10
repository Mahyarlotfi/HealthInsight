# Architecture

## Purpose

This document describes the software architecture of the HealthInsight project.

The goal is to define a clear, maintainable, and scalable architecture that supports future expansion while keeping the codebase organized and easy to understand.

---

# Architecture Style

HealthInsight follows the **Layered Architecture** pattern.

This architecture separates the application into independent layers, where each layer has a single responsibility.

Benefits include:

- Clear separation of responsibilities.
- Easier maintenance.
- Better testability.
- Reduced coupling.
- Improved scalability.
- Easier migration to different user interfaces.
- Easier migration to different databases.

---

# Architecture Layers

The application consists of the following layers:

## 1. Presentation Layer

Responsible for interacting with the user.

Current implementation:

- Command Line Interface (CLI)

Possible future implementations:

- KivyMD Desktop Application
- Django Web Application
- FastAPI REST API
- Flutter Mobile Application (through an API)

Responsibilities:

- Receive user input.
- Display application output.
- Validate basic user input.
- Call the appropriate service.

---

## 2. Service Layer

Contains the application's business logic.

Responsibilities:

- Process user requests.
- Validate business rules.
- Coordinate application operations.
- Communicate with repositories.
- Return processed results.

The Service Layer never communicates directly with the database.

---

## 3. Repository Layer

Responsible for data access.

Responsibilities:

- Read data.
- Write data.
- Update data.
- Delete data.
- Hide database implementation details from the rest of the application.

Repositories are the only layer allowed to communicate with the database.

---

## 4. Database Layer

Responsible for database configuration and persistence.

Responsibilities:

- Configure the database engine.
- Create database sessions.
- Manage database connections.
- Execute SQLAlchemy operations.

The initial database engine is:

- SQLite

Future migration may include:

- PostgreSQL

---

# Data Models

Database models represent the application's entities.

Examples include:

- User
- Medication
- MedicationLog
- DailyRecord
- Activity
- Measurement
- Symptom
- LabResult
- Photo

Models are defined using SQLAlchemy.

---

# Layer Communication Rules

Communication is strictly one-directional.

```text
Presentation
      │
      ▼
Services
      │
      ▼
Repositories
      │
      ▼
Database
```

Allowed communication:

- Presentation → Services
- Services → Repositories
- Repositories → Database

Not allowed:

- Presentation → Database
- Presentation → Repositories
- Services → Database

This rule keeps the architecture loosely coupled and easy to maintain.

---

# Project Structure

```text
HealthInsight/
├── docs/
├── src/
│   └── healthinsight/
│       ├── presentation/
│       │   └── cli/
│       ├── services/
│       ├── repositories/
│       ├── models/
│       ├── database/
│       └── utils/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

---

# Application Flow

The execution flow of the application is:

```text
main.py
    │
    ▼
Presentation Layer
    │
    ▼
Service Layer
    │
    ▼
Repository Layer
    │
    ▼
Database Layer
```

Each layer has a single responsibility and communicates only with the next layer.

---

# Design Principles

HealthInsight follows these software design principles:

- Single Responsibility Principle (SRP)
- Separation of Concerns (SoC)
- Low Coupling
- High Cohesion
- Keep It Simple (KISS)
- Don't Repeat Yourself (DRY)

These principles help keep the project maintainable as it grows.

---

# Future Expansion

The architecture is designed to support future features without major structural changes.

Possible future additions include:

- Graphical Desktop Application
- Web Application
- REST API
- Mobile Application
- Multiple Database Support
- Cloud Synchronization

No significant changes to the business logic should be required when adding new presentation layers.

---

## Technologies

### Core

- Python 3

### Database

- SQLite
- SQLAlchemy
- Alembic

### Development

- Git
- Pytest
- Black
- isort
- Pylint

---

# Summary

HealthInsight uses a Layered Architecture to separate presentation, business logic, data access, and database responsibilities.

This design improves readability, maintainability, testability, and scalability while preparing the project for future expansion.