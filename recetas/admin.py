from django.contrib import admin
from .models import Categoria, Receta


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}


# admin.py
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "autor", "creada_en")
    list_filter = ("categoria", "autor")
    search_fields = ("titulo", "descripcion", "ingredientes", "pasos", "autor__username")
