from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializerToken(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agrega información adicional que quieras incluir en el token
        token['username'] = user.username
        token['email'] = user.email
        token['name'] = user.name
        token['last_name'] = user.last_name

        return token

    def validate(self, attrs):
        # Llama a la validación original del TokenObtainPairSerializer
        data = super().validate(attrs)

        # Obtiene información adicional del usuario
        user_data = UserSerializerToken(self.user).data

        # Agrega información del usuario a la respuesta
        data.update({
            'user': user_data
        })

        return data


class UserSerializer(TokenObtainPairSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class UserListSerializer(serializers.ModelSerializer):
    Model = User

    def to_representation(self, instance):
        super().to_representation(instance)
        print(instance)
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email']
        }
