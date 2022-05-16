from django.db import models

from recipe.models import Recipe


class Comment(models.Model):

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None, null=True)
