from rest_framework import serializers
from apps.RRHH.models import Department, Position, Attendance




class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
        return department
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name, 
            'description': instance.description
        }

        


class PositionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Position
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date') 


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')