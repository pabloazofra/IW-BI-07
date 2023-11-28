from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView
from .models import Masa, Ingrediente, Pizza
from django.http import HttpResponse
from datetime import datetime

##AÑADIR MAS COSAS A LOS DETALLES DE CADA COSA

def index(request):
    year = datetime.now().year
    return render(request, "index.html", {'year': year})

#devuelve listado de pizzas
def pizzas(request):
    pizzas = get_list_or_404(Pizza.objects.all())
    context = {'lista_pizzas': pizzas }
    return render(request, 'pizzas.html', context)

#devuelve detalles de cada pizza
def detalles_pizza(request):
	pizza = get_object_or_404(Pizza)
	context = {'pizza': pizza }
	return render(request, 'detalles_pizza.html', context)

#devuelve listado de masas
def masas(request):
    masas = get_list_or_404(Masa.objects.all()) ##para la base de datos
    context = {'lista_masas': masas }
    return render(request, 'masas.html', context)

#devuelve detalles de cada masa
def detalles_masa(request):
	masa = get_object_or_404(Masa)
	context = {'masa': masa }
	return render(request, 'detalles_masa.html', context)

#devuelve listado de ingredientes
def ingredientes(request):
    ingredientes = get_list_or_404(Ingrediente.objects.all())
    context = {'lista_ingredientes': ingredientes }
    return render(request, 'ingredientes.html', context)

#devuelve detalles de cada ingrediente
def detalles_ingrediente(request):
	ingrediente = get_object_or_404(Ingrediente)
	context = {'ingrediente': ingrediente }
	return render(request, 'detalles_ingre.html', context)

#devuelve el menu
def menu(request):
    return render(request, 'menu.html') #podemos añadir mas productos que pizzas

#hacer reservas (?)
def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas.html')

#contactar
def contacto(request):
    return render(request, 'contacto.html')
