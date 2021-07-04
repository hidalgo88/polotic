from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('agregar/', views.agregar, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar, name="eliminar"),
]