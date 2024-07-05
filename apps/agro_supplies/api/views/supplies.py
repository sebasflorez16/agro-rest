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
        # Verifica si se proporciona un archivo JSON o un solo objeto JSON
        if 'application/json' in request.content_type:
            # Si es un solo objeto JSON, crea una instancia
            serializer = SeedSerializer(data=request.data)
            if serializer.is_valid():
                instance = Variety.objects.create(**serializer.validated_data)
                return Response({'detail': 'Instancia Variety creada exitosamente'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'Datos JSON inválidos'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Si es un archivo JSON, lee y crea instancias desde el archivo
            json_file_path = 'apps/agro_supplies/api/views/fixtures/seeds.json'
            try:
                with open(json_file_path, 'r') as json_file:
                    seeds_data = json.load(json_file)
            except FileNotFoundError:
                return Response({'detail': 'El archivo JSON no se encontró'}, status=status.HTTP_404_NOT_FOUND)
            except json.JSONDecodeError:
                return Response({'detail': 'El archivo JSON es inválido'}, status=status.HTTP_400_BAD_REQUEST)

            created_varieties = []
            for seed_data in seeds_data:
                serializer = SeedSerializer(data=seed_data['fields'])
                if serializer.is_valid():
                    instance, created = Variety.objects.get_or_create(**serializer.validated_data)
                    if created:
                        created_varieties.append(instance)
                    else:
                        # Puedes manejar el caso de instancias similares existentes aquí
                        print(f'Instancia similar ya existe para {serializer.validated_data}')

            return Response({'detail': 'Objetos Variety creados exitosamente', 'created_varieties': created_varieties}, status=status.HTTP_201_CREATED)