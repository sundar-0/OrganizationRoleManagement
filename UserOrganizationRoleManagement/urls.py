from django.contrib import admin
from django.urls import path,include
from Organization.views import OrganizationViewSet
from OrganizationEmployeeRole.views import OrganizationEmployeeRoleViewSet,GroupViewSet
from Employee.views import EmployeeViewSet

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'organizations', OrganizationViewSet,basename='organizations')
router.register(r'employees',EmployeeViewSet,basename='employees')
router.register(r'roles',OrganizationEmployeeRoleViewSet,basename='roles')
router.register(r'groups',GroupViewSet,basename='groups')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns=urlpatterns+router.urls