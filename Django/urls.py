"""
URL configuration for Django project.
"""

from django.contrib import admin
from django.urls import path

from example import views


urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("projects/", views.projects),
    path("contacts/", views.contacts),
    path("admin/", admin.site.urls),
]
