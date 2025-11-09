from rest_framework import serializers
from .models import Genero, Productora, Pelicula, Serie


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ["id", "nombre"]


class ProductoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productora
        fields = ["id", "nombre", "pais"]


class PeliculaSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True, read_only=True)
    generos_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Genero.objects.all(),
        source="generos"
    )
    productora = ProductoraSerializer(read_only=True)
    productora_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="productora",
        queryset=Productora.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Pelicula
        fields = [
            "id",
            "titulo",
            "sinopsis",
            "director",
            "anio",
            "generos",
            "generos_ids",
            "productora",
            "productora_id",
            "portada",
            "creado",
        ]


class SerieSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True, read_only=True)
    generos_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Genero.objects.all(),
        source="generos"
    )
    productora = ProductoraSerializer(read_only=True)
    productora_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="productora",
        queryset=Productora.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Serie
        fields = [
            "id",
            "titulo",
            "sinopsis",
            "director",
            "anio",
            "generos",
            "generos_ids",
            "productora",
            "productora_id",
            "portada",
            "cantidad_capitulos",
            "creado",
        ]
