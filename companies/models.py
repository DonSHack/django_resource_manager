from django.db import models
from django.urls import reverse
from PIL import Image

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company', blank=True)
    email = models.EmailField()
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})
