from rest_framework import serializers
from . models import OrganizationEmployeeRole

from django.contrib.auth.models import User, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"



class OrganizationEmployeeRoleSerializer(serializers.ModelSerializer):
    employee_id = serializers.ReadOnlyField(source='employee_id.employee_first_name')
    organization_id=serializers.ReadOnlyField(source='organization_id.organization_name')
    employee_role=serializers.ReadOnlyField(source='employee_role.name')

    class Meta:
        model = OrganizationEmployeeRole
        fields = ('employee_id','organization_id','employee_role','created_on')