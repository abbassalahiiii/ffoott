from django.core.paginator import Paginator
from django.db.models import Count
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from account.mixins import AuthorAccessMixin
from django.http import HttpResponse , JsonResponse
from .models import Article,category,News,Tables,Natayej,Rooznameh
from django.db.models import Q





# Create your views here.
def hello(request):

    tables_list=Tables.objects.published().order_by('-emtiaz')
    paginator = Paginator(tables_list, 20)
    page = request.GET.get('p')
    tables = paginator.get_page(page)

    news_list=News.objects.published().order_by('-publish')
    paginatorn = Paginator(news_list, 40)
    page = request.GET.get('p')
    news = paginatorn.get_page(page)

    articles_list=Article.objects.published()
    paginator = Paginator(articles_list, 10)
    page = request.GET.get('p')
    articles = paginator.get_page(page)
    
    context={
        "art":articles,
        "ne":news,
        "tables":tables,
        
    }

    return render(request,"myhtml\hello.html",context)



def detail(request,slug):
    article=get_object_or_404(Article.objects.published(),slug=slug)
   
    articles_list=Article.objects.published()
    paginator = Paginator(articles_list, 6)
    page = request.GET.get('p')
    articles = paginator.get_page(page)
    context={
        "a":article,
        "art":articles,
        
    }
    
    
    return render(request,"myhtml\detail.html",context)



def categor(request,slug):

    

    catego=get_object_or_404(category,slug=slug,status=True)

    news_list=catego.news.published().order_by('-publish')
    paginatorn = Paginator(news_list, 40)
    page = request.GET.get('p')
    news = paginatorn.get_page(page)
    
    articles_list=catego.articles.published()
    paginator = Paginator(articles_list, 10)
    page = request.GET.get('p')
    articles = paginator.get_page(page)

    tables_list=catego.tables.published().order_by('-emtiaz')
    paginator = Paginator(tables_list, 20)
    page = request.GET.get('p')
    tables = paginator.get_page(page)
    context={
         "category":catego,
          "articles": articles,
          "news":news,
          "tables":tables,
        
    }
    return render(request,"myhtml\category.html",context)
    
def natij(request):
    natayej_list=Natayej.objects.published().order_by('-publish')
    paginator = Paginator(natayej_list, 20)
    page = request.GET.get('p')
    natayej = paginator.get_page(page)
    context={
        "natayej":natayej,
    }
    return render(request,"myhtml/natijeh.html",context)

def jadval(request):
    
    tables_list=Tables.objects.published().order_by('-emtiaz','rotbeh')
    context={
        "tables":tables_list
    }
    return render(request,"myhtml\jadval2.html",context)

def Newss(request):
    news_list=News.objects.published().order_by('-publish')
    paginatorn = Paginator(news_list, 40)
    page = request.GET.get('p')
    news = paginatorn.get_page(page)
    context={
        "ne":news
    }
    return render(request,"myhtml/news.html",context)

def rooznameh(request):
    
    rooznamehha=Rooznameh.objects.published()
    context={
        "rooznam":rooznamehha
    }
    return render(request,"myhtml/rooznameh.html",context)
    
class Search(ListView):
    context_object_name="art"
    template_name='myhtml/search.html'
    def get_queryset(self):
        search=self.request.GET.get('q')
        return Article.objects.filter(Q(discriptions__icontains=search)|Q(title__icontains=search))
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['search']=self.request.GET.get('q')
        return context





