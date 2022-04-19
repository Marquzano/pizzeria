from django.contrib import admin
from pizzas.models import Pizzas
from pizzas.models import Topping

# Register your models here.
admin.site.register(Pizzas)
admin.site.register(Topping)