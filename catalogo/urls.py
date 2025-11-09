from rest_framework import routers
from django.urls import path, include
from .views import GeneroViewSet, ProductoraViewSet, PeliculaViewSet, SerieViewSet

router = routers.DefaultRouter()
router.register(r"generos", GeneroViewSet, basename="genero")
router.register(r"productoras", ProductoraViewSet, basename="productora")
router.register(r"peliculas", PeliculaViewSet, basename="pelicula")
router.register(r"series", SerieViewSet, basename="serie")

urlpatterns = [
    path("", include(router.urls)),
]
