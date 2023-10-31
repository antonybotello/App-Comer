from django.db import models

# Create your models here.
class Slider(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    descripcion= models.CharField(max_length=200,verbose_name="Descripción")
    url= models.CharField(max_length=100,verbose_name="URL")
    imagen = models.ImageField(upload_to='slider_images/')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre