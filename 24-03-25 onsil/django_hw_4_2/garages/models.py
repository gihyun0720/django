from django.db import models

class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)
