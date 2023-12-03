from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView
from .models import TipoMasa, Ingrediente, Pizza, Reserva, Pedido, Bebida, Entrante, DatosCliente
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
def lista_masas(request):
    tipos_de_masa = TipoMasa.objects.all()
    return render(request, 'masas.html', {'tipos_de_masa': tipos_de_masa})

#devuelve detalles de cada masa
def detalles_masa(request, masa_id):
    masa = get_object_or_404(TipoMasa, pk=masa_id)
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
    masas = get_list_or_404(Masa)
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


def guardar_datos_cliente(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        comentario = request.POST.get('comentario')
        pedido = request.POST.get('pedido')

        # Crear un nuevo objeto DatosCliente y guardarlo en la base de datos
        nuevo_cliente = DatosCliente.objects.create(
            nombre=nombre,
            apellidos=apellidos,
            direccion=direccion,
            telefono=telefono,
            comentario=comentario, 
            pedido=pedido
        )

        # Obtener productos seleccionados del formulario y agregarlos al pedido
        productos_seleccionados = request.POST.getlist('productos_checkbox')
        nuevo_pedido = Pedido.objects.create(cliente=nuevo_cliente)

        for producto in productos_seleccionados:
            # Lógica para agregar cada producto al pedido
            # Puedes obtener el producto por su nombre o algún identificador
            # Ejemplo: producto_obj = Producto.objects.get(nombre=producto)
            # Ejemplo de cómo agregar un producto al pedido:
            # nuevo_pedido.productos.add(producto_obj)
            pass

        return JsonResponse({'mensaje': 'Pedido y datos de cliente guardados correctamente'})
    else:
        # Si la solicitud no es POST, redireccionar a la página del pedido
        return redirect('pedido')