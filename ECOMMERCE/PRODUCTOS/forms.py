from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria']
        label = {
            'nombre' : 'Feo'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'id' : 'floatingInput',
                    'placeholder' : 'nombre',
                    }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'id' : 'floatingInput',
                    'placeholder' : 'descripcion',
                    }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'number',
                    'id' : 'floatingInput',
                    'placeholder' : 'precio',
                    }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'id' : 'floatingInput',
                    'placeholder' : 'categoria',
                    }
            ),
        }