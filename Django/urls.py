"""
URL configuration for Django project.
"""

from django.contrib import admin
from django.urls import path

from example import views


urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),
    path("index/<int:id>", views.people_index),
    path("access/<int:age>", views.access),
    path("admin/", admin.site.urls),
]
