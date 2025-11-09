import django_filters
from .models import Pelicula, Serie, Genero, Productora

class PeliculaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(field_name="titulo", lookup_expr="icontains")
    anio = django_filters.NumberFilter(field_name="anio")
    generos = django_filters.ModelMultipleChoiceFilter(field_name="generos", queryset=Genero.objects.all(), conjoined=False)
    productora = django_filters.ModelChoiceFilter(field_name="productora", queryset=Productora.objects.all())

    class Meta:
        model = Pelicula
        fields = ["titulo", "anio", "generos", "productora"]

class SerieFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(field_name="titulo", lookup_expr="icontains")
    anio = django_filters.NumberFilter(field_name="anio")
    generos = django_filters.ModelMultipleChoiceFilter(field_name="generos", queryset=Genero.objects.all(), conjoined=False)
    productora = django_filters.ModelChoiceFilter(field_name="productora", queryset=Productora.objects.all())

    class Meta:
        model = Serie
        fields = ["titulo", "anio", "generos", "productora"]
