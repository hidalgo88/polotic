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

def eliminar(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    producto.delete()
    return redirect("home")

def editar(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ProductoForm(instance=producto)

    context = {"form" : form}
    return render(request, "home/editar.html", context)