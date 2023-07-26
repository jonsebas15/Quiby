from django.forms import ModelForm
from .models import enviar3, dinero

class sendForm(ModelForm):
    class Meta:
        model = enviar3
        fields = ['destinatario', 'monto', 'descripcion']

class disponible(ModelForm):
    class Meta:
        model = dinero 
        fields = []

