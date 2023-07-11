from django.contrib import admin
from .models import OrganizationEmployeeRole

class OrganizationEmloyeeRoleAdmin(admin.ModelAdmin):
    list_display = ('employee_id','organization_id','employee_role','created_on')


admin.site.register(OrganizationEmployeeRole,  OrganizationEmloyeeRoleAdmin)
