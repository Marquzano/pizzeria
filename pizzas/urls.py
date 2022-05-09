"""Defines url patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns =  [
    # home page
    path('', views.index, name='index'),
    # pizzas page
    path('pizzas/', views.pizzas, name='pizzas'),
    # pizza page
    path('pizzas/(?P<pizza_id>\d+)/', views.pizza, name='pizza'),
]