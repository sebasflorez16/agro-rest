# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.geospatial.models import Lot, Study, Ndvi
from apps.geospatial.serilaizers.geo_serializers import LotSerializer, StudySerializer, NdviSerializer
from apps.geospatial.geo_api.api import get_ndvi_data
from django.utils import timezone

class FetchNDVIView(APIView):
    def post(self, request):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        coordinates = request.data.get('coordinates')
        
        try:
            ndvi_data = get_ndvi_data(coordinates, start_date, end_date)
            
            # Crear un nuevo lote si no existe
            lot, created = Lot.objects.get_or_create(
                ubication='POINT({} {})'.format(coordinates[0], coordinates[1]),
                defaults={'name': 'Lote {}'.format(Lot.objects.count() + 1)}
            )

            # Crear un nuevo estudio
            study = Study.objects.create(
                lot=lot,
                timestamp=timezone.now().date(),
                time=timezone.now().time()
            )
            
            # Crear el registro NDVI
            ndvi_result = Ndvi.objects.create(
                study=study,
                value=ndvi_data['value'],
                spatial_resolution=ndvi_data['spatial_resolution'],
                sensor=ndvi_data['sensor'],
                red_band=ndvi_data['red_band'],
                nir_band=ndvi_data['nir_band'],
                processed_image=ndvi_data['processed_image']
            )
            
            response_data = NdviSerializer(ndvi_result).data
            return Response(response_data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
