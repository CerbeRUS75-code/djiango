# Перенос проекта на другой компьютер без потери данных

## Вариант 1 (SQLite, самый простой)

1. На исходном компьютере:

```bash
python -m pip freeze > requirements.txt
```

2. Скопировать:
- весь проект,
- `db.sqlite3`,
- `requirements.txt`.

3. На новом компьютере:

```bash
python -m pip install -r requirements.txt
python manage.py runserver
```

## Вариант 2 (через dumpdata/loaddata)

1. На исходном компьютере:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py dumpdata example --indent 2 > example_data.json
python -m pip freeze > requirements.txt
```

2. На новом компьютере:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata example_data.json
python manage.py runserver
```

Проверка: открыть главную страницу и убедиться, что книги и авторы на месте.
