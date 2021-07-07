from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Producto, Categoria
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    productos = Producto.objects.all().order_by('-id')
    categorias = Categoria.objects.all()
    context = {'productos': productos, 'categorias': categorias}
    return render(request, "home/index.html", context)


def contacto(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, "home/contacto.html", context)


def nosotros(request):
    return render(request, "home/nosotros.html")


@permission_required('app.add_producto')
def agregar(request):    
    if request.method == "POST":
        form = ProductoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    
    categorias = Categoria.objects.all()
    context = {'form' : form, 'categorias': categorias}
    return render(request, 'home/agregar.html', context)

@permission_required('app.delete_producto')
def eliminar(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    producto.delete()
    return redirect('home')

@permission_required('app.change_producto')
def editar(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm(instance=producto)

    categorias = Categoria.objects.all()
    context = {'form' : form, 'categorias': categorias}
    return render(request, 'home/editar.html', context)

def buscar(request):
    if request.method == "GET":
        busqueda = request.GET.get('buscar')
        productos = Producto.objects.filter(
            nombre__icontains = busqueda
        )
        categorias = Categoria.objects.all()
        return render(request, 'home/buscar.html', {'busqueda' : busqueda, 'productos' : productos, 
        'categorias': categorias})    
    else:
        return render(request, 'home/buscar.html', {})

def verProducto(request, producto_id):
    verProducto = Producto.objects.get(id=producto_id)    
    categorias = Categoria.objects.all()    
    return render(request, 'home/verProducto.html', {
        'producto' : verProducto,
        'categorias': categorias,
    })

def registro(request):
    context = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect(to='home')            
        categorias = Categoria.objects.all()
        context = {'form' : formulario, 'categorias': categorias}
    return render(request, 'registration/registro.html', context)