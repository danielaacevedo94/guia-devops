"""Este archivo contiene las clases de los formularios que se utilizan en la aplicación."""
from django import forms
from .models import Planificaciontareasmodel, Codificaciontareasmodel, Construcciontareasmodel, Pruebastareasmodel
from .models import Liberaciontareasmodel, Desplieguetareasmodel, Operacionestareasmodel, Monitoreotareasmodel, Usuariomodel
from .models import Planificacionherramientasmodel, Codificacionherramientasmodel, Construccionherramientasmodel, Pruebasherramientasmodel
from .models import Liberacionherramientasmodel, Despliegueherramientasmodel, Operacionesherramientasmodel, Monitoreoherramientasmodel

# pylint: disable=missing-class-docstring
class Planificaciontareasform(forms.ModelForm):
    class Meta:
        model = Planificaciontareasmodel
        exclude = ('fecha','userId')

class Planificacionherramientasform(forms.ModelForm):
    class Meta:
        model = Planificacionherramientasmodel
        exclude = ('fecha','userId')

class Codificaciontareasform(forms.ModelForm):
    class Meta:
        model = Codificaciontareasmodel
        exclude = ('fecha','userId')

class Codificacionherramientasform(forms.ModelForm):
    class Meta:
        model = Codificacionherramientasmodel
        exclude = ('fecha','userId')

class Usuarioform(forms.ModelForm):
    class Meta:
        model = Usuariomodel
        exclude = ('fecha',)

class Construcciontareasform(forms.ModelForm):
    class Meta:
        model = Construcciontareasmodel
        exclude = ('fecha','userId')

class Construccionherramientasform(forms.ModelForm):
    class Meta:
        model = Construccionherramientasmodel
        exclude = ('fecha','userId')

class Pruebastareasform(forms.ModelForm):
    class Meta:
        model = Pruebastareasmodel
        exclude = ('fecha','userId')

class Pruebasherramientasform(forms.ModelForm):
    class Meta:
        model = Pruebasherramientasmodel
        exclude = ('fecha','userId')

class Liberaciontareasform(forms.ModelForm):
    class Meta:
        model = Liberaciontareasmodel
        exclude = ('fecha','userId')

class Liberacionherramientasform(forms.ModelForm):
    class Meta:
        model = Liberacionherramientasmodel
        exclude = ('fecha','userId')

class Desplieguetareasform(forms.ModelForm):
    class Meta:
        model = Desplieguetareasmodel
        exclude = ('fecha','userId')

class Despliegueherramientasform(forms.ModelForm):
    class Meta:
        model = Despliegueherramientasmodel
        exclude = ('fecha','userId')

class Operacionestareasform(forms.ModelForm):
    class Meta:
        model = Operacionestareasmodel
        exclude = ('fecha','userId')

class Operacionesherramientasform(forms.ModelForm):
    class Meta:
        model = Operacionesherramientasmodel
        exclude = ('fecha','userId')

class Monitoreotareasform(forms.ModelForm):
    class Meta:
        model = Monitoreotareasmodel
        exclude = ('fecha','userId')

class Monitoreoherramientasform(forms.ModelForm):
    class Meta:
        model = Monitoreoherramientasmodel
        exclude = ('fecha','userId')
