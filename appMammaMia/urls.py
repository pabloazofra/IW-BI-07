from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('menu/', views.menu, name='menu'),
 path('masas/', views.masas, name='masas'),
 path('ingredientes/', views.ingredientes, name='ingredientes'),
 path('pizzas/', views.pizzas, name='pizzas'),
 path('reservas/', views.reservas, name='reservas'),
 path('contacto/', views.contacto, name='contacto'),
]