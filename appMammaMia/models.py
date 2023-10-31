from django.db import models
 
class Pizzas(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Ingredientes(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)

class Crear(models.Model):
    MASA = (
        ('fina', 'Fina'),
        ('clasica', 'Clásica'),
        ('pan', 'Pan'),
        ('queso', 'Queso'),
        ('sin gluten', 'Sin Gluten'),
    )

    MASA = (
        ('tomate', 'Salsa de tomate'),
    )
    masa = models.CharField(max_length=50, choices=MASA)
    ingredients = models.CharField(max_length=50, choices=INGREDIENTES)
 
class Masas(models.Model):
    # Campo para la relación one-to-many (un empleado pertenece a un departamento)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (un empleado tiene varias habilidades)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    antiguedad = models.IntegerField(default=0)
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.       	