from rest_framework import viewsets, filters
from django.db.models import Q

from .models import Genero, Productora, Pelicula, Serie
from .serializers import GeneroSerializer, ProductoraSerializer, PeliculaSerializer, SerieSerializer
from .filters import PeliculaFilter, SerieFilter


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["nombre"]
    ordering_fields = ["nombre"]
    ordering = ["nombre"]


class ProductoraViewSet(viewsets.ModelViewSet):
    queryset = Productora.objects.all()
    serializer_class = ProductoraSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["nombre", "pais"]
    ordering_fields = ["nombre", "pais"]
    ordering = ["nombre"]


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.prefetch_related("generos").select_related("productora").all()
    serializer_class = PeliculaSerializer
    filterset_class = PeliculaFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["titulo", "sinopsis", "director", "productora__nombre"]
    ordering_fields = ["titulo", "anio", "creado"]
    ordering = ["-creado"]


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.prefetch_related("generos").select_related("productora").all()
    serializer_class = SerieSerializer
    filterset_class = SerieFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["titulo", "sinopsis", "director", "productora__nombre"]
    ordering_fields = ["titulo", "anio", "creado"]
    ordering = ["-creado"]
