"""
URL configuration for proyectoPan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.inicio, name="inicio"),
    path("signup/", views.signup, name="signup"),
    path("tareas/", views.lasTareas, name="tareas"),
    path("logout/", views.salida, name="salida"),
    path('ingreso/', views.ingreso, name="ingreso"),
    path('nueva/', views.creatarea, name="nueva"),
    path('detalles/<int:id_tarea>/', views.detalles, name="detalles_tarea"),
    path('detalles/<int:id_tarea>/completas/', views.completado, name="completado"),
    path('detalles/<int:id_tarea>/eliminar/', views.eliminado, name="eliminar"),
    ]