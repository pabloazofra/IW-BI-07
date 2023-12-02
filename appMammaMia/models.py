from django.db import models

class Masa(models.Model):
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
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    descripcion = models.TextField()
    imagen = models.ImageField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    calorias = models.IntegerField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=9)

    def __str__(self):
        return self.nombre

class PizzaATuGusto(models.Model):
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    ingrediente = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre
    
class Entrante(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre
    
class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    pizza = models.ManyToManyField(Pizza, blank=True)
    pizzaATuGusto = models.ManyToManyField(PizzaATuGusto, blank=True)
    entrantes = models.ManyToManyField(Entrante, blank=True)
    bebidas = models.ManyToManyField(Bebida, blank=True)

    def __str__(self):
        return f"Pedido {self.id}"
