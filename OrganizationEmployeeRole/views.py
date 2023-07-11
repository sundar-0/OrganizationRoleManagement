from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from . serializers import OrganizationEmployeeRoleSerializer,GroupSerializer
from . models import OrganizationEmployeeRole
from Organization.permissions import isEmployeeAdminOrReadOnly
from rest_framework import serializers
from django.contrib.auth.models import Group
# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,isEmployeeAdminOrReadOnly]



class OrganizationEmployeeRoleViewSet(viewsets.ModelViewSet):
    """Organization Employee Role"""
    queryset = OrganizationEmployeeRole.objects.all()
    serializer_class = OrganizationEmployeeRoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,isEmployeeAdminOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_admin==True: 
            serializer.save()
        else:
            raise serializers.ValidationError({"message":"You don't have permission to add."})
                      
