# Cybersecurity Monitoring System — Backend

Backend service for the Cybersecurity Monitoring System group project. Built with FastAPI, PostgreSQL, and SQLAlchemy.

## Role
Backend & Database Engineer — responsible for building the core backend infrastructure: database design, REST APIs, authentication, and connecting the detection engine to persistent storage.

## Tech Stack
- **Python** + **FastAPI** — web framework
- **PostgreSQL** — database (running in Docker)
- **SQLAlchemy** — ORM
- **Alembic** — database migrations
- **Pydantic** — request/response validation
- **pytest** — testing

## Project Structure

backend/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── database.py # SQLAlchemy engine/session setup
│ ├── models/ # SQLAlchemy models (DB tables)
│ ├── schemas/ # Pydantic schemas (request/response shapes)
│ ├── routers/ # API route definitions
│ └── crud/ # Database query logic
├── alembic/ # Database migration files
├── tests/ # pytest tests
├── .env # Local environment variables (not committed)
├── .env.example # Template for required env vars
└── requirements.txt


## Database Schema (planned)
- **Users** — id, email, hashed_password, role, created_at, last_login
- **Devices** — id, hostname, ip_address, os_type, status, last_seen, owner_user_id (FK → Users)
- **Events** — id, device_id (FK), event_type, source, payload (JSONB), timestamp, ingested_at
- **Alerts** — id, device_id (FK), event_id (FK), rule_name, severity, status, assigned_to, created_at, resolved_at

## Setup

1. Clone the repo and `cd backend`
2. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Copy `.env.example` to `.env` and fill in your local database credentials
5. Start PostgreSQL via Docker:

docker run --name cyber-monitor-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=yourpassword -e POSTGRES_DB=cybermonitor -p 5432:5432 -d postgres

6. Run migrations:

alembic upgrade head

7. Start the server:

uvicorn app.main:app --reload

8. API docs available at `http://127.0.0.1:8000/docs`

## Progress Log
- [x] FastAPI project scaffolded with health check endpoint
- [x] PostgreSQL running via Docker
- [x] SQLAlchemy connected to database
- [x] Alembic configured for migrations
- [x] `Users` model created and migrated
- [ ] `Devices` model
- [ ] `Events` model
- [ ] `Alerts` model
- [ ] Authentication (JWT)
- [ ] REST endpoints for all resources
- [ ] Detection engine integration
- [ ] pytest test suite