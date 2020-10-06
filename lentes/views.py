from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.models import F
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from lentes.models import Lente, TipoLente, Marca, Usuario, Compra
from lentes.serializers import LenteSerializer, LentePostSerializer, MarcaSerializer, TipoLenteSerializer, UsuarioSerializer, UsuarioLoginSerializer, UsuarioSignUpSerializer, CompraSerializer

class UsuarioViewSet(viewsets.GenericViewSet):

    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """Usuario sign in."""
        serializer = UsuarioLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UsuarioSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UsuarioSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UsuarioSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'DELETE'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def lentes_list(request):
    # GET list of lentes, POST a new lentes, DELETE all lentes
    if request.method == 'GET':
        lentes = Lente.objects.all()
        
        marca = request.GET.get('marca', None)
        lentes = lentes.filter(cantidad_total__gte = 0)
        if marca is not None:
            lentes = lentes.filter(marca__icontains=marca)
        lentes.values('marca', 'tipo_lente')
        lentes_serializer = LenteSerializer(lentes, many=True)
        return JsonResponse(lentes_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        lente_data = JSONParser().parse(request)
        lente_serializer = LentePostSerializer(data=lente_data)
        if lente_serializer.is_valid():
            lente_serializer.save()
            return JsonResponse(lente_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(lente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Lente.objects.all().delete()
        return JsonResponse({'message': '{} Lentes eliminado satisfactoriamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def lentes_detail(request, pk):
    # find lente by pk (id)
    try: 
        lente = Lente.objects.get(pk=pk) 
        
        if request.method == 'GET': 
            lente_serializer = LenteSerializer(lente) 
            return JsonResponse(lente_serializer.data) 

        elif request.method == 'PUT': 
            lente_data = JSONParser().parse(request) 
            lente_serializer = LentePostSerializer(lente, data=lente_data) 
            if lente_serializer.is_valid(): 
                lente_serializer.save() 
                return JsonResponse(lente_serializer.data) 
            return JsonResponse(lente_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            lente.delete() 
            return JsonResponse({'message': 'Lente eliminado de manera satisfactoria!'}, status=status.HTTP_204_NO_CONTENT)

    except Lente.DoesNotExist: 
        return JsonResponse({'message': 'No existe el lente solicitado'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    # GET / PUT / DELETE lentes

    
@api_view(['GET', 'POST', 'DELETE'])
def lente_tipos_list(request):
    # GET list of lentes, POST a new lentes, DELETE all lentes
    if request.method == 'GET':
        lentes_tipos = TipoLente.objects.all()
        
        # descripcion = request.GET.get('descripcion', None)
        # if descripcion is not None:
        #     lentes_tipos = lentes_tipos.filter(descripcion__icontains=descripcion)
        
        lente_tipos_serializer = TipoLenteSerializer(lentes_tipos, many=True)
        return JsonResponse(lente_tipos_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        lente_tipo_data = JSONParser().parse(request)
        lente_tipo_serializer = TipoLenteSerializer(data=lente_tipo_data)
        if lente_tipo_serializer.is_valid():
            lente_tipo_serializer.save()
            return JsonResponse(lente_tipo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(lente_tipo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = TipoLente.objects.all().delete()
        return JsonResponse({'message': '{} Tipos de lentes eliminado satisfactoriamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def lente_tipos_detail(request, pk):
    # find lente by pk (id)
    try: 
        lente_tipo = TipoLente.objects.get(pk=pk) 
        
        if request.method == 'GET': 
            lente_tipo_serializer = TipoLenteSerializer(lente_tipo) 
            return JsonResponse(lente_tipo_serializer.data) 

        elif request.method == 'PUT': 
            lente_tipo_data = JSONParser().parse(request) 
            lente_tipo_serializer = TipoLenteSerializer(lente_tipo, data=lente_tipo_data) 
            if lente_tipo_serializer.is_valid(): 
                lente_tipo_serializer.save() 
                return JsonResponse(lente_tipo_serializer.data) 
            return JsonResponse(lente_tipo_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            lente_tipo.delete() 
            return JsonResponse({'message': 'Tipo de lente eliminado de manera satisfactoria!'}, status=status.HTTP_204_NO_CONTENT)

    except TipoLente.DoesNotExist: 
        return JsonResponse({'message': 'No existe el tipo de lente solicitado'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    # GET / PUT / DELETE lentes_tipos

   
@api_view(['GET', 'POST', 'DELETE'])
def marcas_list(request):
    # GET list of lentes, POST a new lentes, DELETE all lentes
    if request.method == 'GET':
        marcas = Marca.objects.all()
        
        # descripcion = request.GET.get('descripcion', None)
        # if descripcion is not None:
        #     marcas = marcas.filter(descripcion__icontains=descripcion)
        
        marcas_serializer = MarcaSerializer(marcas, many=True)
        return JsonResponse(marcas_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        marca = JSONParser().parse(request)
        lente_serializer = MarcaSerializer(data=marca)
        if lente_serializer.is_valid():
            lente_serializer.save()
            return JsonResponse(lente_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(lente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Marca.objects.all().delete()
        return JsonResponse({'message': '{} Tipos de lentes eliminado satisfactoriamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def marcas_detail(request, pk):
    # find lente by pk (id)
    try: 
        marca = Marca.objects.get(pk=pk) 
        
        if request.method == 'GET': 
            marca_serializer = MarcaSerializer(marca) 
            return JsonResponse(marca_serializer.data) 

        elif request.method == 'PUT': 
            marca_data = JSONParser().parse(request) 
            marca_serializer = MarcaSerializer(marca, data=marca_data) 
            if marca_serializer.is_valid(): 
                marca_serializer.save() 
                return JsonResponse(marca_serializer.data) 
            return JsonResponse(marca_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            marca.delete() 
            return JsonResponse({'message': 'Tipo de lente eliminado de manera satisfactoria!'}, status=status.HTTP_204_NO_CONTENT)

    except Marca.DoesNotExist: 
        return JsonResponse({'message': 'No existe el tipo de lente solicitado'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    # GET / PUT / DELETE marcas

      
@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def usuarios_list(request):
    # GET list of usuarios, POST a new usuarios, DELETE all usuarios
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        
        # descripcion = request.GET.get('descripcion', None)
        # if descripcion is not None:
        #     usuarios = usuarios.filter(descripcion__icontains=descripcion)
        
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        usuario = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Usuario.objects.all().delete()
        return JsonResponse({'message': '{} Usuarios eliminado satisfactoriamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def usuarios_detail(request, pk):
    # find lente by pk (id)
    try: 
        usuario = Usuario.objects.get(pk=pk) 
        
        if request.method == 'GET': 
            usuario_serializer = UsuarioSerializer(usuario) 
            return JsonResponse(usuario_serializer.data) 

        elif request.method == 'PUT': 
            usuario_data = JSONParser().parse(request) 
            usuario_serializer = UsuarioSerializer(usuario, data=usuario_data) 
            if usuario_serializer.is_valid(): 
                usuario_serializer.save() 
                return JsonResponse(usuario_serializer.data) 
            return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            usuario.delete() 
            return JsonResponse({'message': 'Usuario eliminado de manera satisfactoria!'}, status=status.HTTP_204_NO_CONTENT)

    except Usuario.DoesNotExist: 
        return JsonResponse({'message': 'No existe el usuario solicitado'}, status=status.HTTP_404_NOT_FOUND) 
 
    
# GET / PUT / DELETE marcas
@api_view(['GET', 'POST', 'DELETE'])
def compras_list(request):
    # GET list of compras, POST a new compras, DELETE all compras
    if request.method == 'GET':
        compras = Compra.objects.all()
        
        # descripcion = request.GET.get('descripcion', None)
        # if descripcion is not None:
        #     compras = compras.filter(descripcion__icontains=descripcion)
        
        compras_serializer = CompraSerializer(compras, many=True)
        return JsonResponse(compras_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        compra = JSONParser().parse(request)
        id_iventario = compra['inventario'] 
        compra_serializer = CompraSerializer(data=compra)
        print(compra_serializer)
        if compra_serializer.is_valid(): 
                inventario = Lente.objects.get(pk=id_iventario)
                inventario_serializer = LenteSerializer(data=inventario)
                print(inventario)
                print(inventario_serializer)
                if inventario.cantidad_total >= compra['cantidad']:
                    inventario.cantidad_total = inventario.cantidad_total - compra['cantidad']
                    #inventario_serializer.save(inventario.cantidad_total - compra['cantidad'])
                    inventario.save() 
                    compra_serializer.save() 

            # compra_serializer.save()
                return JsonResponse(compra_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(compra_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Compra.objects.all().delete()
        return JsonResponse({'message': '{} Compras eliminado satisfactoriamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def compras_detail(request, pk):
    # find lente by pk (id)
    try: 
        compra = Compra.objects.get(pk=pk) 
        
        if request.method == 'GET': 
            compra_serializer = CompraSerializer(compra) 
            return JsonResponse(compra_serializer.data) 

        elif request.method == 'PUT': 
            compra_data = JSONParser().parse(request) 
            compra_serializer = CompraSerializer(compra, data=compra_data) 
            if compra_serializer.is_valid(): 
                compra_serializer.save() 
                return JsonResponse(compra_serializer.data) 
            return JsonResponse(compra_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            compra.delete() 
            return JsonResponse({'message': 'Compra eliminado de manera satisfactoria!'}, status=status.HTTP_204_NO_CONTENT)

    except Compra.DoesNotExist: 
        return JsonResponse({'message': 'No existe el compra solicitado'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    # GET / PUT / DELETE marcas