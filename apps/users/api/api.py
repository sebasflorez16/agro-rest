from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django_tenants.utils import schema_context
from apps.users.models import User
from rest_framework import status
from apps.users.api.serializers import UserSerializer



@api_view(['GET', 'POST', ])#Especifica cual metodo se va a mostrar en la apiview
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all().values() # Values hace que el serializer devuelva un diccionario si no se pone "TypeError: 'User' object is not subscriptable"
        users_serializer = UserSerializer(users, many=True) #many=True para que el serializer sepa que son varios objetos como la el query de arriba all()
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    #queryset
    user = User.objects.filter(id = pk).first()  #filtra todas las peticiones de los metodos http 1 sola vez la consulta
    if user:

        #List
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        #update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user,data = request.data) # Asi valida para enviar al serializer y actualice
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)#despues de validar devuelve objeto actualizado
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message','Usuario eliminado correctamente!'}, status = status.HTTP_200_OK) #pasar como diccionario cariable 'message' valor 'el mensaje'

    return Response({'message', 'No se encontro ningun usuario'}, status=status.HTTP_400_BAD_REQUEST)