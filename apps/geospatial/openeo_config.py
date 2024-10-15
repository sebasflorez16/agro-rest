# geospatial/views.py

from django.shortcuts import HttpResponse
from openeo_config import OpenEOConfig
from openeo.rest import OpenEoApi

# Crear una instancia del cliente openEO
openeo_client = OpenEoApi(OpenEOConfig.SERVER_URL, auth=(OpenEOConfig.USERNAME, OpenEOConfig.PASSWORD))

def descargar_datos(request):
    # Aquí puedes usar el cliente openEO para descargar datos
    # Ejemplo: openeo_client.download(nombre_archivo)
    return HttpResponse("Datos descargados correctamente.")

def ejecutar_proceso(request):
    # Aquí puedes usar el cliente openEO para ejecutar un proceso
    # Ejemplo: openeo_client.execute_process(proceso)
    return HttpResponse("Proceso ejecutado correctamente.")
