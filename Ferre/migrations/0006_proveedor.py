# Generated by Django 3.1.3 on 2022-08-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferre', '0005_auto_20220724_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('IdProveedor', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Nombrecompleto', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('TipoProveedor', models.CharField(choices=[('Persona natural', 'Persona natural'), ('Personeria juridica', 'Pesoneria juridica')], max_length=50)),
                ('CedulaRepresentante', models.CharField(max_length=50, null=True)),
                ('NombreRepresentante', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Datos proveedor',
                'verbose_name_plural': 'Datos proveedor',
            },
        ),
    ]