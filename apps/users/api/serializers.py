
from rest_framework import serializers
from apps.users.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fields_to_include = ['id', 'username', 'email']
        return {field: representation[field] for field in fields_to_include}
        
        

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
