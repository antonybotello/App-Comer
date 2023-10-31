from django.shortcuts import render
from configuracion.models import Slider

def principal(request):
    titulo="Bienvenido"
    sliders= Slider.objects.filter(estado=True)
    context={
        "titulo": titulo,
        "sliders": sliders
    }
    return render(request, "index.html", context)

def principal_admin(request):
    titulo="Bienvenido"
    context={
        "titulo": titulo,
    }
    return render(request, "index-admin.html", context)