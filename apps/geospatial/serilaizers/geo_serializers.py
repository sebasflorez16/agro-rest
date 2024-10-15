from rest_framework import serializers
from apps.geospatial.models import *



class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'


class NdviSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ndvi
        fields = '__all__'

