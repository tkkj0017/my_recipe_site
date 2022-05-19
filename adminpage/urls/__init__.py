from django.urls import path, include
from ..views import AdminpageTemplateView

app_name = "staffroom"

urlpatterns = [
    path("", AdminpageTemplateView.as_view(), name="index"),
    path("recipe/", include("adminpage.urls.recipe", namespace="recipe")),

]
