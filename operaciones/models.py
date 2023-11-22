from django.db import models
from comunidad.models import Tienda, Usuario


def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}-{instance.tienda.nombre}.{ext}"
    return f"operaciones/productos/{filename}"
# Create your models here.

    
class Producto(models.Model):
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True,default="operaciones\productos\default-product.png")
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    precio= models.PositiveIntegerField(verbose_name="Precio")
    tienda= models.ForeignKey(Tienda, verbose_name="Tienda", on_delete=models.CASCADE)
    estado=models.BooleanField(default=True)

class Pedido(models.Model):
    cliente= models.ForeignKey(Usuario, verbose_name="Cliente",related_name='Cliente', on_delete=models.CASCADE)
    tienda= models.ForeignKey(Tienda, verbose_name="Tienda", on_delete=models.CASCADE)
    fecha_apertura=models.DateField(auto_now=True)
    estado=models.BooleanField(default=True)
    observacion= models.TextField()

class Detalle_Pedido(models.Model):
    pedido=models.ForeignKey(Pedido, verbose_name="Pedido #", on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Detalle_Pedido"
        verbose_name_plural = "Detalle_Pedidos"

    def __str__(self):
        return self.pedido 


