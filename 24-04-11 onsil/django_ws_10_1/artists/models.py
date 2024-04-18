from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    agency = models.TextField()
    debut_data = models.DateField(auto_now=False, auto_now_add=False)
    is_group = models.BooleanField()