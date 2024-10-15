from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.crop.models import *
from apps.crop.serializers.crop_serializers import *
# Create your views here.


class AgricultureWorkViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = AgricultureWork
    serializer_class = AgricultureWorkSerializer

class AgriculturalApplicationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = AgriculturalApplication
    serializer_class = AgricultureApplicationSerializer

class CropViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = Crop
    serializer_class = CropSerializer

class StateLotViewSet(ModelViewSet):
    

    model = StateLot
    serializer_class = StateLotSerializer

class LotViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = Lot
    serializer_class = LotSerializer

