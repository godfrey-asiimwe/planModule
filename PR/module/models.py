from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    description = models.CharField(max_length=1000,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=255,null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        return self.name
