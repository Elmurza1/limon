from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=255)
    data = models.DateTimeField()
    img = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()


class AboutMe(models.Model):
    i = models.TextField()
    blog = models.TextField()
    skills = models.TextField()
    project = models.TextField()
    img = models.ImageField()
    imgs = models.ImageField()
    data = models.DateField()


# class SocialNetwork(models.Model):
#     twitter =
#     linkedin
#     github
#     stack
#     codepen
