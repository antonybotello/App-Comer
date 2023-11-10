from django.urls import path
from comunidad.views import usuario_crear,usuario_eliminar, usuario_editar
urlpatterns = [
    path("usuarios/", usuario_crear, name="usuarios"),
    path("usuarios/eliminar/<int:pk>/", usuario_eliminar, name="usuario-eliminar"),
    path("usuarios/editar/<int:pk>/", usuario_editar, name="usuario-editar")


]
