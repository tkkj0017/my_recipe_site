from django.db import models


class Recipe(models.Model):
    
    class Meta:
        verbose_name = "レシピ"
        verbose_name_plural = "レシピ"
        
    def __str__(self):
        return self.title
    
    title = models.CharField(verbose_name="タイトル", max_length=200)
    content = models.TextField(verbose_name="内容")
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
