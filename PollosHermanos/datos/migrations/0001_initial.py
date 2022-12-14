# Generated by Django 4.1.2 on 2022-11-06 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbProveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProvEmpresa', models.CharField(max_length=200)),
                ('ProvName', models.CharField(max_length=200, null=True)),
                ('ProvLastname', models.CharField(max_length=200)),
                ('ProvPais', models.CharField(max_length=200)),
                ('ProvTipoProd', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbSucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SucName', models.CharField(max_length=200, null=True)),
                ('SucAddress', models.TextField()),
                ('SucGerente', models.CharField(max_length=200)),
                ('SucHorarios', models.CharField(max_length=200)),
                ('SucCombos', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdTipo', models.CharField(max_length=200)),
                ('ProdUnidaddeMed', models.CharField(max_length=10)),
                ('ProdName', models.CharField(max_length=5)),
                ('ProdCantidad', models.IntegerField(default='0')),
                ('ProdProveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.tbproveedores')),
            ],
        ),
        migrations.CreateModel(
            name='tbCombos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CombName', models.CharField(max_length=200, null=True)),
                ('CombTipo', models.CharField(max_length=200, null=True)),
                ('ComPrecio', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('CombDescripcion', models.CharField(max_length=200)),
                ('CombDisp', models.BooleanField(null=True)),
                ('CombSucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.tbsucursales')),
            ],
        ),
    ]
