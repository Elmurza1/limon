from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120, default=True)

    def __str__(self):
        return self.title

class Hashtag(models.Model):
    title = models.CharField(max_length=111)

    def __str__(self):
        return self.title

class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='publication')
    hashtags = models.ManyToManyField(Hashtag, null=True)
    title = models.CharField(max_length=255)
    data = models.DateTimeField()
    img = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)


class AboutMe(models.Model):
    description = RichTextField()
 # i = models.TextField()
    # blog = models.TextField()
    # skills = models.TextField()
    # project = models.TextField()
    img = models.ImageField(null=True)
    imgs = models.ImageField(null=True)
    data = models.DateField(null=True)


class Newsletter(models.Model):
    email = models.EmailField()




