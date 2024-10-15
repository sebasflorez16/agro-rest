
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
import json
from apps.agro_supplies.models import *
from apps.agro_supplies.api.seed_serializers.serializers import *
from rest_framework.permissions import IsAuthenticated


# Se crea este script para la lectura de archivos json grandes
class SeedVarietyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

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

<<<<<<< HEAD
        return Response({'detail': 'Objetos Variety creados exitosamente'}, status=status.HTTP_201_CREATED)


class CompanyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = Company
    serializer_class = CompanySerializer

class SupplierViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = Supplier
    serializer_class = SupplierSerializer

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = Category
    serializer_class = CategorySerializer

class SubcategoryViewSet(ModelViewSet):
    permission_classes =  [IsAuthenticated]

    model = SubCategory
    serializer_class = SubcategorySerializer

class WarehouseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = Warehouse
    serializer_class = WarehouseSerializer

class SupplyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = Supply
    serializer_class = SupplySerializer

class CategoryEquipmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = CategoryEquipment
    serializer_class = CategoryEquipmentSerializer

class SubcategoryEquipmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = SubcategoryEquipment
    serializer_class = SubcategoryEquipmentSerializer

class ToolAndEquipmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = ToolAndEquipment
    serializer_class = ToolAndEquipmentSerializer

class ToolAssigmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    model = ToolAssignment
    serializer_class = ToolAssignmentSerializer
=======
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
>>>>>>> 8966b7d547f86cf55078118fc0a98a93b8d4ef45
