from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
import json
from apps.agro_supplies.models import Variety
from apps.agro_supplies.api.seed_serializers.serializers import SeedSerializer
from apps.users.authentication_mixins import Authentication


class SeedVarietyViewSet(ModelViewSet, Authentication):
    queryset = Variety.objects.all()
    serializer_class = SeedSerializer

    def create(self, request, *args, **kwargs):
        # Ruta al archivo JSON en tu proyecto
        json_file_path = 'apps/agro_supplies/api/views/fixtures/seeds.json'

        try:
            # Abre y lee el archivo JSON desde la ubicación del proyecto
            with open(json_file_path, 'r') as json_file:
                seeds_data = json.load(json_file)
        except FileNotFoundError:
            return Response({'detail': 'El archivo JSON no se encontró'}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError:
            return Response({'detail': 'El archivo JSON es inválido'}, status=status.HTTP_400_BAD_REQUEST)

        # Itera a través de los objetos en el archivo JSON y crea instancias de Variety
        for seed_data in seeds_data:
            serializer = SeedSerializer(data=seed_data['fields'])
            """nombre = seed_data['fields']['name']
            healt = seed_data['fields']['health']
            info = f'{nombre}, {healt}'
            print(info)"""
            if serializer.is_valid():
                serializer.save()

        return Response({'detail': 'Objetos Variety creados exitosamente'}, status=status.HTTP_201_CREATED)
