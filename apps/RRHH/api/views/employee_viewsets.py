from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.RRHH.api.serializers.employee_serializer import EmployeeSerializer
from apps.users.authentication_mixins import Authentication



class EmployeeViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Empleado creado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk = None):
        employee = self.get_queryset().filter(id = pk).first()
        if employee.state == True:
            employee.state = False
            employee.save()
            return Response({'message': 'Empleado desactivado correctamente'}, status= status.HTTP_200_OK)
        return Response({'message': 'El empleado no ha sido encontrado o ya esta desactivado'}, status= status.HTTP_409_CONFLICT)

    def update(self, request, pk= None):
        if self.get_queryset(pk):
            employee_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return Response(employee_serializer.data, status= status.HTTP_200_OK)
            return Response({'message': 'Empleado no encontrado'}, status= status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        employee_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(employee_serializer.data, status = status.HTTP_200_OK)


    
    
