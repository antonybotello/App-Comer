# Generated by Django 4.2.6 on 2023-11-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0002_usuario_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]