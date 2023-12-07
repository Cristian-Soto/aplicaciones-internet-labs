from django.shortcuts import render, get_object_or_404, redirect
from .models import Asignatura, Alumno
from .forms import AsignaturaForm, AlumnoForm

def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'lista_asignaturas.html', {'asignaturas': asignaturas})

def detalle_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    alumnos = asignatura.alumnos.all()
    return render(request, 'detalle_asignatura.html', {'asignatura': asignatura, 'alumnos': alumnos})

def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, 'crear_asignatura.html', {'form': form})

def agregar_alumno(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            asignatura.alumnos.add(alumno)
            return redirect('detalle_asignatura', asignatura_id=asignatura_id)
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form, 'asignatura': asignatura})

def modificar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('detalle_asignatura', asignatura_id=asignatura_id)
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'modificar_asignatura.html', {'form': form, 'asignatura': asignatura})

def eliminar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('lista_asignaturas')
    return render(request, 'eliminar_asignatura.html', {'asignatura': asignatura})

def modificar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('detalle_asignatura', asignatura_id=alumno.asignaturas.first().id)
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'modificar_alumno.html', {'form': form, 'alumno': alumno})

def eliminar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    asignatura_id = alumno.asignaturas.first().id
    if request.method == 'POST':
        alumno.delete()
        return redirect('detalle_asignatura', asignatura_id=asignatura_id)
    return render(request, 'eliminar_alumno.html', {'alumno': alumno})