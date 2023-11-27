from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    asignaturas = models.ManyToManyField(Asignatura, related_name='alumno')
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
# Create your models here.
