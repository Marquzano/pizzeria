from django.shortcuts import render

from .models import Pizzas, Topping

# Create your views here.
def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas on our menu."""
    pizzas = Pizzas.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show the toppings for our pizza."""
    pizza = Pizzas.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, "pizzas/pizza.html", context)
    # toppings is being sent but the html page seems
    # to say that toppings is an empty string list
    # need to figure this out