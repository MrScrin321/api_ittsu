# api_student_points

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание

API для сервиса, который позволяет узнать суммарное количество баллов студента за мероприятия.

## Как запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:

   ```
   git clone https://github.com/valtocom/api_student_points.git
   ```

   ```
   cd student_points/
   ```

2. Cоздать и активировать виртуальное окружение:

   ```
   python -m venv venv
   ```

   ```
   # для OS Lunix и MacOS
   source venv/bin/activate

   # для OS Windows
   source venv/Scripts/activate
   ```

   ```
   python -m pip install --upgrade pip
   ```

3. Установить зависимости из файла requirements.txt:

   ```
   pip install -r requirements.txt
   ```

4. Выполнить миграции:

   ```
   python manage.py migrate
   ```

5. Запустить проект:

   ```
   python manage.py runserver
   ```

## Ресурсы

- Postman
https://www.postman.com/
