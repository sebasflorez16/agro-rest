from rest_framework.routers import DefaultRouter
from apps.agro_supplies.api.views.supplies import *

router = DefaultRouter()

router.register(r'seeds', SeedVarietyViewSet, basename='seeds')
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'subcategory', SubcategoryViewSet, basename='subcategory')
router.register(r'warehouse', WarehouseViewSet, basename='warehouse')
router.register(r'supply', SupplyViewSet, basename='supply')
router.register(r'category-equipment', CategoryEquipmentViewSet, basename='category-equipment')
router.register(r'subcategory-equipment', SubcategoryEquipmentViewSet, basename='subcategory-equipment')
router.register(r'toolandequipment', ToolAndEquipmentViewSet, basename='toolandequipment')
router.register(r'toolassignment', ToolAssigmentViewSet, basename='toolassignment')

urlpatterns = router.urls
