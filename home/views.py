from django.views import generic
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from home.models import Article, New
from home.serializer import ArticleSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class HomeView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'index.html'


class MovementDetail(generic.DetailView):
    model = Article
    context_object_name = 'movement'
    template_name = 'custom_templates.html'


class NewsList(generic.ListView):
    model = New
    context_object_name = 'news'
    template_name = 'news.html'


class NewDetail(generic.DetailView):
    model = New
    context_object_name = 'new'
    template_name = 'new.html'


class ArticleApi(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
