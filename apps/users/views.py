from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from apps.users.api.serializers import CustomTokenObtainPairSerializer
from rest_framework import status



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer  # Asegúrate de que la clase sea la correcta
    
    def get(self, request, *args, **kwargs):
        # Renderiza la plantilla HTML del login
        return render(request, 'authentication/auth-login-alt.html')

    def post(self, request, *args, **kwargs):
<<<<<<< HEAD
        # Utiliza el serializer para validar y obtener el token
        serializer = self.get_serializer(data=request.data)
=======
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

    


class Logout(APIView):
    def post(self,request, *args, **kwargs):

>>>>>>> 8966b7d547f86cf55078118fc0a98a93b8d4ef45
        try:
            serializer.is_valid(raise_exception=True)  # Valida el serializer

            # Extrae datos de la respuesta
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'Error': 'El usuario o la contraseña son inválidos'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Obtiene el token del encabezado de autorización
            token = request.auth
            # Agrega el token a la lista negra
            OutstandingToken.objects.filter(token=token).update(blacklisted=True)

            return Response({"message": "Logout exitoso"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
