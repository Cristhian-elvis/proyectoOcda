from django.db import models

# Create your models here.

class Alumno(models.Model):
    dni = models.IntegerField(default=0)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    promedio = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

#----------------

class Docente(models.Model):
    dni = models.IntegerField(default=0)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

#----------------

class Area(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#----------------

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    
    #alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    #nota_Final = models.IntegerField(default=0)

    def __str__(self):
        return str(self.nombre)

#----------------

class CursoMatriculado(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    nota_Final = models.IntegerField(default=0)

    def __str__(self):
        return str(self.alumno) + " " + str(self.curso)

#----------------

class Nota(models.Model):
    cursoMatriculado = models.ForeignKey(CursoMatriculado, on_delete=models.CASCADE)

    trimestre_1 = models.IntegerField(default=0)
    trimestre_2 = models.IntegerField(default=0)
    trimestre_3 = models.IntegerField(default=0)


    def __str__(self):
        return str(self.trimestre_1)+str(self.trimestre_2)+str(self.trimestre_3)