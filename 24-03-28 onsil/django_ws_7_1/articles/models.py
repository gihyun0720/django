from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='media/')
    image_description = models.TextField()
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_pulic = models.BooleanField(default = True)