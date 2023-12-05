from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.detalles_pizza, name='detalles_pizza'),
    path('ingredientes/', views.ingredientes, name='ingredientes'),
    path('ingredientes/<int:ingrediente_id>/', views.detalles_ingrediente, name='detalles_ingrediente'),
    path('reservas/', views.reservas, name='reservas'),
    path('contacto/', views.contacto, name='contacto'),
    path('pedido/', views.pedido, name='pedido'),
    path('guardar_datos_cliente/', views.guardar_datos_cliente, name='guardar_datos_cliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('masas/', views.masas, name='masas'),
    path('masas/<int:nombre>/', views.detalles_masa, name='detalles_masa'),
]