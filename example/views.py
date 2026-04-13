from datetime import datetime

from django.shortcuts import render


def index(request):
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Доброе утро"
    elif 12 <= hour < 18:
        greeting = "Добрый день"
    else:
        greeting = "Добрый вечер"

    langs = ["Python", "JavaScript", "PHP", "C#", "C++"]
    context = {
        "title": "Python Django",
        "message": "Главная страница",
        "greeting": greeting,
        "langs": langs,
    }
    return render(request, "index.html", context=context)


def about(request):
    context = {
        "title": "О нас",
        "body": "<h1>О нас</h1>",
    }
    return render(request, "about.html", context=context)


def contacts(request):
    return render(request, "contacts.html", context={"title": "Контакты", "n": -5})
