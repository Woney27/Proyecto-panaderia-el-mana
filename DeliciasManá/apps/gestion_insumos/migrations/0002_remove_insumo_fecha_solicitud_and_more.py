# Generated by Django 5.1.2 on 2024-11-10 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_insumos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumo',
            name='fecha_solicitud',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='idProveedor',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='pedidoNum',
        ),
    ]
