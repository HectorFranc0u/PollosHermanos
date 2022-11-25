from django.shortcuts import render, redirect
from django.utils import timezone
from datos import models
from django.contrib.auth.models import User
from .form import ProductosForm, ProveedorForm
# Create your views here.

def consultas(req):
    consultaprod = models.tbProductos.objects.all()
    consutlaprov = models.tbProveedores.objects.all()
    return render(req, 'consultas.html', {"consultaprov":consutlaprov, "consultaprod":consultaprod})

def agregar(req):
    if req.method == "POST":
        form = ProveedorForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ProveedorForm()
    
    context = {'form' : form}
    return render(req, 'agregar.html', context)

def eliminar(req, tbProveedores_id):
    borrar = models.tbProveedores.objects.get(id=tbProveedores_id)
    borrar.delete()
    return redirect('consultas')

def editar(req, tbProveedores_id):
    editar = models.tbProveedores.objects.get(id=tbProveedores_id)
    if req.method == "POST":
        form = ProveedorForm(req.POST, instance=editar)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ProveedorForm(instance=editar)

    context = {"form" : form }
    return render(req, "editar.html", context)
