from django.contrib import admin
from .models import lastareas

class adminTareas(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)

admin.site.register(lastareas, adminTareas)
