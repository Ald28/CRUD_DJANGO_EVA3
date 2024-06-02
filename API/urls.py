from django.urls import path, include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()

router.register(r'autor', views.autorSerializer)

router.register(r'libro', views.libroSerializer)

router.register(r'usuario', views.usuarioSerializer)

router.register(r'prestamo', views.prestamoSerializer)

urlpatterns = [
    path('',include(router.urls)),
    
]