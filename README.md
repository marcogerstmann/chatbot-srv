# Chatbot Service

## Initialize project

```bash
poetry install --no-root
```

## Configure project

Add all variables to a `.env` file in UPPERCASE that are present as variables in `settings.py`.

## Run project

```bash
uvicorn app.main:app --reload
```
