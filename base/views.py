from django.shortcuts import render
from configuracion.models import Slider
from operaciones.models import Producto
def principal(request):
    titulo="Bienvenido"
    sliders= Slider.objects.filter(estado=True)
    productos= Producto.objects.all()
    context={
        "titulo": titulo,
        "sliders": sliders,
        "productos":productos
    }
    return render(request, "index.html", context)

def principal_admin(request):
    titulo="Bienvenido"
    context={
        "titulo": titulo,
    }
    return render(request, "index-admin.html", context)