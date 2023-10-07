FROM python:3

WORKDIR /app

COPY ./pyproject.toml .

RUN poetry install --no-dev

COPY . .

CMD ["python", "manage.py", "runserver"]