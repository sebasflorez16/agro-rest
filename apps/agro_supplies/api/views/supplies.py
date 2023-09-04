from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse

from apps.agro_supplies.models import Variety
from apps.agro_supplies.api.seed_serializers.serializers import SeedSerializer
from apps.users.authentication_mixins import Authentication


class SeedVarietyViewSet(ModelViewSet):
    queryset = Variety.objects.all()
    serializer_class = SeedSerializer

    #from django.http import JsonResponse


    """def create(self, request):
        file_name = 'seeds.json'
        try:
            with open(file_name, 'r', encoding='utf-8') as seed_file:
                try:
                    seed_data_list = json.load(seed_file)
                except json.JSONDecodeError as e:
                    return JsonResponse({"error": "Invalid JSON format in the file."}, status=400)

                for seed_data in seed_data_list:
                    serializer = self.serializer_class(data=seed_data['fields'])
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return JsonResponse({'message': 'Variedades de semillas creadas correctamente'}, status=200)
        except FileNotFoundError:
            return JsonResponse({"error": "File not found."}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An error occurred while processing the file."}, status=500)"""
