from gestionAlumnos.models import Alumno, Area, Curso, Docente, Nota
from django.contrib import admin

# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    pass

class DocenteAdmin(admin.ModelAdmin):
    pass

class AreaAdmin(admin.ModelAdmin):
    pass

class CursoAdmin(admin.ModelAdmin):
    pass

class NotaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Nota, NotaAdmin)
