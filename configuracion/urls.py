from django.urls import path
from configuracion.views import slider,slider_editar,slider_eliminar
urlpatterns = [
    path('sliders/',slider,name="sliders"),
    path('sliders/editar/<int:pk>/',slider_editar,name="editar_slider"),
    path('sliders/eliminar/<int:pk>/',slider_eliminar,name="eliminar_slider"),



]
