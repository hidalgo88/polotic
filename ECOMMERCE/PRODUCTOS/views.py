from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, "home/index.html", context)

def agregar(request):    
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProductoForm()

    context = {'form' : form}
    return render(request, 'home/agregar.html', context)