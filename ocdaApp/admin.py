from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from ocdaApp.models import Alumno, Area, Curso, CursoMatriculado, Docente, Nota

# Register your models here.

class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumno

@admin.register(Alumno)
class AlumnoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'dni',
        'nombre',
        'apellido',
        'promedio'
    )

    resource_class = AlumnoResource

#---------------

class DocenteResource(resources.ModelResource):
    class Meta:
        model = Docente

@admin.register(Docente)
class DocenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'dni',
        'nombre',
        'apellido'
    )

    resource_class = DocenteResource

#---------------

class AreaResource(resources.ModelResource):
    class Meta:
        model = Area

@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'nombre',
    )

    resource_class =AreaResource

#---------------

class CursoResource(resources.ModelResource):
    class Meta:
        model = Curso

@admin.register(Curso)
class CursoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'nombre',
        'docente',
        'area'
    )

    resource_class =CursoResource

#---------------

class CursoMatriculadoResource(resources.ModelResource):
    class Meta:
        model = CursoMatriculado

@admin.register(CursoMatriculado)
class CursoMatriculadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'alumno',
        'curso',
        'nota_Final'
    )

    resource_class =CursoMatriculadoResource

#---------------

class NotaResource(resources.ModelResource):
    class Meta:
        model = Nota

@admin.register(Nota)
class NotaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = (
        'cursoMatriculado',
        'trimestre_1',
        'trimestre_2',
        'trimestre_3'
    )

    resource_class =NotaResource

#admin.site.register(Alumno, AlumnoAdmin)
#admin.site.register(Docente, DocenteAdmin)
#admin.site.register(Area, AreaAdmin)
#admin.site.register(Curso, CursoAdmin)
#admin.site.register(Nota, NotaAdmin)
