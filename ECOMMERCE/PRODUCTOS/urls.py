from django.urls import path
from . import views
from .views import buscar

urlpatterns = [
    # path('', views.index, name="index"),
    path('home/', views.home, name="home"),

    path('buscar/', views.buscar, name="buscar"),

    path('agregar/', views.agregar, name="agregar"),

    path('eliminar/<int:producto_id>/', views.eliminar, name="eliminar"),

    path('editar/<int:producto_id>/', views.editar, name="editar"),
]