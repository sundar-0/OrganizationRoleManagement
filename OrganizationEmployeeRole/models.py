from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import Group

from Employee.models import EmployeeModel

from Organization.models import Organization

class OrganizationEmployeeRole(models.Model):
    employee_id=models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='emp_id')
    organization_id=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='org_id')
    employee_role=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='role')
    created_on=models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.organization_id) 

