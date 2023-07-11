from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name','contact_person', 'organization_type', 'registration_number', 'country', 'state', 'city')
    list_filter = ('organization_type', 'country')
    search_fields = ('contact_person', 'registration_number', 'country', 'state', 'city')
    ordering = ('contact_person',)

admin.site.register(Organization, OrganizationAdmin)
