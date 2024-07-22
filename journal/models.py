from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=255)
    data = models.DateTimeField()
    img = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()

