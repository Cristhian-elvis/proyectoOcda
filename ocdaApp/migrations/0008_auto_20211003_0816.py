# Generated by Django 3.2.7 on 2021-10-03 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocdaApp', '0007_auto_20211003_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='area',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='cursomatriculado',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='cursomatriculado',
            name='curso',
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
            name='CursoMatriculado',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
    ]
