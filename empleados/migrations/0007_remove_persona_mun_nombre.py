# Generated by Django 5.0.3 on 2024-06-22 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0006_empleado_usr_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='Mun_nombre',
        ),
    ]
