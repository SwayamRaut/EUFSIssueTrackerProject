# Formula Car Issue Tracker API

A backend project for tracking technical issues on a Formula car and the components affected by them.

I built this project while working through backend engineering fundamentals and preparing to contribute to EUFS Edinburgh. The main goal was to move beyond an in-memory CRUD API and build something with a proper database, migrations, layered application structure, and a repeatable Docker setup.

## What it does

The API currently supports issue and component management, including:

- creating, reading, updating, and deleting issues
- creating and managing car components
- linking issues to the relevant component
- filtering and paginating issue data
- request and response validation with Pydantic
- persistent storage in PostgreSQL
- database schema migrations with Alembic

FastAPI also provides interactive API documentation at `/docs` while the application is running.

## Stack

- **Python**
- **FastAPI** — API routes and dependency injection
- **Pydantic** — request/response validation
- **SQLAlchemy 2.0** — ORM and database access
- **PostgreSQL** — relational database
- **Alembic** — schema migrations
- **Docker / Docker Compose** — local containerized environment
- **Git**

## Project structure

```text
EUFSIssueTrackerProject/
├── alembic/              # database migrations
├── app/
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # FastAPI routes
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # application/service logic
│   └── database.py       # database session and engine setup
├── alembic.ini
├── compose.yaml
├── Dockerfile
├── main.py
└── requirements.txt

Running with Docker

Docker Compose runs the API and PostgreSQL as separate containers.

docker compose up --build

The API is available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs
First-time database setup

On a fresh PostgreSQL volume, apply the existing Alembic migrations:

docker compose exec app alembic upgrade head

This brings the database schema up to the latest migration revision.

The PostgreSQL data is stored in a Docker named volume, so stopping or recreating the containers does not remove the database data.

Configuration

The application expects the following database environment variables:

DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
DB_NAME

When running through Docker Compose, the API connects to PostgreSQL over the Compose network using the database service name rather than localhost.

Why I built it

This started as a way to properly learn Python backend development rather than only build endpoints that worked locally. While building it I worked through FastAPI application structure, relational data modelling, SQLAlchemy sessions, Alembic migrations, PostgreSQL, Linux/Bash, Docker images and containers, volumes, networking, and port mapping.

The project is still being developed. Authentication, automated testing, CI/CD, and deployment are planned as the next steps.
