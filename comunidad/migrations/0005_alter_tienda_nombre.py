# Generated by Django 4.2.6 on 2023-11-08 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0004_tienda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='nombre',
            field=models.CharField(max_length=45, verbose_name='Nombre'),
        ),
    ]
