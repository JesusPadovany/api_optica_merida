from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos, telefono, direccion, numero_tarjeta, password = None):
        if not email:
            raise ValueError('El usuariodebe tener un correo electronico')
        usuario = self.model(
            email = self.normalize_email(email),
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            direccion = direccion,
            telefono = telefono,
            numero_tarjeta = numero_tarjeta
        )
        usuario.set_password(password)
        usuario.save()
        return Usuario
        
    def create_superuser(self, email, username, nombres, apellidos, telefono, direccion, numero_tarjeta, password):
        usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            direccion = direccion,
            telefono = telefono,
            numero_tarjeta = numero_tarjeta
        )
        usuario.is_active = True
        usuario.save()
        return usuario
class Usuario(AbstractBaseUser):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField(max_length = 255, unique = True)
    numero_tarjeta = models.CharField(max_length = 255)
    direccion = models.CharField(max_length = 255)
    telefono = models.CharField(max_length = 30)
    nombres = models.CharField(max_length = 75)
    apellidos = models.CharField(max_length = 75)
    is_admin =  models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return "{}".format(self.email)

    @property
    def is_staff(self):
        return self.is_admin
class TipoLente(models.Model):
    tipo_lente = models.CharField(max_length = 255)


class Marca(models.Model):
    nombre_marca = models.CharField(max_length = 255)

class Lente(models.Model):
    idtipo_lente = models.ForeignKey(TipoLente, on_delete=models.CASCADE)
    idmarcas = models.ForeignKey(Marca, on_delete=models.CASCADE)
    cantidad_total = models.IntegerField()
    descripcion = models.CharField(max_length = 255)
    codigo = models.CharField(max_length = 255)
    foto = models.CharField(max_length = 255)
    precio = models.FloatField()

# class Carrito(models.Model):
#     idusuario
#     idlente,

class Compra(models.Model):
    #idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idinventario = models.ForeignKey(Lente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_compra = models.DateField()