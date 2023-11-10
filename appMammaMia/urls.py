from django.urls import path
from . import views
from .views import masas, ingredientes, pizzas, menu

urlpatterns = [
 path('', views.index, name='index'),
 path('menu/', menu, name='menu'),
 path('masas/', masas, name='masas'),
 path('ingredientes/', ingredientes, name='ingredientes'),
 path('pizzas/', pizzas, name='pizzas')
]