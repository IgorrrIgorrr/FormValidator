FROM python:3.10-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-dev

COPY . /app

CMD ["poetry", "run", "uvicorn", "formvalidator.main:app", "--host", "0.0.0.0", "--port", "8000"]
