from django.contrib import admin
from .models import *

# Register your models here.

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'vegetariano')
    search_fields = ('nombre',) 

admin.site.register(Pizza)
admin.site.register(Masas)
admin.site.register(Ingrediente)
admin.site.register(Pedido)
admin.site.register(DatosCliente)
admin.site.register(Bebida)
admin.site.register(Entrante)
admin.site.register(PizzaATuGusto)
admin.site.register(Reserva)