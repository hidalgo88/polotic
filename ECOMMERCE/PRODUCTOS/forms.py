from django import forms
from django.forms import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen']
        # widgets = {
        #     'nombre': forms.TextInput(
        #         attrs={
        #             'class' : 'form-control',
        #             'type' : 'text',
        #             'id' : 'floatingInput',
        #             'placeholder' : 'nombre',
        #             }
        #     ),
        #     'descripcion': forms.TextInput(
        #         attrs={
        #             'class' : 'form-control',
        #             'type' : 'text',
        #             'id' : 'floatingInput',
        #             'placeholder' : 'descripcion',
        #             }
        #     ),
        #     'precio': forms.TextInput(
        #         attrs={
        #             'class' : 'form-control',
        #             'type' : 'number',
        #             'id' : 'floatingInput',
        #             'placeholder' : 'precio',
        #             }
        #     ),
        #     'categoria': forms.TextInput(
        #         attrs={
        #             'class' : 'form-control',
        #             'type' : 'text',
        #             'id' : 'floatingInput',
        #             'placeholder' : 'categoria',
        #             }
        #     ),
        # }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']