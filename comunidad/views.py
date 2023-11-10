from django.shortcuts import render, redirect
from comunidad.forms import UsuarioForm,UsuarioEditarForm
from comunidad.models import Usuario
from django.contrib import messages
from PIL import Image
# Create your views here.
def usuario_crear(request):
    titulo="Usuario"
    accion="Agregar"
    usuarios= Usuario.objects.all()
    if request.method=="POST":
        form= UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            usuario= form.save()
            if usuario.imagen:
                img = Image.open(usuario.imagen.path)
                img= img.resize((500,500))
                img.save(usuario.imagen.path)
            usuario.save()
            messages.success(request, f'¡El Usuario se agregó de forma exitosa!')

            return redirect("usuarios")
        else:
            messages.success(request, f'¡Error al agregar al Usuario!')
    else:
        form=UsuarioForm()
    context={
        "titulo":titulo,
        "usuarios":usuarios,
        "form":form,
        "accion":accion
    }
    return render(request,"comunidad/usuarios/usuarios.html", context)
def usuario_editar(request,pk):
    usuario= Usuario.objects.get(id=pk)
    usuarios= Usuario.objects.all()
    accion="Editar"
    nombre=f"{usuario.primer_nombre} {usuario.primer_apellido}"
    titulo=f"Usuario {usuario.id} {nombre}"

    if request.method=="POST":
        form= UsuarioEditarForm(request.POST,request.FILES, instance=usuario)
        if form.is_valid():
            usuario= form.save()
            if usuario.imagen:
                img = Image.open(usuario.imagen.path)
                img= img.resize((500,500))
                img.save(usuario.imagen.path)
            usuario.save()
            messages.success(request, f'¡{nombre} se editó de forma exitosa!')
            return redirect("usuarios")
        else:
            messages.error(request, f'¡Error al editar a {nombre}!')

    else:
        form=UsuarioEditarForm(instance=usuario)
    context={
        "titulo":titulo,
        "usuarios":usuarios,
        "form":form,
        "accion":accion
    }
    return render(request,"comunidad/usuarios/usuarios.html", context)
def usuario_eliminar(request,pk):

    usuario=Usuario.objects.filter(id=pk)
    usuario.update(estado=False)
    
    ## Agregar mensjae de exito
    return redirect('usuarios')