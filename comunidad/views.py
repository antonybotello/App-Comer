from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from comunidad.forms import UsuarioForm,UsuarioEditarForm, GroupForm, TiendaForm,TiendaEditarForm
from comunidad.models import Usuario, Tienda
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
# Create your views here.

#@permission_required('comunidad.add_usuario', raise_exception=True)
def usuario_crear(request):
    titulo="Usuario"
    accion="Agregar"
    usuarios= Usuario.objects.all()
    if request.method=="POST":
        form= UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['documento']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['documento']
                user.first_name= request.POST['primer_nombre']
                user.last_name= request.POST['primer_apellido']
                user.email= request.POST['correo']
                user.password=make_password("@" + request.POST['primer_nombre'][0] + request.POST['primer_apellido'][0] + request.POST['documento'][-4:])
                user.save()
            else:
                user=User.objects.get(username=request.POST['documento'])
            rol_id = request.POST.get('rol')  # Obtén el ID del grupo seleccionado en el formulario
            if rol_id:
                rol = Group.objects.get(id=rol_id)
                user.groups.add(rol)  # Asocia el usuario al grupo
            usuario = Usuario.objects.create(
                primer_nombre=request.POST['primer_nombre'],
                segundo_nombre=request.POST['segundo_nombre'],
                primer_apellido=request.POST['primer_apellido'],
                segundo_apellido=request.POST['segundo_apellido'],
                fecha_nacimiento=request.POST['fecha_nacimiento'],
                imagen=request.FILES.get('imagen'),  # Asume que tu formulario maneja archivos
                correo=request.POST['correo'],
                tipo_documento=request.POST['tipo_documento'],
                documento=request.POST['documento'],
                user=user,
                
            )
            messages.success(request, f'¡El Usuario se agregó de forma exitosa!')
            if usuario.imagen:
                 img = Image.open(usuario.imagen.path)
                 img= img.resize((500,500))
                 img.save(usuario.imagen.path)
            usuario.save()
            return redirect('usuarios')

        else:
            messages.success(request, f'¡Error al agregar al Usuario!')
            form = UsuarioForm(request.POST,request.FILES)
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
    titulo=f"Usuario {nombre}"

    if request.method=="POST":
        form= UsuarioEditarForm(request.POST,request.FILES, instance=usuario)
        if form.is_valid():
            usuario= form.save()
            # Actualizar el grupo del usuario
            rol_id = request.POST.get('rol')
            if rol_id:
                rol = Group.objects.get(id=rol_id)
                usuario.user.groups.set([rol])
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

def edit_group(request, group_id=None):
    groups = Group.objects.all()
    if group_id:
        group = get_object_or_404(Group, id=group_id)
    else:
        group = None

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('edit_group',group_id)  # Cambia 'list_groups' por el nombre de la URL donde se listan los grupos
    else:
        form = GroupForm(instance=group)
    context={
    'groups':groups,
    'group': group,
    'form': form
    }
    return render(request, 'comunidad/usuarios/grupos.html', context)


def tienda_crear(request):
    titulo="Tienda"
    accion="Agregar"
    tiendas= Tienda.objects.all()
    if request.method=="POST":
        form= TiendaForm(request.POST,request.FILES)
        if form.is_valid():
            tienda= form.save()
            tienda.save()
            messages.success(request, f'¡El Tienda se agregó de forma exitosa!')

            return redirect("tiendas")
        else:
            messages.success(request, f'¡Error al agregar al Tienda!')
    else:
        form=TiendaForm()
    context={
        "titulo":titulo,
        "tiendas":tiendas,
        "form":form,
        "accion":accion
    }
    return render(request,"comunidad/tiendas/tiendas.html", context)


def tienda_eliminar(pk):
    tienda=Tienda.objects.filter(id=pk)
    tienda.update(estado=False)
    
    ## Agregar mensjae de exito
    return redirect('tiendas')


def tienda_editar(request,pk):
    tienda= Tienda.objects.get(id=pk)
    tiendas= Tienda.objects.all()
    accion="Editar"
    titulo=f"Tienda {tienda.nombre}"

    if request.method=="POST":
        form= TiendaEditarForm(request.POST,request.FILES, instance=tienda)
        if form.is_valid():
            tienda= form.save()
           
            messages.success(request, f'¡{tienda.nombre} se editó de forma exitosa!')
            return redirect("tiendas")
        else:
            messages.error(request, f'¡Error al editar a {tienda.nombre}!')

    else:
        form=TiendaEditarForm(instance=tienda)
    context={
        "titulo":titulo,
        "tiendas":tiendas,
        "form":form,
        "accion":accion
    }
    return render(request,"comunidad/tiendas/tiendas.html", context)