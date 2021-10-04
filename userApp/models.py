from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, username, nombres, apellidos, password):
        
        usuario = self.model(
            username = username,
            nombres = nombres,
            apellidos = apellidos
            )

        usuario.set_password(password)
        usuario.save()

        return usuario

    def create_superuser(self, username, nombres, apellidos, password):
        
        usuario = self.create_user(
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password = password
            )

        usuario.usuario_admin = True
        usuario.save()

        return usuario

    def create_docenteuser(self, username, nombres, apellidos, password):
        
        usuario = self.model(
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password = password
            )

        usuario.usuario_docente = True
        usuario.save()

        return usuario

    def create_alumnouser(self, username, nombres, apellidos, password):
        
        usuario = self.model(
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password = password
            )

        usuario.usuario_alumno = True
        usuario.save()

        return usuario


class Usuario(AbstractBaseUser):
    username = models.IntegerField(unique= True ,default=0)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    usuario_activo = models.BooleanField(default=True)
    usuario_admin = models.BooleanField(default=False)
    usuario_docente = models.BooleanField(default=False)
    usuario_alumno = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    

    def __str__(self) -> str:
        return str(self.username) + ", " + self.nombres+ ", " + self.apellidos

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_admin


