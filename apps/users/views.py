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
        # Utiliza el serializer para validar y obtener el token
        serializer = self.get_serializer(data=request.data)
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
