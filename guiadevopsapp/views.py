"""This file contains the views for the application."""
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .forms import Planificaciontareasform, Usuarioform, Codificaciontareasform, Construcciontareasform, Pruebastareasform
from .forms import Liberaciontareasform, Desplieguetareasform, Operacionestareasform, Monitoreotareasform
from .forms import Planificacionherramientasform, Codificacionherramientasform, Construccionherramientasform, Pruebasherramientasform
from .forms import Liberacionherramientasform, Despliegueherramientasform, Operacionesherramientasform, Monitoreoherramientasform
from .models import Planificaciontareasmodel, Codificaciontareasmodel, Construcciontareasmodel, Pruebastareasmodel
from .models import Liberaciontareasmodel, Desplieguetareasmodel, Operacionestareasmodel, Monitoreotareasmodel, Usuariomodel
from .models import Planificacionherramientasmodel, Codificacionherramientasmodel, Construccionherramientasmodel, Pruebasherramientasmodel
from .models import Liberacionherramientasmodel, Despliegueherramientasmodel, Operacionesherramientasmodel, Monitoreoherramientasmodel

# pylint: disable=missing-function-docstring
@login_required(login_url="/accounts/google/login/")
def home(request):
    form = Planificaciontareasform()
    if request.method == 'POST':
        form = Planificaciontareasform(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            form = Planificaciontareasform()
        else:
            print('Form is invalid')

    
    context = {'form': form}
    return render(request, 'index.html', context)

def inicio(request):
    return render(request, 'home.html')

@login_required(login_url="/accounts/google/login/")
def iniciodash(request):
    return render(request, 'indexdash.html')

def actividades(request):
    return render(request, 'actividades.html')

@login_required(login_url="/accounts/google/login/")
def planificacion(request):
    return render(request, 'planificacion.html')

@login_required(login_url="/accounts/google/login/")
def planificaciontareas(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    planificacion = Planificaciontareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        planificacion = model_to_dict(planificacion)
    except :
        planificacion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in planificacion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Planificaciontareasform()

    try:
        planificacion_instance = Planificaciontareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Planificaciontareasmodel.DoesNotExist:
        planificacion_instance = None

    if request.method == 'POST':

        form = Planificaciontareasform(request.POST)
        
        if form.is_valid():
            planificacion_form = form.save(commit=False)
            planificacion_form.userId = social_user_id
            planificacion_form.save()
            return redirect('planificaciontareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Planificaciontareasform(instance=planificacion_instance)

    cantidadVerdaderos = len(true_counts)
    cantidadFalsos = len(false_counts)
    total=63
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
        }
    return render(request, 'planificaciontareas.html',context)

@login_required(login_url="/accounts/google/login/")
def planificacionherramientas(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    planificacion = Planificacionherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        planificacion = model_to_dict(planificacion)
    except :
        planificacion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in planificacion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Planificacionherramientasform()

    try:
        planificacion_instance = Planificacionherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Planificacionherramientasmodel.DoesNotExist:
        planificacion_instance = None

    if request.method == 'POST':

        form = Planificacionherramientasform(request.POST)
        
        if form.is_valid():
            planificacion_form = form.save(commit=False)
            planificacion_form.userId = social_user_id
            planificacion_form.save()
            return redirect('planificacionherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Planificacionherramientasform(instance=planificacion_instance)

    cantidadVerdaderos = len(true_counts)
    cantidadFalsos = len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    total=len(Planificacionherramientasmodel._meta.fields)-3
    #total=1
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
        }
    return render(request, 'planificacionherramientas.html',context)

@login_required(login_url="/accounts/google/login/")
def planificacionpracticas(request):
    return render(request, 'planificacionpracticas.html')

@login_required(login_url="/accounts/google/login/")
def perfilusuario(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    try:
        usuario_instance = Usuariomodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Usuariomodel.DoesNotExist:
        usuario_instance = None

    objetoBaseDatos=Usuariomodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    print(objetoBaseDatos)

    if request.method == 'POST':       
        form = Usuarioform(request.POST)
        numeroProyectos=request.POST.get('numeroProyectos')
        numeroEmpleados=request.POST.get('numeroEmpleados')
        tipoEmpresa=request.POST.get('tipoEmpresa')
        informacionModelo=Usuariomodel.objects.create(userId=social_user_id,numeroProyectos=numeroProyectos,numeroEmpleados=numeroEmpleados,tipoEmpresa=tipoEmpresa)
        informacionModelo.save()
        
        return redirect('perfilusuario')

    else:
        form = Usuarioform(instance=usuario_instance)
        
    context = {
        'form': form,        
        'objetoBaseDatos': objetoBaseDatos,
    }
    return render(request, 'perfilusuario.html',context)

@login_required(login_url="/accounts/google/login/")
def codificacion(request):
    return render(request, 'codificacion.html')

@login_required(login_url="/accounts/google/login/")
def codificaciontareas(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    codificacion = Codificaciontareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        codificacion = model_to_dict(codificacion)
    except :
        codificacion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in codificacion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Codificaciontareasform()

    try:
        codificacion_instance = Codificaciontareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Codificaciontareasmodel.DoesNotExist:
        codificacion_instance = None

    if request.method == 'POST':

        form = Codificaciontareasform(request.POST)
        
        if form.is_valid():
            codificacion_form = form.save(commit=False)
            codificacion_form.userId = social_user_id
            codificacion_form.save()
            return redirect('codificaciontareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Codificaciontareasform(instance=codificacion_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    total=23
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
        }
    return render(request, 'codificaciontareas.html', context)

@login_required(login_url="/accounts/google/login/")
def codificacionherramientas(request):
    
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    codificacion = Codificacionherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        codificacion = model_to_dict(codificacion)
    except :
        codificacion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in codificacion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Codificacionherramientasform()

    try:
        codificacion_instance = Codificacionherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Codificacionherramientasmodel.DoesNotExist:
        codificacion_instance = None

    if request.method == 'POST':

        form = Codificacionherramientasform(request.POST)
        
        if form.is_valid():
            codificacion_form = form.save(commit=False)
            codificacion_form.userId = social_user_id
            codificacion_form.save()
            return redirect('codificacionherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Codificacionherramientasform(instance=codificacion_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    total=len(Codificacionherramientasmodel._meta.fields)-3
    #total=2
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
        }
    return render(request, 'codificacionherramientas.html', context)

@login_required(login_url="/accounts/google/login/")
def codificacionpracticas(request):
    return render(request, 'codificacionpracticas.html')

@login_required(login_url="/accounts/google/login/")
def construccion(request):
    return render(request, 'construccion.html')

@login_required(login_url="/accounts/google/login/")
def construcciontareas(request):
    
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    construccion = Construcciontareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        construccion = model_to_dict(construccion)
    except :
        construccion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in construccion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Construcciontareasform()

    try:
        construccion_instance = Construcciontareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Construcciontareasmodel.DoesNotExist:
        construccion_instance = None

    if request.method == 'POST':

        form = Construcciontareasform(request.POST)
        
        if form.is_valid():
            construccion_form = form.save(commit=False)
            construccion_form.userId = social_user_id
            construccion_form.save()
            return redirect('construcciontareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Construcciontareasform(instance=construccion_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    total=18
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
        }
    return render(request, 'construcciontareas.html', context)

@login_required(login_url="/accounts/google/login/")
def construccionherramientas(request):
        
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    construccion = Construccionherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        construccion = model_to_dict(construccion)
    except :
        construccion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in construccion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Construcciontareasform()

    try:
        construccion_instance = Construccionherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Construccionherramientasmodel.DoesNotExist:
        construccion_instance = None

    if request.method == 'POST':

        form = Construccionherramientasform(request.POST)
        
        if form.is_valid():
            construccion_form = form.save(commit=False)
            construccion_form.userId = social_user_id
            construccion_form.save()
            return redirect('construccionherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Construccionherramientasform(instance=construccion_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    total=len(Construccionherramientasmodel._meta.fields)-3
    #total=1
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
        }
    return render(request, 'construccionherramientas.html', context)

@login_required(login_url="/accounts/google/login/")
def construccionpracticas(request):
    return render(request, 'construccionpracticas.html')

@login_required(login_url="/accounts/google/login/")
def pruebas(request):
    return render(request, 'pruebas.html')

@login_required(login_url="/accounts/google/login/")
def pruebastareas(request):
        
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    pruebas = Pruebastareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        pruebas = model_to_dict(pruebas)
    except :
        pruebas = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in pruebas.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Pruebastareasform()

    try:
        pruebas_instance = Pruebastareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Pruebastareasmodel.DoesNotExist:
        pruebas_instance = None

    if request.method == 'POST':

        form = Pruebastareasform(request.POST)
        
        if form.is_valid():
            pruebas_form = form.save(commit=False)
            pruebas_form.userId = social_user_id
            pruebas_form.save()
            return redirect('pruebastareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Pruebastareasform(instance=pruebas_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    total=23
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'pruebastareas.html', context)

@login_required(login_url="/accounts/google/login/")
def pruebasherramientas(request):
        
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    pruebas = Pruebasherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        pruebas = model_to_dict(pruebas)
    except :
        pruebas = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in pruebas.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Pruebasherramientasform()

    try:
        pruebas_instance = Pruebasherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Pruebasherramientasmodel.DoesNotExist:
        pruebas_instance = None

    if request.method == 'POST':

        form = Pruebasherramientasform(request.POST)
        
        if form.is_valid():
            pruebas_form = form.save(commit=False)
            pruebas_form.userId = social_user_id
            pruebas_form.save()
            return redirect('pruebasherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Pruebasherramientasform(instance=pruebas_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    #total=Pruebasherramientasmodel.objects.all().filter(userId=social_user_id).count()-1
    total=len(Pruebasherramientasmodel._meta.fields)-3
    #total=6
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'pruebasherramientas.html', context)

@login_required(login_url="/accounts/google/login/")
def pruebaspracticas(request):
    return render(request, 'pruebaspracticas.html')

@login_required(login_url="/accounts/google/login/")
def liberacion(request):
    return render(request, 'liberacion.html')

@login_required(login_url="/accounts/google/login/")
def liberaciontareas(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    liberacion = Liberaciontareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        liberacion = model_to_dict(liberacion)
    except :
        liberacion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in liberacion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Liberaciontareasform()

    try:
        liberacion_instance = Liberaciontareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Pruebastareasmodel.DoesNotExist:
        liberacion_instance = None

    if request.method == 'POST':

        form = Liberaciontareasform(request.POST)
        
        if form.is_valid():
            liberacion_form = form.save(commit=False)
            liberacion_form.userId = social_user_id
            liberacion_form.save()
            return redirect('liberaciontareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Liberaciontareasform(instance=liberacion_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    total=21
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'liberaciontareas.html', context)

@login_required(login_url="/accounts/google/login/")
def liberacionherramientas(request):
        
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    liberacion = Liberacionherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        liberacion = model_to_dict(liberacion)
    except :
        liberacion = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in liberacion.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Liberaciontareasform()

    try:
        liberacion_instance = Liberacionherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Pruebasherramientasmodel.DoesNotExist:
        liberacion_instance = None

    if request.method == 'POST':

        form = Liberacionherramientasform(request.POST)
        
        if form.is_valid():
            liberacion_form = form.save(commit=False)
            liberacion_form.userId = social_user_id
            liberacion_form.save()
            return redirect('liberacionherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Liberacionherramientasform(instance=liberacion_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    total=len(Liberacionherramientasmodel._meta.fields)-3
    #total=2
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'liberacionherramientas.html', context)

@login_required(login_url="/accounts/google/login/")
def liberacionpracticas(request):
    return render(request, 'liberacionpracticas.html')

@login_required(login_url="/accounts/google/login/")
def despliegue(request):
    return render(request, 'despliegue.html')

@login_required(login_url="/accounts/google/login/")
def desplieguetareas(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    despliegue = Desplieguetareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        despliegue = model_to_dict(despliegue)
    except :
        despliegue = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in despliegue.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Desplieguetareasform()

    try:
        despliegue_instance = Desplieguetareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Desplieguetareasmodel.DoesNotExist:
        despliegue_instance = None

    if request.method == 'POST':

        form = Desplieguetareasform(request.POST)
        
        if form.is_valid():
            despliegue_form = form.save(commit=False)
            despliegue_form.userId = social_user_id
            despliegue_form.save()
            return redirect('desplieguetareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Desplieguetareasform(instance=despliegue_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    total=23
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'desplieguetareas.html', context)

@login_required(login_url="/accounts/google/login/")
def despliegueherramientas(request):
        
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    despliegue = Despliegueherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        despliegue = model_to_dict(despliegue)
    except :
        despliegue = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in despliegue.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Despliegueherramientasform()

    try:
        despliegue_instance = Despliegueherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Despliegueherramientasmodel.DoesNotExist:
        despliegue_instance = None

    if request.method == 'POST':

        form = Despliegueherramientasform(request.POST)
        
        if form.is_valid():
            despliegue_form = form.save(commit=False)
            despliegue_form.userId = social_user_id
            despliegue_form.save()
            return redirect('despliegueherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Despliegueherramientasform(instance=despliegue_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    total=len(Despliegueherramientasmodel._meta.fields)-3
    #total=5
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'despliegueherramientas.html', context)

@login_required(login_url="/accounts/google/login/")
def desplieguepracticas(request):
    return render(request, 'desplieguepracticas.html')

@login_required(login_url="/accounts/google/login/")
def operaciones(request):
    return render(request, 'operaciones.html')

@login_required(login_url="/accounts/google/login/")
def operacionestareas(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    operaciones = Operacionestareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        operaciones = model_to_dict(operaciones)
    except :
        operaciones = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in operaciones.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Operacionestareasform()

    try:
        operaciones_instance = Operacionestareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Operacionestareasmodel.DoesNotExist:
        operaciones_instance = None

    if request.method == 'POST':

        form = Operacionestareasform(request.POST)
        
        if form.is_valid():
            operaciones_form = form.save(commit=False)
            operaciones_form.userId = social_user_id
            operaciones_form.save()
            return redirect('operacionestareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Operacionestareasform(instance=operaciones_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    total=23
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }    
    return render(request, 'operacionestareas.html', context)

@login_required(login_url="/accounts/google/login/")
def operacionesherramientas(request):
        
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    operaciones = Operacionesherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        operaciones = model_to_dict(operaciones)
    except :
        operaciones = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in operaciones.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Operacionesherramientasform()

    try:
        operaciones_instance = Operacionesherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Operacionesherramientasmodel.DoesNotExist:
        operaciones_instance = None

    if request.method == 'POST':

        form = Operacionesherramientasform(request.POST)
        
        if form.is_valid():
            operaciones_form = form.save(commit=False)
            operaciones_form.userId = social_user_id
            operaciones_form.save()
            return redirect('operacionesherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Operacionesherramientasform(instance=operaciones_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    total=len(Operacionesherramientasmodel._meta.fields)-3
    #total=5
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }    
    return render(request, 'operacionesherramientas.html', context)

@login_required(login_url="/accounts/google/login/")
def operacionespracticas(request):
    return render(request, 'operacionespracticas.html')

@login_required(login_url="/accounts/google/login/")
def monitoreo(request):
    return render(request, 'monitoreo.html')

@login_required(login_url="/accounts/google/login/")
def monitoreotareas(request):

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    monitoreo = Monitoreotareasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        monitoreo = model_to_dict(monitoreo)
    except :
        monitoreo = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in monitoreo.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Monitoreotareasform()

    try:
        monitoreo_instance = Monitoreotareasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Monitoreotareasmodel.DoesNotExist:
        monitoreo_instance = None

    if request.method == 'POST':

        form = Monitoreotareasform(request.POST)
        
        if form.is_valid():
            monitoreo_form = form.save(commit=False)
            monitoreo_form.userId = social_user_id
            monitoreo_form.save()
            return redirect('monitoreotareas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Monitoreotareasform(instance=monitoreo_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    total=26
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'monitoreotareas.html', context)

@login_required(login_url="/accounts/google/login/")
def monitoreoherramientas(request):
        
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        social_user_id = social_account.uid
    except:
        social_user_id = request.user.id
    
    monitoreo = Monitoreoherramientasmodel.objects.all().filter(userId=social_user_id).order_by('-fecha').first()
    
    try:
        monitoreo = model_to_dict(monitoreo)
    except :
        monitoreo = {}
    
    true_counts = {}
    false_counts = {}
    for key, value in monitoreo.items():

        if isinstance(value,bool):
            if value:
                true_counts[key] = true_counts.get(key, 0) + 1
            else:
                false_counts[key] = false_counts.get(key, 0) + 1
        

    form = Monitoreoherramientasform()

    try:
        monitoreo_instance = Monitoreoherramientasmodel.objects.filter(userId=social_user_id).order_by('-fecha').first()
    except Monitoreoherramientasmodel.DoesNotExist:
        monitoreo_instance = None

    if request.method == 'POST':

        form = Monitoreoherramientasform(request.POST)
        
        if form.is_valid():
            monitoreo_form = form.save(commit=False)
            monitoreo_form.userId = social_user_id
            monitoreo_form.save()
            return redirect('monitoreoherramientas')
        else:
            print('Form is invalid')
            print(form.errors)
    else:
        form = Monitoreoherramientasform(instance=monitoreo_instance)
    
    cantidadVerdaderos=len(true_counts)
    cantidadFalsos=len(false_counts)
    #total=cantidadFalsos+cantidadVerdaderos
    total=len(Monitoreoherramientasmodel._meta.fields)-3
    #total=5
    context = {
        'form': form,
        'diccionarioVerdaderos': true_counts,
        'diccionarioFalsos': false_counts,
        'cantidadVerdaderos': cantidadVerdaderos,
        'cantidadFalsos': cantidadFalsos,
        'total': total,
    }
    return render(request, 'monitoreoherramientas.html', context)

@login_required(login_url="/accounts/google/login/")
def monitoreopracticas(request):
    return render(request, 'monitoreopracticas.html')

@login_required(login_url="/accounts/google/login/")
def referencias(request):
    return render(request, 'referencias.html')