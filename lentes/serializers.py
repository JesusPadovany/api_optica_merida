# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from lentes.models import Marca, TipoLente, Lente, Compra, Usuario
 
 
class TipoLenteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TipoLente
        fields = ('id',
                  'tipo_lente')

class MarcaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Marca
        fields = ('id',
                  'nombre_marca')

class LenteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Lente
        fields = ('id',
                  'idtipo_lente',
                  'idmarcas',
                  'cantidad_total',
                  'descripcion',
                  'codigo',
                  'foto',
                  'precio')

class CompraSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Compra
        fields = ('id',
                  'idinventario',
                  'cantidad',
                  'fecha_compra')

class UsuarioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Usuario
        fields = ('id',
                  'username',
                  'nombres',
                  'apellidos',
                  'email')

class UsuarioLoginSerializer(serializers.ModelSerializer):
# Campos que vamos a requerir
    username = serializers.CharField(min_length=4, max_length=64)
    password = serializers.CharField(min_length=8, max_length=64)

    class Meta:
        model = Usuario
        fields = ('id',
                  'username',
                  'password')


    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class UsuarioSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )

    direccion = serializers.CharField(max_length=250, required=False)
    
    numero_tarjeta = serializers.CharField(max_length=250, required=False)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Debes introducir un número con el siguiente formato: +999999999. El límite son de 15 dígitos."
    )
    telefono = serializers.CharField(validators=[phone_regex], required=False)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    nombres = serializers.CharField(min_length=2, max_length=50)
    apellidos = serializers.CharField(min_length=2, max_length=100)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = Usuario.objects.create_user(**data)
        return user