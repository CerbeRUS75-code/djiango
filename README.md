# Django Учебный Проект (lesson-6)

## Запуск

```powershell
cd C:\django
C:\django\Python312\python.exe manage.py runserver 127.0.0.1:8000
```

## Проверка

Открой одну страницу:
- http://127.0.0.1:8000/

На странице есть 3 формы:
1. Обычная HTML-форма
2. Django Form (`forms.Form`) + вывод `as_table/as_ul/as_p/as_div`
3. Сложная форма с разными типами полей

После отправки любой формы сверху показывается результат обработки.
