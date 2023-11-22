from django.shortcuts import render, get_object_or_404, redirect
from configuracion.models import Slider
from configuracion.forms import SliderForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def slider(request):
    titulo = "Slider"
    accion = "Agregar"
    sliders=Slider.objects.all()
    if request.method == "POST":
        # Si se envió el formulario, procesa los datos del formulario
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡El Slider se agregó de forma exitosa!')
            return redirect("sliders")  # Redirige a la lista de sliders después de la creación
        else:
            messages.error(request, f'¡Error al agregar slider!')
    else:
        # Si es una solicitud GET, muestra un formulario en blanco
        form = SliderForm()
    # Obtén la URL de la vista "sliders"
    url_add = reverse("sliders")
    # Pasa el formulario y otros datos a la plantilla
    context = {
        "titulo": titulo,
        "form": form,
        "sliders":sliders,
        "url_add": url_add,
        "accion":accion

    }

    return render(request, "configuracion/slider.html", context)

def slider_editar(request, pk):
    titulo = "Configuración Slider"

    # Obtén el objeto Slider que se va a editar
    slider = get_object_or_404(Slider, id=pk)

    if request.method == "POST":
        # Si se envió el formulario, procesa los datos del formulario
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            return redirect("sliders")  # Redirige a la lista de sliders después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario con los datos existentes
        form = SliderForm(instance=slider)

    # Obtén la URL de la vista "sliders"
    url_add = reverse("editar_slider")

    # Pasa el formulario y otros datos a la plantilla
    context = {
        "titulo": titulo,
        "form": form,
        "url_add": url_add,
    }

    return render(request, "configuracion/slider_editar.html", context)

def slider_eliminar(request, pk):
# Obtén el objeto Slider que se va a "eliminar"
    slider = get_object_or_404(Slider, id=pk)

    # Cambia el estado de 1 a 0
    slider.estado = False
    slider.save()

    return redirect("sliders")  # Redirige a la lista de sliders después de cambiar el estado
