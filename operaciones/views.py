from django.shortcuts import render,redirect
from operaciones.models import Producto
from operaciones.forms import ProductoForm,ProductoEditarForm 
from django.contrib import messages
from PIL import Image
# Create your views here.
def producto_crear(request):
    titulo="Producto"
    accion="Agregar"
    productos= Producto.objects.all()
    if request.method=="POST":
        form= ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            producto= form.save()
            if producto.imagen:
                img = Image.open(producto.imagen.path)
                img= img.resize((500,500))
                img.save(producto.imagen.path)
            producto.save()
            messages.success(request, f'¡El Producto se agregó de forma exitosa!')

            return redirect("productos")
        else:
            messages.success(request, f'¡Error al agregar al Producto!')
    else:
        form=ProductoForm()
    context={
        "titulo":titulo,
        "productos":productos,
        "form":form,
        "accion":accion
    }
    return render(request,"operaciones/productos/productos.html", context)


def producto_editar(request,pk):
    producto= Producto.objects.get(id=pk)
    productos= Producto.objects.all()
    accion="Editar"
    nombre=f"{producto.nombre}"
    titulo=f"Producto {producto.id} {nombre}"

    if request.method=="POST":
        form= ProductoEditarForm(request.POST,request.FILES, instance=producto)
        if form.is_valid():
            producto= form.save()
            if producto.imagen:
                img = Image.open(producto.imagen.path)
                img= img.resize((500,500))
                img.save(producto.imagen.path)
            producto.save()
            messages.success(request, f'¡{nombre} se editó de forma exitosa!')
            return redirect("productos")
        else:
            messages.error(request, f'¡Error al editar a {nombre}!')

    else:
        form=ProductoEditarForm(instance=producto)
    context={
        "titulo":titulo,
        "productos":productos,
        "form":form,
        "accion":accion
    }
    return render(request,"operaciones/productos/productos.html", context)
def producto_eliminar(request,pk):

    producto=Producto.objects.filter(id=pk)
    producto.update(estado=False)
    
    ## Agregar mensjae de exito
    return redirect('productos')