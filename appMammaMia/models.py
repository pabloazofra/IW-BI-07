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
    imagen = models.ImageField()

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
    nombre_persona = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=9)
