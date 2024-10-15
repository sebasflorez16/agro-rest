from rest_framework import serializers
from apps.crop.models import *



class AgricultureWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureWork
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'manager': instance.manager,
            'status': instance.state
        }
    

class AgricultureApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalApplication
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id
        }


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'common_name': instance.common_name,
            'variety': instance.variety,
            'crop_cycle': instance.crop_cycle,
            'planting_time': instance.planting_time,
            'state': instance.state,
            'agriculture_work': [work.name for work in instance.agriculture_work.all()]# Lista de labores agricolas que se han hecho en el cultivo
        }
    
class StateLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateLot
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title
        }
    
class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'
    
    def to_representation(self, instance):
        #Verifica en la DB si hay un cultivo asignado para este lote
        crop = instance.crop.name if instance.crop else 'No hay cultivo asignado a este lote'

        return {
            'id': instance.id,
            'name': instance.name,
            'manager': instance.name,
            'crop': crop,
            'state': instance.state,
            'agriculture_work': [work.name for work in instance.agriculture_work.all()] #Muestra la lista de labores agricolas que se han relizado en el lote.
        }