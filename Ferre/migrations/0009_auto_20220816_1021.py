# Generated by Django 3.1.3 on 2022-08-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferre', '0008_auto_20220816_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='ClaseProveedor',
            field=models.CharField(choices=[('Minoristas', 'Minorista'), ('Mayorista', 'Mayorista')], max_length=50),
        ),
    ]
