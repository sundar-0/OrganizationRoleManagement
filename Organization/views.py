from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions

from . serializers import OrganizationSerializer

from . models import Organization

from . permissions import isEmployeeAdminOrReadOnly
from rest_framework import serializers
# Create your views here.
class OrganizationViewSet(viewsets.ModelViewSet):
    """Organization"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,isEmployeeAdminOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_admin==True: 
            serializer.save()
        else:
            raise serializers.ValidationError({"message":"You don't have permission to add."})
                      
