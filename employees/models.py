from django.db import models
from django.urls import reverse
from companies.models import Company

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, default=1)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})