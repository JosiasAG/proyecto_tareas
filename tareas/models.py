from django.db import models
from django.contrib.auth.models import User

class lastareas(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField(blank=True)
    fecha_creacion=models.DateTimeField(auto_now=True)
    fecha_termino=models.DateTimeField(null=True)
    importante=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
