from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from lentes.models import Lente, TipoLente, Marca
from lentes.serializers import LenteSerializer, MarcaSerializer, TipoLenteSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def lentes_list(request):
    # GET list of lentes, POST a new lentes, DELETE all lentes
    if request.method == 'GET':
        lentes = Lente.objects.all()
        
        # descripcion = request.GET.get('descripcion', None)
        # if descripcion is not None:
        #     lentes = lentes.filter(descripcion__icontains=descripcion)
        
        lentes_serializer = LenteSerializer(lentes, many=True)
        return JsonResponse(lentes_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        lente_data = JSONParser().parse(request)
        lente_serializer = LenteSerializer(data=lente_data)
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
            lente_serializer = TutorialSerializer(lente) 
            return JsonResponse(lente_serializer.data) 

        elif request.method == 'PUT': 
            lente_data = JSONParser().parse(request) 
            lente_serializer = TutorialSerializer(lente, data=lente_data) 
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
            lente_tipo_serializer = TutorialSerializer(lente_tipo) 
            return JsonResponse(lente_tipo_serializer.data) 

        elif request.method == 'PUT': 
            lente_tipo_data = JSONParser().parse(request) 
            lente_tipo_serializer = TutorialSerializer(lente_tipo, data=lente_tipo_data) 
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
            marca_serializer = TutorialSerializer(marca) 
            return JsonResponse(marca_serializer.data) 

        elif request.method == 'PUT': 
            marca_data = JSONParser().parse(request) 
            marca_serializer = TutorialSerializer(marca, data=marca_data) 
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