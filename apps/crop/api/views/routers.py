from rest_framework.routers import DefaultRouter
from apps.crop.api.views.views import *

router = DefaultRouter()

router.register(r'agriculture-work', AgricultureWorkViewSet, basename='agriculturework')
router.register(r'agriculture-application', AgriculturalApplicationViewSet, basename='application')
router.register(r'crop', CropViewSet, basename='crop')
router.register(r'state-lot', StateLotViewSet, basename='state-lot')
router.register(r'lot', LotViewSet, basename='lot')


urlpatterns = router.urls