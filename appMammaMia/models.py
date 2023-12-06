from django.db import models
from django.utils import timezone


class Masas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    vegetariano = models.BooleanField(default=False)
    alergenos = models.TextField()
    imagen = models.ImageField(upload_to='ingredientes/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    masa = models.ForeignKey(Masas, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='pizzas/')
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    calorias = models.IntegerField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=9)
    comensales = models.IntegerField(max_length = 2, default=1)
    mesas = models.IntegerField(max_length = 2, default=1)
    fecha_y_hora = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nombre

class PizzaATuGusto(models.Model):
    masa = models.ForeignKey(Masas, on_delete=models.CASCADE, blank=True, null=True)
    ingrediente = models.ManyToManyField(Ingrediente, blank=True, null=True)

    def __str__(self):
        return self.masa
    
class Entrante(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='entrantes/')

    def __str__(self):
        return self.nombre
    
class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre

    
class DatosCliente(models.Model):
    nombreCliente = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=50)
    direccion = models.TextField()
    telefono = models.IntegerField(max_length=9)
    

    def __str__(self):
        return "{}".format(self.nombreCliente)

class Pedido(models.Model):
    cliente = models.ForeignKey(DatosCliente, on_delete=models.CASCADE)
    pizza = models.ManyToManyField(Pizza, blank=True)
    pizzaATuGusto = models.ManyToManyField(PizzaATuGusto, blank=True, null=True)
    entrantes = models.ManyToManyField(Entrante, blank=True)
    bebidas = models.ManyToManyField(Bebida, blank=True)
    comentario = models.TextField()

    def __str__(self):
        return f"Pedido {self.id}"