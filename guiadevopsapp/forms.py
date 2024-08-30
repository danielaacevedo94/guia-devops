"""Este archivo contiene las clases de los formularios que se utilizan en la aplicación."""
from django import forms
from .models import Planificaciontareasmodel, Codificaciontareasmodel, Construcciontareasmodel, Pruebastareasmodel
from .models import Liberaciontareasmodel, Desplieguetareasmodel, Operacionestareasmodel, Monitoreotareasmodel, Usuariomodel
from .models import Planificacionherramientasmodel, Codificacionherramientasmodel, Construccionherramientasmodel, Pruebasherramientasmodel
from .models import Liberacionherramientasmodel, Despliegueherramientasmodel, Operacionesherramientasmodel, Monitoreoherramientasmodel

# pylint: disable=missing-class-docstring
"""class Planificaciontareasform(forms.ModelForm):
    class Meta:
        model = Planificaciontareasmodel
        exclude = ('fecha',)"""

class Planificaciontareasform(forms.ModelForm):
    class Meta:
        model = Planificaciontareasmodel
        exclude = ('fecha','userId')
        

class Planificacionherramientasform(forms.ModelForm):
    class Meta:
        model = Planificacionherramientasmodel
        exclude = ('fecha',)

class Codificaciontareasform(forms.ModelForm):
    class Meta:
        model = Codificaciontareasmodel
        exclude = ('fecha',)

class Codificacionherramientasform(forms.ModelForm):
    class Meta:
        model = Codificacionherramientasmodel
        exclude = ('fecha',)

class Usuarioform(forms.ModelForm):
    class Meta:
        model = Usuariomodel
        exclude = ('fecha',)

class Construcciontareasform(forms.ModelForm):
    class Meta:
        model = Construcciontareasmodel
        exclude = ('fecha',)

class Construccionherramientasform(forms.ModelForm):
    class Meta:
        model = Construccionherramientasmodel
        exclude = ('fecha',)

class Pruebastareasform(forms.ModelForm):
    class Meta:
        model = Pruebastareasmodel
        exclude = ('fecha',)

class Pruebasherramientasform(forms.ModelForm):
    class Meta:
        model = Pruebasherramientasmodel
        exclude = ('fecha',)

class Liberaciontareasform(forms.ModelForm):
    class Meta:
        model = Liberaciontareasmodel
        exclude = ('fecha',)

class Liberacionherramientasform(forms.ModelForm):
    class Meta:
        model = Liberacionherramientasmodel
        exclude = ('fecha',)

class Desplieguetareasform(forms.ModelForm):
    class Meta:
        model = Desplieguetareasmodel
        exclude = ('fecha',)

class Despliegueherramientasform(forms.ModelForm):
    class Meta:
        model = Despliegueherramientasmodel
        exclude = ('fecha',)

class Operacionestareasform(forms.ModelForm):
    class Meta:
        model = Operacionestareasmodel
        exclude = ('fecha',)

class Operacionesherramientasform(forms.ModelForm):
    class Meta:
        model = Operacionesherramientasmodel
        exclude = ('fecha',)

class Monitoreotareasform(forms.ModelForm):
    class Meta:
        model = Monitoreotareasmodel
        exclude = ('fecha',)

class Monitoreoherramientasform(forms.ModelForm):
    class Meta:
        model = Monitoreoherramientasmodel
        exclude = ('fecha',)
