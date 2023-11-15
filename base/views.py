from django.shortcuts import render, redirect
from configuracion.models import Slider
from operaciones.models import Producto
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from comunidad.models import Usuario
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
@login_required
def principal_admin(request):
    titulo="Bienvenido"
    usuarios= Usuario.objects.all().count()
    context={
        "titulo": titulo,
        "usuarios_cantidad":usuarios
    }
    return render(request, "index-admin.html", context)

def logout_user(request):
    logout(request)
    return redirect('index')
