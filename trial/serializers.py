from rest_framework import serializers
from .models import Ingredient
from .models import Recipe
from .models import Restaurant

#creazione dei serializer per la conversione in json
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "name", "ingredients"]

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "recipes"]