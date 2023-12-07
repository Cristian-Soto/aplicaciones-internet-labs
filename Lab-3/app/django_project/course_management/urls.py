from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_asignaturas, name='lista_asignaturas'),
    path('asignatura/<int:asignatura_id>/', views.detalle_asignatura, name='detalle_asignatura'),
    path('crear_asignatura/', views.crear_asignatura, name='crear_asignatura'),
    path('asignatura/<int:asignatura_id>/agregar_alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('asignatura/<int:asignatura_id>/modificar/', views.modificar_asignatura, name='modificar_asignatura'),
    path('asignatura/<int:asignatura_id>/eliminar/', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('alumno/<int:alumno_id>/modificar/', views.modificar_alumno, name='modificar_alumno'),
    path('alumno/<int:alumno_id>/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),
]
