# Проект Learning_system

REST API для Проекта Learning_system личный кабинет для изучения курсов студентам.
У авторизированного пользователя есть доступ к своему личному кабинету

## Стек технологий:

* [Python 3.10.6](https://www.python.org/downloads/)
* [Django 4.2.5](https://www.djangoproject.com/download/)
* [Django Rest Framework 3.14](https://pypi.org/project/djangorestframework/#files)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Olga-koml/learining_system.git
```

```
cd learining_system
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


## Документация для YaMDb доступна по адресу:

```http://127.0.0.1:8000/swagger/```

## Автор:

[Комлева Ольга](https://github.com/Olga-koml)