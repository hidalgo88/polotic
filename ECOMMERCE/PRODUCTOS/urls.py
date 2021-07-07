from django.urls import path
# from django.contrib import admin
from django.urls.conf import include
from . import views
# from .views import buscar

urlpatterns = [
    # path('', views.index, name="index"),
    path('home/', views.home, name="home"),

    path('verProducto/<int:producto_id>/', views.verProducto, name="verProducto"),

    path('buscar/', views.buscar, name="buscar"),

    path('agregar/', views.agregar, name="agregar"),

    path('contacto/', views.contacto, name="contacto"),

    path('nosotros/', views.nosotros, name="nosotros"),

    path('eliminar/<int:producto_id>/', views.eliminar, name="eliminar"),

    path('editar/<int:producto_id>/', views.editar, name="editar"),

    path('accounts/', include('django.contrib.auth.urls')),

    path('registro/', views.registro, name="registro"),
]