#Creamos la funcion para la vista
import openeo
from apps.geospatial.models import *
from django.utils import timezone


def get_ndvi_data(cordinates, start_date, end_date): #Estos datos los recibe desde el front
    #Conectamos con OpenEO
    connection = openeo.connect(
        "openeo.vito.be"
        ).authenticate_oidc()
    
    bbox = {
        "west":  5.26072252824706,
        "south": 51.15104749829274,
        "east": 5.287988791144827,
        "north": 51.16575171816709
        } 
    
    #Creamos el datacube

    datacube = connection.load_collection(
                      "SENTINEL2_L2A",)\
                      .filter_bbox(**bbox)\
                      .filter_temporal(start_date, end_date)\
                      .ndvi()

    job = datacube.create_job()
    job.start_and_wait()
    result = job.download_result()

    # Procesar los resultados y extraer la información necesaria
    ndvi_value = ...  # Aquí se extrae el valor de NDVI del resultado
    spatial_resolution = ...  # Extraer resolución espacial
    sensor = ...  # Extraer el sensor utilizado
    red_band = ...  # Extraer la banda roja
    nir_band = ...  # Extraer la banda NIR
    processed_image = ...  # Extraer la imagen procesada

    return {
        'value': ndvi_value,
        'spatial_resolution': spatial_resolution,
        'sensor': sensor,
        'red_band': red_band,
        'nir_band': nir_band,
        'processed_image': processed_image
    }
