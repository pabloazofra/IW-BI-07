from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView
from .models import Masas, Ingrediente, Pizza, Reserva, Pedido, Bebida, Entrante, DatosCliente
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime

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
def detalles_masa(request, masa_id):
    masa = get_object_or_404(Masas, pk=masa_id)
    pizzas_asociadas = Pizza.objects.filter(tipo_masa=masa)
    return render(request, 'detalles_masa.html', {'masa': masa, 'pizzas_asociadas': pizzas_asociadas})

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


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Pedido, DatosCliente

def guardar_datos_cliente(request):
    try:
        if request.method == 'POST':
        # Obtener datos del formulario
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            direccion = request.POST.get('direccion')
            telefono = request.POST.get('telefono')
            
            pizza = request.POST.getlist('pizza')
            masa = request.POST.get('masa')
            ingrediente = request.POST.getlist('ingrediente')
            pizzaATuGusto = pizzaATuGusto.objects.create(masa=masa, ingrediente=ingrediente)
            entrantes = request.POST.getlist('entrantes')
            bebidas = request.POST.getlist('bebidas')
            comentario = request.POST.get('bebidas')

            # Crear un nuevo objeto DatosCliente y guardarlo en la base de datos
            nuevo_cliente = DatosCliente.objects.create(
                nombre_cliente=nombre,
                apellidos=apellidos,
                direccion=direccion,
                telefono=telefono,
            )
            DatosCliente.objects.create(cliente=nuevo_cliente)

            nuevo_pedido = Pedido.objects.create(
                cliente=nuevo_cliente,
                pizza=pizza,
                pizzaATuGusto=pizzaATuGusto,
                entrantes=entrantes,
                bebidas=bebidas,
                comentario=comentario
            )
            #
            



            return JsonResponse({'mensaje': 'Pedido y datos de cliente guardados correctamente'})
        else:
            # Si la solicitud no es POST, redireccionar a la página del pedido
            return redirect('pedido')

    except Exception as e:
        import traceback
        print(traceback.format_exc())
