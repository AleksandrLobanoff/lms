FROM python:3

WORKDIR /app

COPY ./pyproject.toml .

RUN pip install poetry

RUN poetry install --no-dev

COPY . .

CMD ["python", "manage.py", "runserver"]
