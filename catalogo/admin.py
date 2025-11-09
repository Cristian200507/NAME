from django.contrib import admin
from .models import Genero, Productora, Pelicula, Serie


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Productora)
class ProductoraAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "pais")
    search_fields = ("nombre", "pais")


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "director", "anio", "productora", "creado")
    list_filter = ("anio", "productora", "generos")
    search_fields = ("titulo", "sinopsis", "director", "productora__nombre")
    readonly_fields = ("creado",)
    filter_horizontal = ("generos",)
    list_per_page = 20


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "director", "anio", "productora", "cantidad_capitulos", "creado")
    list_filter = ("anio", "productora", "generos")
    search_fields = ("titulo", "sinopsis", "director", "productora__nombre")
    readonly_fields = ("creado",)
    filter_horizontal = ("generos",)
    list_per_page = 20
