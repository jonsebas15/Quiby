from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class enviar(models.Model):
    destinatario = models.CharField(max_length=15)
    monto = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class dinero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dinero = models.CharField(max_length=30)

class UsuarioPersonalizado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dinero = models.DecimalField(default=0, max_digits=10, decimal_places=2)

class datosUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dinero = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)

class enviar2(models.Model):
    destinatario = models.CharField(max_length=15)
    monto = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

class enviar3(models.Model):
    destinatario = models.CharField(max_length=15)
    monto = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    nombreUser = models.CharField(max_length=30)