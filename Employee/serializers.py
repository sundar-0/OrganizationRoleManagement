from rest_framework import serializers
from . models import EmployeeModel
from OrganizationEmployeeRole.serializers import OrganizationEmployeeRoleSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ('email','employee_first_name','employee_last_name','employee_contact_no','employee_address','is_active','is_admin')
    

   