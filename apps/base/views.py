from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view, permission_classes


# Create your views here.

permission_classes = [IsAuthenticated]
@api_view(['GET'])
def dashboard(request):
    return render(request, 'dashboard/helpdesk.html')