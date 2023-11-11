from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='home'),
    path('entrees/',views.entree_page,name='entrees'),
    path('desserts/',views.desserts_page,name='desserts'),
    path('add_recipe/',views.add_recipe,name='add_recipe'),
    path('appetizers/',views.appetizers,name='appetizers'),
    path('recipes/<int:pk>/',views.RecipeDetailView.as_view(),name='recipe_detail'),
    path('recipes/<int:pk>/update/',views.RecipeUpdateView.as_view(),name='recipe_update'),
    path('recipes/<int:pk>/delete/',views.RecipeDeleteView.as_view(),name='recipe_delete'),
]