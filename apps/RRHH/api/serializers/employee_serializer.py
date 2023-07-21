from rest_framework import serializers
from apps.RRHH.models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    
    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee


    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'identification_number': instance.identification_number,
            'name' : f"{instance.name} {instance.last_name}",
            'email' : instance.email,
            'phone' : instance.phone,
            'image' : instance.image if instance.image != instance.image else '',
            'salary' : int(instance.salary),
            'department' : instance.department.name if instance.department is not None else '',
            'position' : instance.position.name if instance.position is not None else '',
        }
    
