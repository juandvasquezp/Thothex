# Generated by Django 5.0.3 on 2024-04-26 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='Per_apellido',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='Per_nombre',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='Per_telefono',
        ),
        migrations.AlterField(
            model_name='persona',
            name='Mun_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.municipio', verbose_name='Municipio'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='Per_identificacion',
            field=models.IntegerField(verbose_name='Identificacion'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='Per_tipoId',
            field=models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('CE', 'Cedula de Extranjeria'), ('PA', 'Pasaporte')], max_length=30, verbose_name='Tipo de identificacion'),
        ),
    ]
