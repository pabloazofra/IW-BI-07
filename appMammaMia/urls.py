from django.urls import path
from . import views
from .views import masas, ingredientes, pizzas, menu

urlpatterns = [
     path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.detalles_pizza, name='detalles_pizza'),
    path('masas/', views.masas, name='masas'),
    path('masas/<int:masa_id>/', views.detalles_masa, name='detalles_masa'),
    path('ingredientes/', views.ingredientes, name='ingredientes'),
    path('ingredientes/<int:ingrediente_id>/', views.detalles_ingrediente, name='detalles_ingrediente'),
    path('menu/', views.menu, name='menu'),
    path('reservas/', views.reservas, name='reservas'),
    path('contacto/', views.contacto, name='contacto'),
]