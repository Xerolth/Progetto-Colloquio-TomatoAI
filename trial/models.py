from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    recipes = models.ManyToManyField(Recipe)