from rest_framework import serializers
from apps.agro_supplies.models import *


class SeedSerializer(serializers.ModelSerializer):
    siembra = serializers.JSONField()
    herbicide_susceptibility = serializers.JSONField()
    health = serializers.JSONField()
    nutrition = serializers.JSONField()

    class Meta:
        model = Variety
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'lote': instance.lote,
            'ica_producer_record': instance.ica_producer_record
        }

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name' : instance.name,
            'rut': instance.rut
        }

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'company': instance.self.company
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name
        }

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name
        }

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'manager': instance.manager
        }
    
class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'stock': instance.stock
        }
    
class CategoryEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEquipment
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name
        }
    

class SubcategoryEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcategoryEquipment
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name
        }
    

class ToolAndEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolAndEquipment
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'amount': instance.amount,
            'state': instance.state,
            'store': instance.store
        }
    
class ToolAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolAssignment
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'tool': instance.tool,
            'estado': instance.estado
        }