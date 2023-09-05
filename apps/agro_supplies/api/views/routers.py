from rest_framework.routers import DefaultRouter
from apps.agro_supplies.api.views.supplies import SeedVarietyViewSet

router = DefaultRouter()

router.register(r'seeds', SeedVarietyViewSet, basename='seeds')

urlpatterns = router.urls
