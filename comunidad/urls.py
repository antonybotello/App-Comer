from django.urls import path
from comunidad.views import usuario_crear,usuario_eliminar, usuario_editar, edit_group
from comunidad.views import tienda_crear,tienda_eliminar,tienda_editar
urlpatterns = [
    path("usuarios/", usuario_crear, name="usuarios"),
    path("usuarios/eliminar/<int:pk>/", usuario_eliminar, name="usuario-eliminar"),
    path("usuarios/editar/<int:pk>/", usuario_editar, name="usuario-editar"),

    path("tiendas/", tienda_crear, name="tiendas"),  
    path("tiendas/eliminar/<int:pk>/", tienda_eliminar, name="tienda-eliminar"),
    path("tiendas/editar/<int:pk>/", tienda_editar, name="tienda-editar"),

    path('usuarios/roles/', edit_group, name='create_group'),
    path('usuarios/roles/<int:group_id>/', edit_group, name='edit_group'),

]
