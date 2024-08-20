# Generated by Django 5.0.3 on 2024-04-04 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('Dep_id', models.AutoField(primary_key=True, serialize=False)),
                ('Dep_nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('Mun_id', models.AutoField(primary_key=True, serialize=False)),
                ('Mun_nombre', models.CharField(max_length=30)),
                ('Dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('Per_id', models.AutoField(primary_key=True, serialize=False)),
                ('Per_tipoId', models.CharField(max_length=30)),
                ('Per_identificacion', models.IntegerField()),
                ('Per_nombre', models.CharField(max_length=40)),
                ('Per_apellido', models.CharField(max_length=40)),
                ('Per_password', models.CharField(max_length=50)),
                ('Per_correo', models.EmailField(max_length=254)),
                ('Per_telefono', models.IntegerField()),
                ('Dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.departamento')),
                ('Mun_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Cliente', models.IntegerField()),
                ('departamento_Id', models.IntegerField()),
                ('municipio_Id', models.IntegerField()),
                ('obligacion', models.IntegerField()),
                ('persona_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.persona')),
            ],
        ),
    ]
