from django.contrib import admin
from .models import Publication, AboutMe, Newsletter
@admin.register(Publication)
class AdminPublication(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AboutMe)
class AdminAbout(admin.ModelAdmin):
    list_display = ['data']


@admin.register(Newsletter)
class PublicationClient(admin.ModelAdmin):
    list_display = ['email',]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False



