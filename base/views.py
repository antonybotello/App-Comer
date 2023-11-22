from django.shortcuts import render, redirect

from operaciones.models import Producto
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from comunidad.models import Usuario
from configuracion.models import Slider
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
    usuarios_obj= Usuario.objects.all()

    context={
        "titulo": titulo,
        "usuarios_cantidad":usuarios,
        "usuarios_obj":usuarios_obj
    }
    return render(request, "index-admin.html", context)

def logout_user(request):
    logout(request)
    return redirect('index')


