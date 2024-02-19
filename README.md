# Chatbot Service

## Get started

### 1. Install dependencies with poetry

```sh
poetry install --no-root
```

### 2. Configure environment variables

Add all variables to a `.env` file in UPPERCASE that are present as variables in `config.py`.

### 3. Spin up dockerized services

```sh
docker-compose up -d
```

### 4. Run database migrations

```sh
alembic upgrade head
```

### 5. Run app

```sh
uvicorn app.main:app --reload
```

## Add new database migration

1. Create a revision file in `./alembic/versions` by running `alembic revision --autogenerate -m "add customer table"`
2. Apply all versions that are not yet applied to the database by running `alembic upgrade head`
