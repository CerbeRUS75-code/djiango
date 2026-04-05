"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example import views

urlpatterns = [
    path("", views.index, name="home"),
    path(
        "about",
        views.about,
        kwargs={"user": "User", "email": "user@user.ru"},
        name="about",
    ),
    path("contact", views.contact, name="contact"),
    path(
        "user1",
        views.user1,
        kwargs={"login": "admin", "email": "admin@mail.ru"},
        name="user1",
    ),
    path(
        "user2",
        views.user2,
        kwargs={"login": "guest", "email": "guest@mail.ru"},
        name="user2",
    ),
    path('admin/', admin.site.urls),
]
