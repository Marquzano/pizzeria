from django.db import models

# Create your models here.

class Pizzas(models.Model):
    """A pizza that we can make"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'pizzas'

    def __str__(self):
        """Return the name of the pizza"""
        return self.name

class Topping(models.Model):
    """Topping for a pizza"""
    name = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizzas, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name