from django.shortcuts import render, redirect
from django.utils import timezone
from datos import models
from django.contrib.auth.models import User
from .form import ProductosForm, ProveedorForm, SucursalesForm, CombosForm
# Create your views here.

def consultas(req):
    consultaprod = models.tbProductos.objects.all()
    consutlaprov = models.tbProveedores.objects.all()
    consultacombos = models.tbCombos.objects.all()
    consultasucursales = models.tbSucursales.objects.all()

    return render(req, 'consultas.html', {"consultaprov":consutlaprov, "consultaprod":consultaprod, 
                    "consultacombos" : consultacombos, "consultasucursales" : consultasucursales})

# metodos para agregar registros a las tablas
def agregarProv(req):
    if req.method == "POST":
        form = ProveedorForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ProveedorForm()
    
    context = {'form' : form}
    return render(req, 'agregarProv.html', context)

def agregarProd(req):
    if req.method == "POST":
        form = ProductosForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ProductosForm()
    
    context = {'form' : form}
    return render(req, 'agregarProd.html', context)

def agregarSuc(req):
    if req.method == "POST":
        form = SucursalesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = SucursalesForm()
    
    context = {'form' : form}
    return render(req, 'agregarSuc.html', context)

def agregarComb(req):
    if req.method == "POST":
        form = CombosForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = CombosForm()

    context = {'form' : form}
    return render(req, 'agregarComb.html', context)

# metodos para eliminar registros de las tablas
def eliminarProv(req, tbProveedores_id):
    borrar = models.tbProveedores.objects.get(id=tbProveedores_id)
    borrar.delete()
    return redirect('consultas')

def eliminarProd(req, tbProductos_id):
    borrar = models.tbProductos.objects.get(id=tbProductos_id)
    borrar.delete()
    return redirect('consultas')

def eliminarSuc(req, tbSucursales_id):
    borrar = models.tbSucursales.objects.get(id=tbSucursales_id)
    borrar.delete()
    return redirect('consultas')

def eliminarComb(req, tbCombos_id):
    borrar = models.tbCombos.objects.get(id=tbCombos_id)
    borrar.delete()
    return redirect('consultas')

# metodos para editar registros de las tablas
def editarProv(req, tbProveedores_id):
    editar = models.tbProveedores.objects.get(id=tbProveedores_id)
    if req.method == "POST":
        form = ProveedorForm(req.POST, instance=editar)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ProveedorForm(instance=editar)

    context = {"form" : form }
    return render(req, "editarProv.html", context)

def editarProd(req, tbProductos_id):
    editar = models.tbProductos.objects.get(id=tbProductos_id)
    if req.method == "POST":
        form = ProductosForm(req.POST, instance=editar)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ProductosForm(instance=editar)

    context = {"form" : form }
    return render(req, "editarProd.html", context)

def editarSuc(req, tbSucursales_id):
    editar = models.tbSucursales.objects.get(id=tbSucursales_id)
    if req.method == "POST":
        form = SucursalesForm(req.POST, instance=editar)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = SucursalesForm(instance=editar)

    context = {"form" : form }
    return render(req, "editarSuc.html", context)

def editarComb(req, tbCombos_id):
    editar = models.tbCombos.objects.get(id=tbCombos_id)
    if req.method == "POST":
        form = CombosForm(req.POST, instance=editar)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = CombosForm(instance=editar)

    context = {"form" : form }
    return render(req, "editarComb.html", context)
