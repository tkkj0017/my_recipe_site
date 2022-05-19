from django.urls import path

from recipe.views import RecipeListView, RecipeDetailView


app_name = "recipe"

urlpatterns = [
    path('', RecipeListView.as_view(), name="index"),
    path('<int:pk>', RecipeDetailView.as_view(), name="detail"),
]
