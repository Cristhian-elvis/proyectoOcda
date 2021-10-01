# Generated by Django 3.2.7 on 2021-10-01 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAlumnos', '0002_rename_curso_curso_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='area',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='curso',
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
    ]
