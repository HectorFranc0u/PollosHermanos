from django.db import models

# Create your models here.
class tbSucursales(models.Model):
    SucName = models.CharField(max_length=200, null=True)
    SucAddress = models.TextField()
    SucGerente = models.CharField(max_length=200)
    SucHorarios = models.CharField(max_length=200)
    SucCombos = models.CharField(max_length=200)

    def __str__(self):
        return str(self.SucName)


class tbCombos(models.Model):
    CombName = models.CharField(max_length=200, null=True)
    CombTipo = models.CharField(max_length=200, null=True)
    ComPrecio = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    CombDescripcion = models.CharField(max_length=200)
    CombDisp = models.BooleanField(null=True)
    CombSucursal = models.ForeignKey(tbSucursales, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.CombName)

class tbProveedores(models.Model):
    ProvEmpresa = models.CharField(max_length=200)
    ProvName = models.CharField(max_length=200, null=True)
    ProvLastname = models.CharField(max_length=200)
    ProvPais = models.CharField(max_length=200)
    ProvTipoProd = models.CharField(max_length=200)

class tbProductos(models.Model):
    ProdName = models.CharField(max_length=200, null=True)
    ProdTipo = models.CharField(max_length=200)
    ProdUnidaddeMed = models.CharField(max_length=10)
    ProdName = models.CharField(max_length=5)
    ProdCantidad = models.IntegerField(default='0')
    ProdProveedor = models.ForeignKey(tbProveedores, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ProdName)