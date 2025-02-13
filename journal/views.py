from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
#rom django.shortcuts import renderfrom
from django.views.generic import TemplateView
from .models import Publication, AboutMe, Newsletter, Category, Hashtag, PublicationComment


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def  get_context_data(self, **kwargs):
      context = {
        'publication_list': Publication.objects.filter(is_active=True)
    }
      return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
       context = {
        'about': AboutMe.objects.first()
       }
       return context


class PublicationView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication_list': Publication.objects.get(id=publication_pk),

        }
        return context

# class PublicationView(TemplateView):
#     template_name = 'publication-detail.html'
#
#     def  get_context_data(self, **kwargs):
#      blog_pk = kwargs['pk']
#
#      context = {
#         'publication_list': Publication.objects.get(id=blog_pk)
#     }
#      return context

def newsletter_email_view(request):
    print('это ваш данные от ПОСТ запроса', request.POST)

    input_email = request.POST['email']


    Newsletter.objects.create(email=input_email)
    return render(request, 'index.html')


class CreateCommentView(View):
    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = PublicationComment.objects.get(id=publication_pk)
        render(request, 'publication-detail.html', { 'publication_list': Publication.objects.get(id=publication_pk),})