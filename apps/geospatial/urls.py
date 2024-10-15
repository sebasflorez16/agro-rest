# urls.py
from django.urls import path
from apps.geospatial.geo_api.views.views import FetchNDVIView

urlpatterns = [
    path('api/fetch_ndvi/', FetchNDVIView.as_view(), name='geo-data'),
]
