from django import forms
from datos import models

class ProductosForm(forms.ModelForm):

    class Meta:
        model = models.tbProductos
        fields = ['ProdName', 'ProdTipo', 'ProdUnidaddeMed', 'ProdNombre', 'ProdCantidad']

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = models.tbProveedores
        fields = ['ProvEmpresa', 'ProvName', 'ProvLastname', 'ProvPais', 'ProvTipoProd']