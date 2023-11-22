from django.db import models
from operaciones.models import Producto
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=10,verbose_name="Nombre" )
    descripcion = models.TextField(max_length=100,verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=10,verbose_name="Nombre" )
    descripcion = models.TextField(max_length=100,verbose_name="Descripción")
    categoria = models.ForeignKey(Categoria, verbose_name="Categoría", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Subcategoria"
        verbose_name_plural = "Subategorias"

    def __str__(self):
        return self.nombre
class Sub_Producto(models.Model):
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria,verbose_name='Subcategoría', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Subcategoria_Producto"
        verbose_name_plural = "Subcategoria_Producto"



