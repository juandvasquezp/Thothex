# Generated by Django 5.0.3 on 2024-05-19 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0002_alter_factura_cl_codigo_compra_venta'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='compra',
            table='Compra',
        ),
        migrations.AlterModelTable(
            name='venta',
            table='Venta',
        ),
    ]
