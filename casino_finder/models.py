# from django.db import models
from django.contrib.gis.db import models #once installed postgis add this

# Create your models here.
class Casino(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    location = models.PointField(null = True, blank= True) #once installed postgis add this
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name