# urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'autores', views.AutorViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
