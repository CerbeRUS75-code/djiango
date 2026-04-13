"""
URL configuration for Django project.
"""

from django.contrib import admin
from django.urls import path

from example import views


urlpatterns = [
    path("", views.forms_page),
    path("admin/", admin.site.urls),
]
