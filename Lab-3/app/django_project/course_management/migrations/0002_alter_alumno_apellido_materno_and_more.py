# Generated by Django 4.2.7 on 2023-12-07 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellido_materno',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido_paterno',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='asignaturas',
            field=models.ManyToManyField(to='course_management.asignatura'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
