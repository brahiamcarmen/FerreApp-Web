# Generated by Django 3.1.3 on 2022-08-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferre', '0019_auto_20220818_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='Fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]