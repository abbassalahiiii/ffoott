from django.urls import path
from .views import hello,detail,categor,jadval,natij,rooznameh,Newss,Search

app_name="hello"
urlpatterns = [
    path('',hello,name="hello"),
    path('article/<slug:slug>',detail,name="detail"),
    path('category/<slug:slug>',categor,name="category"),
    path('category/<slug:slug>/page/<int:page>',categor,name="category"),
    path('jadval',jadval,name="jadval"),
    path('natayej',natij,name="natayej"),
    path('rooznameh',rooznameh,name="rooznameh"),
    path('news',Newss,name="news"),
    path('search/',Search.as_view(),name="search"),
    path('search/page/<int:slug>',Search.as_view(),name="search"),


]

