from django.forms import ModelForm
from operaciones.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields= "__all__"
        exclude=["estado",]
        

class ProductoEditarForm(ModelForm):
    class Meta:
        model= Producto
        fields= "__all__"
        exclude=["estado",]


