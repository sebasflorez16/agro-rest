from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.RRHH.api.serializers.employee_serializer import EmployeeSerializer
from apps.RRHH.api.serializers.serializers import ContractorSerializer, TemporarySerializer
from apps.users.authentication_mixins import Authentication



class EmployeeViewSet(Authentication, ModelViewSet):
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
    
class ContractorViwSet(Authentication, ModelViewSet):
    serializer_class =ContractorSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request, *args, **kwargs):
        contractor_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(contractor_serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        contractor_serializer = self.serializer_class(data = request.data)
        if contractor_serializer.is_valid():
            contractor_serializer.save()
            return Response({'message':'Contratista creado correctamente'}, status= status.HTTP_200_OK)
        return Response(contractor_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        


    
class TemporaryViewSet(viewsets.ModelViewSet):
    serializer_class = TemporarySerializer


    def retrieve(self, request, pk = None, *args, **kwargs):
        instance = self.get_queryset(pk)
        if instance is None:
            return Response({'message': 'Registro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        temporary_serializer = self.serializer_class(instance)
        return Response(temporary_serializer.data, status=status.HTTP_200_OK)
    


    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()


    def list(self, request, *args, **kwargs):
        contractor_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(contractor_serializer.data, status = status.HTTP_200_OK)


    def update(self, request, pk= None):
        if self.get_queryset(pk):
            temporary_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if temporary_serializer.is_valid():
                temporary_serializer.save()
                return Response({'message': 'Registro actualizado', 'data':temporary_serializer.data}, status= status.HTTP_200_OK)
            return Response({'message': 'Empleado no encontrado'}, status= status.HTTP_400_BAD_REQUEST)

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Empleado temporal creado correctamente"}, status=status.HTTP_201_CREATED, headers=headers)