# 🚀 FastAPI Backend Boilerplate

A minimal, production-ready backend starter built with **FastAPI**, **PostgreSQL**, **Redis**, and **SQLAlchemy (async)**. Skip the boilerplate setup and start building features immediately.

## Tech Stack

- **Python** 3.13
- **FastAPI** — async web framework
- **SQLAlchemy 2.0** — async ORM with `asyncpg` driver
- **Alembic** — database migrations
- **PostgreSQL** — primary database
- **Redis** — caching / task queue
- **Pydantic Settings** — environment variable management
- **Uvicorn** — ASGI server
- **uv** — fast Python package manager
- **Ruff** — linter & formatter
- **Pytest** — testing

## Prerequisites

- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Redis](https://redis.io/docs/getting-started/)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

| Variable       | Description                          | Example                                          |
|----------------|--------------------------------------|--------------------------------------------------|
| `DATABASE_URL` | Async PostgreSQL connection string   | `postgresql+asyncpg://user:pass@localhost/db`    |
| `REDIS_URL`    | Redis connection string              | `redis://localhost:6379`                         |

### 4. Run database migrations

```bash
uv run alembic upgrade head
```

### 5. Start the development server

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

## Project Structure

```
.
├── alembic/                 # Migration scripts
│   ├── versions/            # Auto-generated migration files
│   └── env.py               # Alembic environment config
├── app/
│   ├── core/
│   │   └── config.py        # App settings (via pydantic-settings)
│   ├── db/
│   │   ├── base.py          # SQLAlchemy declarative base
│   │   ├── models/          # ORM models
│   │   └── session.py       # Async engine & session factory
│   └── main.py              # FastAPI app entry point
├── alembic.ini              # Alembic configuration
├── pyproject.toml           # Project metadata & dependencies
└── .env                     # Local environment variables (not committed)
```

## Database Migrations

Create a new migration after changing models:

```bash
uv run alembic revision --autogenerate -m "describe your change"
```

Apply migrations:

```bash
uv run alembic upgrade head
```

Roll back one step:

```bash
uv run alembic downgrade -1
```

## Running Tests

```bash
uv run pytest
```

## Linting & Formatting

```bash
# Check for issues
uv run ruff check .

# Auto-fix issues
uv run ruff check . --fix

# Format code
uv run ruff format .
```

## Adding a New Model

1. Create a file under `app/db/models/your_model.py`
2. Define your SQLAlchemy model inheriting from `Base`
3. Import it in `app/db/models/__init__.py` so Alembic detects it
4. Generate and apply the migration:

```bash
uv run alembic revision --autogenerate -m "add your_model"
uv run alembic upgrade head
```

## Environment Variables Reference

Create a `.env` file in the project root. Never commit this file.

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/mydb
REDIS_URL=redis://localhost:6379
```

For Alembic (sync driver required), the `env.py` automatically strips the `+asyncpg` suffix — no extra config needed.

## Contributing

1. Fork the repo and create a branch: `git checkout -b feat/your-feature`
2. Make your changes and run lint + tests before committing
3. Open a pull request with a clear description

## License

MIT
