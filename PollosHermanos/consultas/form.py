from django import forms
from datos import models

class ProductosForm(forms.ModelForm):

    class Meta:
        model = models.tbProductos
        fields = ['ProdName', 'ProdTipo', 'ProdUnidaddeMed', 'ProdNombre', 'ProdCantidad', 'ProdProveedor']

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = models.tbProveedores
        fields = ['ProvEmpresa', 'ProvName', 'ProvLastname', 'ProvPais', 'ProvTipoProd']

class CombosForm(forms.ModelForm):

    class Meta:
        model = models.tbCombos
        fields = ['CombName', 'CombTipo', 'ComPrecio', 'CombDescripcion', 'CombDisp', 'CombSucursal']

class SucursalesForm(forms.ModelForm):

    class Meta:
        model = models.tbSucursales
        fields = ['SucName', 'SucAddress', 'SucGerente', 'SucHorarios', 'SucCombos']