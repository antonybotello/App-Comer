# Generated by Django 4.2.6 on 2023-10-31 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción')),
                ('url', models.CharField(max_length=100, verbose_name='URL')),
                ('imagen', models.ImageField(upload_to='slider_images/')),
            ],
        ),
    ]
