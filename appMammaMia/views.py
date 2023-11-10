from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Masa, Ingrediente, Pizza
from django.http import HttpResponse
from datetime import datetime


def index(request):
    year = datetime.now().year
    return render(request, "index.html", {'year': year})
def masas(request):
    masas = Masa.objects.all()
    return render(request, 'masas.html', {'masas': masas})

def ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingredientes.html', {'ingredientes': ingredientes})

def pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzas.html', {'pizzas': pizzas})

def menu(request):
    return render(request, 'menu.html')