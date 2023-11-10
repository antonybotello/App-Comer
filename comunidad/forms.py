from django.forms import ModelForm, widgets
from comunidad.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        fields= "__all__"
        exclude=["estado",]
        widgets={
            'fecha_nacimiento':widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

class UsuarioEditarForm(ModelForm):
    class Meta:
        model= Usuario
        fields= "__all__"
        exclude=["estado","fecha_nacimiento", "documento"]
        