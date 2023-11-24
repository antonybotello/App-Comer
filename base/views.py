from django.shortcuts import render, redirect

from operaciones.models import Producto
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from comunidad.models import Usuario, Tienda
from operaciones.models import Pedido,Producto
from configuracion.models import Slider
from django.db.models import Count,Q
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
    titulo = "Bienvenido"
    
    # Obtener las cantidades correctas
    usuarios = Usuario.objects.all().count()
    tiendas = Tienda.objects.all().count()  
    productos = Producto.objects.all().count() 
    pedidos = Pedido.objects.all().count()  

    # Obtener nombres de tiendas y cantidad de productos por tienda
    tiendas_con_productos = Tienda.objects.annotate(cantidad_productos=Count('producto', filter=Q(producto__estado=True))).values('nombre', 'cantidad_productos')
    
    
    usuarios_obj = Usuario.objects.all()

    context = {
        "titulo": titulo,
        "usuarios_cantidad": usuarios,
        "tiendas_cantidad": tiendas,
        "productos_cantidad": productos,
        "pedidos_cantidad": pedidos,
        "usuarios_obj": usuarios_obj,
        "tiendas_con_productos": tiendas_con_productos
    }

    return render(request, "index-admin.html", context)

def logout_user(request):
    logout(request)
    return redirect('index')


