
#rom django.shortcuts import renderfrom
from django.views.generic import TemplateView
from .models import Publication, AboutMe

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def  get_context_data(self, **kwargs):
      context = {
        'publication_list': Publication.objects.all()
    }
      return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
       context = {
        'about_me': AboutMe.objects.first()
       }
       return context


class PublicationView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication_list': Publication.objects.get(id=publication_pk)
        }
        return context
