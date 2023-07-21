from rest_framework import serializers
from apps.RRHH.models import Department, Position, Attendance, ContractorEmployee, TemporaryEmployee




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

# Tipos de empleados


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorEmployee
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


    """def create(self, validated_data):
        contractor = ContractorEmployee.objects.create(**validated_data)
        return contractor"""
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'identification_number': instance.identification_number,
            'name' : f"{instance.first_name} {instance.last_name}",
            'email' : instance.email,
            'phone' : instance.phone,
            'rut': instance.rut,
            'description': instance.description,
            'payment_type': instance.payment_type,
            'payment_value': instance.payment_value
        }
    

class TemporarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryEmployee
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'identification_number': instance.identification_number,
            'name' : f"{instance.first_name} {instance.last_name}",
            'email' : instance.email,
            'phone' : instance.phone,
            'description': instance.description,
            'payment_type': instance.payment_type,
            'payment_value': instance.payment_value
        }