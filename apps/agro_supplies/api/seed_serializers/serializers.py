from rest_framework import serializers
from apps.agro_supplies.models import Variety


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
