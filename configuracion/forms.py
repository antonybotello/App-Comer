from django.forms import ModelForm
from configuracion.models import Slider
from django import forms
class SliderForm(ModelForm):
    class Meta:
        model= Slider
        fields= "__all__"
        exclude=["estado",]
        widgets = {
            'prioridad': forms.NumberInput(attrs={'max': 9}),
        }
        

