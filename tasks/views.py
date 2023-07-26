from django.shortcuts import render, redirect
from django.http import HttpResponse
# con esta clase hago un preterminado formulario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError
from .form import sendForm
from .models import enviar3, dinero, UsuarioPersonalizado, datosUsuario
from django.contrib.auth.decorators import login_required #protege rutas
from decimal import Decimal


# Create your views here.


def principal(request):
    # return HttpResponse("<h1>Hola mundo</h1>") otra forma (se usa el httpResponse)
    return render(request, 'index.html')


def registrar(request):
    if request.method == 'GET':
        return render(request, 'registrar.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                print(request.POST)
                usuario = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    )
                usuario.save()
                usuario2 = datosUsuario.objects.create(usuario =usuario, dinero=0, nombre=request.POST['nombre'], email=request.POST['email'])
                usuario2.save()
                #return HttpResponse('Usuario creado')
                login(request, usuario)
                return render(request, 'index.html')
            except IntegrityError:
                # return HttpResponse('El usuario ya existe')
                return render(request, 'registrar.html', {
                    'form': UserCreationForm,
                    "error": 'Este usuario  ya fue creado'
                    })
        return render(request, 'registrar.html', {
                    'form': UserCreationForm,
                    "error" :'Las contraseñas no coiciden'
                })
@login_required
def cartera(request):
    cuenta = datosUsuario.objects.get(usuario = request.user)

    #prueba = User.objects.get(username = 'johan1')
    print(cuenta.usuario)

    return render(request, 'cartera.html',{
        'cuenta': cuenta,
    })

def salir(request):
    logout(request)
    return render(request, 'index.html')

def ingresar(request):
    if request.method == 'GET':
        return render(request, 'ingresar.html')
    else:
       usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if usuario is None:
            return render(request, 'ingresar.html',{
                'form': AuthenticationForm,
                'error': 'cedula o codigo incorrecto(s)'
                }) 
       else:
           login(request, usuario)
           return render(request, 'index.html')
@login_required      
def enviarDinero(request):
    if request.method == 'GET':
        return render(request, 'enviarDinero.html')
    else:
        try:
            try:
                destinatario = User.objects.get(username = request.POST['destinatario'])
                print(destinatario)
                form = sendForm(request.POST)
                new_task = form.save(commit = False)
                new_task.user = request.user

                cuenta = datosUsuario.objects.get(usuario = request.user)
                cuenta2 = datosUsuario.objects.get(usuario = destinatario)
                

                new_task.nombre = cuenta2.nombre
                new_task.nombreUser = cuenta.nombre

                
                dinero = Decimal(new_task.monto)
                if cuenta.dinero < dinero:
                    return render(request, 'enviarDinero.html', {
                    'form': sendForm,
                    'error': 'No tienes suficiente dinero para enviar',
                    })
                cuenta.dinero -= dinero
                cuenta.save()

            
                cuenta2.dinero += dinero
                new_task.save()
                cuenta2.save()
                    
                return render(request, 'enviarDinero.html', {
                'form': sendForm,
                'error': 'El dinero fue enviado con exito',
                })
            except:
                return render(request, 'enviarDinero.html', {
                'form': sendForm,
                'error': 'El usuario a intentar enviar no existe',
                })
            
        except ValueError:
            return render(request, 'enviarDinero.html', {
                'form': sendForm,
                'error': 'Error en los datos'})
@login_required
def historial(request):
    listas = enviar3.objects.filter(user=request.user)
    print(listas)
    for i in listas:
        print(i)
        print(i.monto)
    listas2 = enviar3.objects.filter(destinatario = request.user)
    

    

    return render(request, 'historial.html', {
        'listas': listas,
        'listas2': listas2,
    })


def ganar1000(request):
    cuenta = datosUsuario.objects.get(usuario = request.user)
    cuenta.dinero += 1000
    cuenta.save()
    return render(request, 'cartera.html', {
            'cuenta': cuenta,
    })