from django.urls import path
#. indica la directory in cui è presente questo file
from . import views

urlpatterns = [
    # url per la creazione
    path("ingredients/", views.IngredientList.as_view(), name="ingredient-view"),
    path("recipes/", views.RecipeListCreate.as_view(), name="recipe-view-create"),
    path("restaurants/", views.RestaurantListCreate.as_view(), name="restaurant-view-create"),
    # url per aggiornamento e distruzione
    path("ingredients/<int:pk>", views.IngredientRetrieveUpdateDestroy.as_view(), name="ingredient-update"),
    path("recipes/<int:pk>", views.RecipeRetrieveUpdateDestroy.as_view(), name="recipe-update"),
    path("restaurants/<int:pk>", views.RestaurantRetrieveUpdateDestroy.as_view(), name="restaurant-update")
]