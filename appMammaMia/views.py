from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView
from .models import Masas, Ingrediente, Pizza, Reserva, Pedido, Bebida, Entrante, DatosCliente, PizzaATuGusto
from django.http import JsonResponse
from django.http import HttpResponseBadRequest, HttpResponse
from django.db import transaction
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

##AÑADIR MAS COSAS A LOS DETALLES DE CADA COSA

def index(request):
    return render(request, "index.html")

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
    tipos_de_masa = Masas.objects.all()
    return render(request, 'masas.html', {'masas': tipos_de_masa})

#devuelve detalles de cada masa
def detalles_masa(request, nombre):
    masa = get_object_or_404(Masas, id=nombre)
    pizzas_asociadas = Pizza.objects.filter(masa=masa)
    return render(request, 'detalles_masa.html', {'masa': masa, 'pizzas_asociadas': pizzas_asociadas})


#devuelve listado de ingredientes
def ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    context = {'ingredientes': ingredientes }
    return render(request, 'ingredientes.html', context)

#devuelve detalles de cada ingrediente
def detalles_ingrediente(request):
	ingrediente = get_object_or_404(Ingrediente)
	context = {'ingrediente': ingrediente }
	return render(request, 'detalles_ingre.html', context)

#hacer reservas (?)
def reservas(request):
    reserva = get_object_or_404(Reserva)
    context = {'reserva': reserva }
    return render(request, 'reservas.html', context)

#contactar
def contacto(request):
    return render(request, 'contacto.html')

def pedido(request):
    bebidas = get_list_or_404(Bebida)
    entrantes = get_list_or_404(Entrante)
    masas = Masas.objects.all()
    ingredientes = get_list_or_404(Ingrediente)
    pizzas = get_list_or_404(Pizza.objects.all())
    pedido = Pedido.objects.all()
    datosCliente = DatosCliente.objects.all()

    context = {'lista_pizzas': pizzas,
               'lista_pizzasTugusto': pedido,
               'lista_entrantes': entrantes, 
               'lista_bebidas': bebidas,
               'lista_masas': masas,
               'lista_ingredientes': ingredientes,
               'lista_clientes': datosCliente, 
               }
    return render(request, 'pedido.html', context)





@transaction.atomic  # Utiliza una transacción para garantizar la integridad de la base de datos
def guardar_datos_cliente(request):
    if request.method == 'POST':
        try:
            # Lee y decodifica los datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)
            
            # Extrae datos del diccionario
            nombre = data.get('nombreCliente')
            apellidos = data.get('apellidos')
            direccion = data.get('direccion')
            telefono = data.get('telefono')

            pizza = data.get('pizza')
            masa = data.get('masa')
            ingrediente = data.get('ingrediente')
            entrantes = data.get('entrantes')
            bebidas = data.get('bebidas')
            comentario = data.get('comentario')
            
            # Inicia una transacción para garantizar la integridad de la base de datos
            with transaction.atomic():
                # Crea un nuevo objeto DatosCliente y guárdalo en la base de datos
                nuevo_cliente = DatosCliente.objects.create(
                    nombreCliente=nombre,
                    apellidos=apellidos,
                    direccion=direccion,
                    telefono=telefono,
                )

                nueva_pizza_a_tu_gusto = PizzaATuGusto.objects.create(
                    masa=masa
                )
                nueva_pizza_a_tu_gusto.ingrediente.add(*ingrediente)

                nuevo_pedido = Pedido.objects.create(
                    cliente=nuevo_cliente,
                    comentario=comentario
                )

                # Agrega elementos a las relaciones ManyToMany
                nuevo_pedido.pizza.add(*pizza)
                nuevo_pedido.pizzaATuGusto.add(nueva_pizza_a_tu_gusto)
                nuevo_pedido.entrantes.add(*entrantes)
                nuevo_pedido.bebidas.add(*bebidas)
            
            return JsonResponse({'mensaje': 'Pedido y datos de cliente guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error en la vista: {str(e)}'}, status=500)
    else:
        # Si la solicitud no es POST, redireccionar a la página del pedido
        return redirect('pedido')
