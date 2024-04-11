from django.db import models

# Create your models here.

class Memo(models.Model):
    memo = models.TextField()
    summary = models.CharField(max_length=20)
    created_at = models.TimeField(auto_now=True, auto_now_add=True)
    updated_at = models.TimeField(auto_now=True, auto_now_add=True)
