from comunidad.models import Usuario
from operaciones.models import Producto

def sesion(request):
    usuario_actual= request.user
    image_user= r"/media/comunidad/default-user.jpeg"
    if request.user.is_authenticated:
        if Usuario.objects.filter(user_id=usuario_actual.id):
            image_user=Usuario.objects.get(user_id=usuario_actual.id).imagen.url
    context={
        'usuario_actual':usuario_actual,
        'image_user': image_user
    }
    return context


def carrito(request):
    carrito = request.session.get('carrito', {})
    productos_carrito = Producto.objects.filter(id__in=carrito.keys())
    total_items = sum(carrito.values())

    productos_con_cantidad = [
        {'producto': producto, 'cantidad': carrito.get(str(producto.id), 0)} 
        for producto in productos_carrito
    ]
    total_pedido = sum(item['producto'].precio * item['cantidad'] for item in productos_con_cantidad)

    return {
        'carrito': carrito,
        'productos_con_cantidad': productos_con_cantidad,
        'total_items': total_items,
        'total_pedido': total_pedido,
    }
