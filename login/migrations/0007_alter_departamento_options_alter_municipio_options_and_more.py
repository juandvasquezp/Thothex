# Generated by Django 5.0.3 on 2024-05-19 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_rename_persona_perfil_persona'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ('Dep_nombre',), 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'ordering': ('Mun_nombre',), 'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.AlterModelTable(
            name='departamento',
            table='login_departamento',
        ),
        migrations.AlterModelTable(
            name='municipio',
            table='login_municipio',
        ),
    ]