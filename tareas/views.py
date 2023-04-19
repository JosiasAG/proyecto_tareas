from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import tareasForm
from .models import lastareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'index.html')

def signup (request):
    if request.method=="GET":
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                    })  
        else:
            return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "Las contraseñas no coinciden"
                    }) 


def salida(request):
    logout(request)
    return redirect('inicio')
    
def ingreso(request):
    if request.method == "GET":
        return render(request, "ingreso.html", {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], 
        password=request.POST['password'])
        if user == None:
            return render(request, "ingreso.html", {
                'form': AuthenticationForm,
                'error': "El usuario y/o contraseña es incorrecto"
                })
        else:
            login(request, user)
            return redirect('tareas')


@login_required        
def creatarea(request):
    if request.method=='GET':
        return render(request, "creartareas.html", {'form': tareasForm})
    else:
        form = tareasForm(request.POST)
        new = form.save(commit=False)
        new.user = request.user
        new.save()
        return redirect('tareas')


@login_required     
def lasTareas(request):
    tare = lastareas.objects.filter(user=request.user)
    return render(request, 'tareas.html', {'tareas': tare})


@login_required 
def detalles(request, id_tarea):
    tares = None
    formulario = None
    if request.method=='GET':
        tares = get_object_or_404(lastareas, pk=id_tarea)
        formulario = tareasForm(instance=tares)
        return render(request, 'detalle_tarea.html', {'tareadeta':tares, 'formul': formulario})
    else:
        try:
            tares = get_object_or_404(lastareas, pk=id_tarea, user=request.user)
            formulario = tareasForm(request.POST ,instance=tares)
            formulario.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detalle_tarea.html', {'tareadeta':tares, 'formul': formulario})

@login_required         
def completado(request, id_tarea):
    tarea = get_object_or_404(lastareas, pk=id_tarea, user=request.user)
    tarea.fecha_termino = timezone.now()
    tarea.save()
    return redirect('tareas')

@login_required 
def eliminado(request, id_tarea):
    tarea2 = get_object_or_404(lastareas, pk=id_tarea, user=request.user)
    tarea2.delete()
    return redirect('tareas')