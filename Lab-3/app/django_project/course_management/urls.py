from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crear_asignatura/', views.crear_asignatura, name='crear_asignatura'),
    path('asignatura/<int:asignatura_id>/', views.detalle_asignatura, name='detalle_asignatura'),
    path('asignatura/<int:asignatura_id>/agregar_alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('asignatura/editar/<int:asignatura_id>/', views.editar_asignatura, name='editar_asignatura'),
    path('alumno/editar/<int:alumno_id>/', views.editar_alumno, name='editar_alumno'),
    path('asignatura/eliminar/<int:asignatura_id>/', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('alumno/eliminar/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('alumno/<int:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
]