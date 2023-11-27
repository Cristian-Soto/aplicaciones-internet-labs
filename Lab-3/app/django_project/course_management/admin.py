from django.contrib import admin
from .models import Asignatura, Alumno

class AsignaturaAdmin(admin.ModelAdmin):
    list_display= ('codigo','nombre')

class AlumnoAdmin(admin.ModelAdmin):
    list_display= ('nombre','apellido_paterno','apellido_materno')

admin.site.register(Asignatura,AsignaturaAdmin)
admin.site.register(Alumno,AlumnoAdmin)