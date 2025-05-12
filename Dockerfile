FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock README.md /app/

RUN pip install --upgrade pip && pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi


COPY . /app/

EXPOSE 8000

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]