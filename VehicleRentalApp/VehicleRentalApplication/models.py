from django.db import models

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Vehicle_Photos")
    type = models.CharField(max_length=50)
    cost = models.IntegerField()
    availability = models.DateTimeField()
    description = models.TextField()
    
    def __str__(self):
        return self.name




class VehicleMap(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name