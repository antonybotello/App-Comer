from django.urls import path
from operaciones.views import *
urlpatterns = [
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('purgar-carrito/', purgar_carrito, name='purgar_carrito'),
    
    path('catalogo/<str:categoria>/<str:subcategoria>/<str:palabra>/', catalogo_productos, name='catalogo_productos'),


    path("productos/<int:producto_id>/", producto_detalle, name="producto-detalle"),
    path("productos-admin/", producto_crear, name="productos"),
    path("productos/eliminar/<int:pk>/", producto_eliminar, name="producto-eliminar"),
    path("productos/editar/<int:pk>/", producto_editar, name="producto-editar"),
    path("productos/<int:pk>/", producto_detalle, name="productos-usuario"),
   

]
