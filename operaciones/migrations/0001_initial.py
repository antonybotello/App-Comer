# Generated by Django 4.2.6 on 2023-11-08 02:23

from django.db import migrations, models
import django.db.models.deletion
import operaciones.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comunidad', '0005_alter_tienda_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='operaciones\\productos\\default-product.png', null=True, upload_to=operaciones.models.get_image_filename)),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('precio', models.PositiveIntegerField(verbose_name='Precio')),
                ('estado', models.BooleanField(default=True)),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comunidad.tienda', verbose_name='Tienda')),
            ],
        ),
    ]