from django.forms import ModelForm
from .models import lastareas

class tareasForm(ModelForm):
    class Meta:
        model = lastareas
        fields = ['titulo','descripcion','importante']