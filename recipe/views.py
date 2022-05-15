from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"
