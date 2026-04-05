"""
URL configuration for Django project.
"""

from django.contrib import admin
from django.urls import include, path

from example import views


product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]


urlpatterns = [
    path("", views.index),
    path("request/", views.request_info),
    path("user/", views.user),
    path("user/<str:name>/", views.user),
    path("user/<str:name>/<int:code>/", views.user),
    path("products/<int:id>/", include(product_patterns)),
    path("admin/", admin.site.urls),
]
