from django.views.generic import  TemplateView

from recipe.models import Recipe


class IndexTemplateView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)

        try:
            context['recipe_top'] = Recipe.objects.order_by('?')[0]
        except IndexError:
            context['recipe_top'] = None
            
        context['recipe_list'] = Recipe.objects.order_by("-created")
        
        return context
