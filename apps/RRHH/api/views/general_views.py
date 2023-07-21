from rest_framework import viewsets

from apps.RRHH.api.serializers.serializers import *
from apps.RRHH.models import *





class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.filter(state = True)


class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer

