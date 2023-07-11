from django.db import models

# Create your models here.
from django.db import models

class Organization(models.Model):
    organization_name=models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    organization_type = models.CharField(max_length=100)
    no_of_employee = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=100)
    registration_date = models.DateField()
    organization_setup_date = models.DateField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.organization_name
