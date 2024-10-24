# Generated by Django 5.1.2 on 2024-10-23 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteMayorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=50)),
                ('cuit', models.PositiveIntegerField()),
                ('telefono', models.PositiveIntegerField()),
                ('domicilio', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaVenta', models.DateField(auto_now_add=True)),
                ('nroComprobante', models.IntegerField(unique=True)),
                ('tipoCliente', models.CharField(choices=[('minorista', 'Minorista'), ('mayorista', 'Mayorista')], default='Minorista', max_length=50)),
                ('formaPago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')], default='Efectivo', max_length=20)),
                ('montoTotal', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadProducto', models.PositiveIntegerField()),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='gestion_ventas.venta')),
            ],
        ),
    ]
