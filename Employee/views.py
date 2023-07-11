from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions

from . serializers import EmployeeSerializer

from . models import EmployeeModel

from Organization. permissions import isEmployeeAdminOrReadOnly
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from OrganizationEmployeeRole.serializers import OrganizationEmployeeRoleSerializer
from OrganizationEmployeeRole.models import OrganizationEmployeeRole
from django.http import Http404
from rest_framework.parsers import JSONParser
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    """Employee Model"""
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,isEmployeeAdminOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_admin==True: 
            serializer.save()
        else:
            raise serializers.ValidationError({"message":"You don't have permission to add."})
        

                      
    @action(detail=True, methods=['get'])
    def get_role(self, request, pk=None):
        try:
            employee_role = OrganizationEmployeeRole.objects.get(employee_id=pk)
            serializer = OrganizationEmployeeRoleSerializer(employee_role)
            return Response(serializer.data)
        except OrganizationEmployeeRole.DoesNotExist:
            raise Http404
        
    @action(detail=True,methods=['put'])
    def update_role(self,request,pk):
        try:
            employee_role = OrganizationEmployeeRole.objects.get(employee_id=pk)
            serializer = OrganizationEmployeeRoleSerializer(employee_role,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)  
        except OrganizationEmployeeRole.DoesNotExist:
            raise Http404


        
        