from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre_categoria
        
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=64)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria")
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre