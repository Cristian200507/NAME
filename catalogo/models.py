from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

    def __str__(self):
        return self.nombre


class Productora(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Productora"
        verbose_name_plural = "Productoras"

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=300)
    sinopsis = models.TextField(blank=True)
    director = models.CharField(max_length=200, blank=True)
    anio = models.PositiveSmallIntegerField()
    generos = models.ManyToManyField(Genero, related_name="peliculas", blank=True)
    productora = models.ForeignKey(
        Productora, on_delete=models.SET_NULL, null=True, blank=True, related_name="peliculas"
    )
    portada = models.ImageField(upload_to="portadas/peliculas/", blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return self.titulo


class Serie(models.Model):
    titulo = models.CharField(max_length=300)
    sinopsis = models.TextField(blank=True)
    director = models.CharField(max_length=200, blank=True)
    anio = models.PositiveSmallIntegerField()
    generos = models.ManyToManyField(Genero, related_name="series", blank=True)
    productora = models.ForeignKey(
        Productora, on_delete=models.SET_NULL, null=True, blank=True, related_name="series"
    )
    portada = models.ImageField(upload_to="portadas/series/", blank=True, null=True)
    cantidad_capitulos = models.PositiveIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.titulo
