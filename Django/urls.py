"""
URL configuration for Django project.
"""

from django.contrib import admin
from django.urls import path

from example import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_book, name="add_book"),
    path("add-author/", views.add_author, name="add_author"),
    path("admin/", admin.site.urls),
]
