# Generated by Django 5.1.2 on 2024-11-04 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_productos', '0002_alter_producto_cantidad_disponible_and_more'),
        ('gestion_ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='precioItem',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='item',
            name='producto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gestion_productos.producto'),
        ),
        migrations.AlterField(
            model_name='clientemayorista',
            name='cuit',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
