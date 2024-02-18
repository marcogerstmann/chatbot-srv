# Chatbot Service

## Get started

### 1. Install dependencies with poetry

```sh
poetry install --no-root
```

### 2. Configure environment variables

Add all variables to a `.env` file in UPPERCASE that are present as variables in `config.py`.

### 3. Run database migrations

```sh
alembic upgrade head
```

### 4. Run app

```sh
uvicorn app.main:app --reload
```

## Add new database migration

1. In `./alembic/env.py` make sure that all models are referenced in the imports (even though they will not be used in that file)
2. Create a revision file in `./alembic/versions` by running `alembic revision --autogenerate -m "add customer table"`
3. Apply all versions that are not yet applied to the database by running `alembic upgrade head`
