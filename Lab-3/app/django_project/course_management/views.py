from django.shortcuts import render, get_object_or_404, redirect
from .models import Asignatura, Alumno
def index(request):
	return render(request, 'index.html')

def crear_asignatura(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        codigo = request.POST['codigo']
        asignatura = Asignatura(nombre=nombre, codigo=codigo)
        asignatura.save()
        return redirect('/asignatura/'+str(asignatura.id))  # Redirige a la página de inicio después de crear la asignatura.
    else:
        # Si se accedió a la página de creación de asignaturas por GET, muestra el formulario.
        return render(request, 'crear_asignatura.html')

def detalle_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    return render(request, 'detalle_asignatura.html', {'asignatura': asignatura})

def agregar_alumno(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)


    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido_paterno = request.POST['apellido_paterno']
        apellido_materno = request.POST['apellido_materno']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        alumno = Alumno(
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            fecha_nacimiento=fecha_nacimiento,
        )
        alumno.save()
        asignatura.alumno.add(alumno)
        return redirect('detalle_asignatura', asignatura_id=asignatura_id)  
    else:
        return render(request, 'agregar_alumno.html', {'asignatura': asignatura})

def eliminar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    asignatura.delete()
    return redirect('lista_asignaturas')

def eliminar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    alumno.delete()
    return redirect('lista_alumnos')

def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)

    if request.method == 'POST':
        asignatura.nombre = request.POST['nombre']
        asignatura.codigo = request.POST['codigo']
        asignatura.save()
        return redirect('detalle_asignatura', asignatura.id)

    return render(request, 'editar_asignatura.html', {'asignatura': asignatura})

def editar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)

    if request.method == 'POST':
        alumno.nombre = request.POST['nombre']
        alumno.apellido_paterno = request.POST['apellido_paterno']
        alumno.apellido_materno = request.POST['apellido_materno']
        alumno.fecha_nacimiento = request.POST['fecha_nacimiento']
        alumno.save()
        return redirect('detalle_alumno', alumno.id)

    return render(request, 'editar_alumno.html', {'alumno': alumno})

def detalle_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    
    
    return render(request, 'detalle_alumno.html', {'alumno': alumno})