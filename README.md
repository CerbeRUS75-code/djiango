# Django Учебный Проект (lesson-4)

## Запуск

```powershell
cd C:\django
C:\django\Python312\python.exe manage.py runserver 127.0.0.1:8000
```

## Проверка страниц

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/about/
- http://127.0.0.1:8000/contacts/

## Что проверять

- Главная `/`:
  - приветствие по времени суток (`Доброе утро/день/вечер`)
  - вывод переменных `{{ title }}`, `{{ message }}`
  - цикл `{% for %}` по списку языков
  - тег времени `{% now %}`
- About `/about/`:
  - разница между обычным выводом `{{ body }}` и блоком `{% autoescape off %}`
- Contacts `/contacts/`:
  - условие `{% if / elif / else %}` для `n = -5`

## Файлы

- `example/views.py`
- `Django/urls.py`
- `example/templates/index.html`
- `example/templates/about.html`
- `example/templates/contacts.html`
