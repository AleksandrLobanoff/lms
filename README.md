# Проект LMS-системы

Проект LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.

## Docker:

**Для создания Docker-image:**


docker build -t name image


**Запуск контейнера:**


docker run name image


#### Запуск через Docker Compose

`docker-compose up -d --build`


Для остановки:

`docker-compose down`


## Проект содержит два приложения:

### LMS:

Курсы, Уроки, Платежи

### Users:

Пользователи

(Обязательные поля для профиля пользователя - "email" и "password")
