"""operation URL Configuration
"""
from django.contrib import admin
from django.urls import path

from .views import AdditionView


urlpatterns = [
    path('add', AdditionView.as_view(), name='addition'),
]
