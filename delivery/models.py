from django.db import models

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Drone(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Delivery(models.Model):
    pickup_location = models.ForeignKey(Location, related_name='pickup', on_delete=models.CASCADE)
    dropoff_location = models.ForeignKey(Location, related_name='dropoff', on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
