# Конспект по ORM Django

## Базовые операции

- `Book.objects.create(...)` - создать и сразу сохранить объект.
- `Book.objects.all()` - получить все записи.
- `Book.objects.filter(...)` - выбрать записи по условию.
- `Book.objects.exclude(...)` - исключить записи по условию.
- `Book.objects.get(...)` - получить один объект (или ошибка).
- `Book.objects.order_by("title")` / `order_by("-published_year")` - сортировка.
- `Book.objects.count()` - количество записей.
- `Book.objects.filter(...).exists()` - проверить наличие записей.

## Изменение данных

- `obj.field = value; obj.save()` - обновить объект.
- `Book.objects.filter(...).update(...)` - массовое обновление SQL-запросом.
- `Book.objects.filter(...).delete()` - удаление записей.

## Удобные методы

- `get_or_create(...)` - получить или создать объект.
- `update_or_create(...)` - обновить или создать объект.

## Связи

- `ForeignKey` реализует связь many-to-one.
- `Book.objects.select_related("author")` - подтягивает автора в том же SQL-запросе (JOIN).

## Примеры из этой работы

```python
from example.models import Book, Author

books = Book.objects.select_related("author").all()

obj, created = Author.objects.get_or_create(
    name="Лев Толстой",
    defaults={"birth_year": 1828},
)

Book.objects.filter(title="Колобок").update(price=120)
```
