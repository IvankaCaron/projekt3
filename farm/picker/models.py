from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Spot(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = models.Manager()


    def __str__(self):
        return self.name