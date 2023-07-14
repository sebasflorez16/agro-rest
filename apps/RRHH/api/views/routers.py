from django.db import router
from rest_framework.routers import DefaultRouter
from apps.RRHH.api.views.general_views import *
from apps.RRHH.api.views.employee_viewsets import EmployeeViewSet

router = DefaultRouter()

router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'department', DepartmentViewSet, basename= 'department')
router.register(r'position', PositionViewSet, basename= 'position')
router.register(r'attendance', AttendanceViewSet, basename= 'attendance')


urlpatterns = router.urls
