from django.shortcuts import render


def index(request):
    tech_stack = ["Python", "Django", "PostgreSQL", "Docker"]
    return render(
        request,
        "index.html",
        context={
            "title": "Сайт-визитка | Главная",
            "header": "Python Django Разработчик",
            "tech_stack": tech_stack,
        },
    )


def about(request):
    facts = [
        "Создаю backend-сервисы на Django",
        "Проектирую REST API и работу с БД",
        "Пишу чистый и поддерживаемый код",
    ]
    return render(
        request,
        "about.html",
        context={
            "title": "Сайт-визитка | Обо мне",
            "header": "Обо мне",
            "facts": facts,
        },
    )


def projects(request):
    cards = [
        {"name": "Task Manager", "desc": "Сервис управления задачами для команды"},
        {"name": "Shop API", "desc": "API для каталога товаров и заказов"},
        {"name": "Study Tracker", "desc": "Приложение для трекинга обучения"},
    ]
    return render(
        request,
        "projects.html",
        context={
            "title": "Сайт-визитка | Проекты",
            "header": "Мои проекты",
            "cards": cards,
        },
    )


def contacts(request):
    return render(
        request,
        "contacts.html",
        context={
            "title": "Сайт-визитка | Контакты",
            "header": "Контакты",
            "email": "admin@admin.com",
            "phone": "+7 (900) 000-00-00",
            "city": "Чита",
        },
    )
