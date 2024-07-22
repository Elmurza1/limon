from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class PublicationView(TemplateView):
    template_name = 'publication-detail.html'


class AboutView(TemplateView):
    template_name = 'about.html'

