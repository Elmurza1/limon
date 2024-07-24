from django.contrib import admin
from .models import Publication, AboutMe
@admin.register(Publication)
class AdminPublication(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AboutMe)
class AdminAbout(admin.ModelAdmin):
    list_display = ['data']

