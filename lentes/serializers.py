from rest_framework import serializers 
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
                  'email',
                  'fecha_compra')