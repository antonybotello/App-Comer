# Generated by Django 4.2.6 on 2023-11-21 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, verbose_name='Nombre')),
                ('descripcion', models.TextField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, verbose_name='Nombre')),
                ('descripcion', models.TextField(max_length=100, verbose_name='Descripción')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clasificacion.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Subcategoria',
                'verbose_name_plural': 'Subategorias',
            },
        ),
        migrations.CreateModel(
            name='Sub_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operaciones.producto', verbose_name='Producto')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clasificacion.subcategoria', verbose_name='Subcategoría')),
            ],
            options={
                'verbose_name': 'Subcategoria_Producto',
                'verbose_name_plural': 'Subcategoria_Producto',
            },
        ),
    ]
