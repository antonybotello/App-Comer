from django.urls import path
from operaciones.views import producto_crear, producto_editar,producto_eliminar
urlpatterns = [
    path("productos/", producto_crear, name="productos"),
    path("productos/eliminar/<int:pk>/", producto_eliminar, name="producto-eliminar"),
    path("productos/editar/<int:pk>/", producto_editar, name="producto-editar")


]
