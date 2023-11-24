from django.shortcuts import render,redirect,get_object_or_404
from operaciones.models import Producto,Pedido
from operaciones.forms import ProductoForm,ProductoEditarForm
from django.contrib import messages
from django.http import JsonResponse
from PIL import Image
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto = Producto.objects.get(id=producto_id)

    # Convierte producto_id a cadena para asegurarte de consistencia
    str_producto_id = str(producto_id)

    if str_producto_id in carrito:
        # El producto ya está en el carrito, incrementa la cantidad
        carrito[str_producto_id] += 1
    else:
        # El producto no está en el carrito, agrégalo con cantidad 1
        carrito[str_producto_id] = 1

    request.session['carrito'] = carrito
    messages.success(request, f'¡Se agregó {producto.nombre} al carrito!')
    print(carrito)
    return redirect(request.META.get('HTTP_REFERER', f'/operaciones/productos/{producto_id}/'))

def eliminar_producto_carrito(request, producto_id):
    try:
        # Lógica para eliminar el producto del carrito
        carrito = request.session.get('carrito', {})
        if str(producto_id) in carrito:
            del carrito[str(producto_id)]
            request.session['carrito'] = carrito
            messages.warning(request, f'¡Se ha eliminado el producto del carrito!')
            return JsonResponse({'success': True})
        
        else:
            return JsonResponse({'success': False, 'message': 'Producto no encontrado en el carrito.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

def purgar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
    messages.warning(request, f'¡Se ha vaciado el carrito!')

    return redirect(request.META.get('HTTP_REFERER', "index"))

def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    titulo = producto.nombre
    productos = Producto.objects.filter(tienda=producto.tienda,estado=True).exclude(id=producto_id)

    context = {
        "titulo": titulo,
        "producto_obj": producto,
        "productos": productos,
    }

    return render(request, "partials/usuarios/operaciones/productos/producto-hoja.html", context)

def catalogo_productos(request,categoria=None,subcategoria=None, palabra=None):
    pass
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
    
    messages.success(request, f'¡El Producto "{producto[0].nombre}" se eliminó correctamente!')
    return redirect('productos')


def pedido_crear(request):
    titulo = "Pedido"
    accion = "Agregar"
    pedidos = Pedido.objects.all()

    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            messages.success(request, f'¡El Pedido se agregó de forma exitosa!')
            return redirect("pedidos")
        else:
            messages.error(request, 'Error al agregar el Pedido. Por favor, verifica los campos.')
    else:
        form = PedidoForm()

    context = {
        "titulo": titulo,
        "pedidos": pedidos,
        "form": form,
        "accion": accion
    }
    return render(request, "ruta_de_tu_template/pedido_template.html", context)