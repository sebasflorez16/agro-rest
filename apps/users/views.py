from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.sessions.models import Session
from datetime import datetime
from apps.users.api.serializers import UserSerializerToken
from rest_framework import status



class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)# el user es un field dentro del modelo token
                user_serializer = UserSerializerToken(user) #Del mismo modelo del token
                if created: # Validamos si se ha creado el token
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso'
                }, status = status.HTTP_200_OK)

                else: # Elimina el token por seguridad si se trata de volver a iniciar sesión
                    token.delete()
                    return Response({
                        'error': 'Ya se ha iniciado sesion con esta cuenta'
                    }, status = status.HTTP_409_CONFLICT)

            else:
                return Response({'error': 'Este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'Error': 'El usuario o la contraseña son invalidos'}, status = status.HTTP_400_BAD_REQUEST)

        return Response({'mensaje':'Desde Response'}, status = status.HTTP_200_OK)


class Logout(APIView):
    def post(self,request, *args, **kwargs):

        try:
            token = request.GET.get('token')
            print(token)
            token = Token.objects.filter(key = token).first()

            
            if token:
                user = token.user # Valida dentro del modelo si hay un usuario a ese token

                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())#Borra todas las sesiones del usuario segun el tiempo que se le indique
                if all_sessions.exists(): # Verifica si hay mas sesiones que la actual
                    for session in all_sessions:
                        session_data = session.get_decoded() # Decodifica la sesion encontrada
                        if user.id == int(session_data.get('_auth_user_id')): # Verifica si el user coincide con la data de la sesion
                            session.delete()

                token.delete()

                session_message = f"Las sesiones del usuario {user.username} han sido eliminadas"
                token_message = 'Token eliminado'
                return Response({'session_message':session_message, 'token_message':token_message},
                                status=status.HTTP_200_OK)
            
            return Response({'error':'No se ha encontrado usuario con estas credenciales'},
                                status = status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error':'No se ha encontrado token'},
                                status = status.HTTP_409_CONFLICT)   
