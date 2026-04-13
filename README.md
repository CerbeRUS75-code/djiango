# Django Учебный Проект (lesson-5)

## Запуск

```powershell
cd C:\django
C:\django\Python312\python.exe manage.py runserver 127.0.0.1:8000
```

## Проверка страниц

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/about/
- http://127.0.0.1:8000/projects/
- http://127.0.0.1:8000/contacts/

## Что реализовано

- Static-файлы: `example/static/css/style.css`, `example/static/images/*`
- Базовый шаблон: `example/templates/base.html`
- Наследование шаблонов через `{% extends "base.html" %}`
- Вложенный шаблон подвала через `{% include "footer.html" %}`
- Bootstrap (CDN) + собственный CSS
- Сайт-визитка из нескольких страниц с изображениями
