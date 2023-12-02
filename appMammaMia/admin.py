from django.contrib import admin
from .models import Ingrediente

# Register your models here.

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'vegetariano')
    search_fields = ('nombre',) 