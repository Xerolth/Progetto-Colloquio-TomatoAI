from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ingredient
from .models import Recipe
from .models import Restaurant
from .serializers import IngredientSerializer
from .serializers import RecipeSerializer
from .serializers import RestaurantSerializer

# Create your views here.

#viste per creazione
class IngredientListCreate(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

#viste per aggiornamento ed eliminazione
class IngredientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = "pk"

class RecipeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = "pk"

class RestaurantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "pk"