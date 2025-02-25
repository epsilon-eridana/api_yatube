# Проект API для Yatube

## Описание

API для Yatube предоставляет программный интерфейс для взаимодействия с социальной сетью Yatube, где пользователи могут публиковать посты, комментировать их и подписываться на других авторов.

## Технологии

- Python 3
- Django 3
- Django REST Framework

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/epsilon-eridana/api_yatube.git
   cd api_yatube
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции:

   ```bash
   python manage.py migrate
   ```

5. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

## Документация API

После запуска сервера, документация API доступна по адресу: `http://127.0.0.1:8000/redoc/`.

## Тестирование

Для запуска тестов используйте команду:

   ```bash
   pytest
   ```

## Автор

- [epsilon-eridana](https://github.com/epsilon-eridana)
