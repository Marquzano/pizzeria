"""Defines url patterns for pizzas."""

from django.urls import path

from . import views

urlpatterns =  [
    path('', views.index, name='index')
]