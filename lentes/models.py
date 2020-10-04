from django.db import models

DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Create your models here.

# class Usuario(models.Model):
#     username = models.CharField(max_length = 255)
#     password,
#     email = models.CharField(max_length = 255)
#     numero_tarjeta = models.CharField(max_length = 255)
#     direccion = models.CharField(max_length = 255)
#     telefono = models.CharField(max_length = 30)
#     nombres = models.CharField(max_length = 75)
#     apellidos = models.CharField(max_length = 75)

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