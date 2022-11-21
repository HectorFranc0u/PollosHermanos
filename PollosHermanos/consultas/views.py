from django.shortcuts import render, redirect
from django.utils import timezone
from datos import models
from django.contrib.auth.models import User
from .form import ProductosForm, ProveedorForm
# Create your views here.

def consultas(req):
    consultaprod = models.tbProductos.objects.all()
    consutlaprov = models.tbProveedores.objects.all()
    return render(req, 'consultas.html', {"consultaprod":consultaprod}, {"consultaprov":consutlaprov})

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
    
