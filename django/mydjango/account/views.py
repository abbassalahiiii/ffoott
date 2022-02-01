from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import ProfileForm
from .mixins import FieldsMixin, formvalidmixin, AuthorAccessMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView , CreateView , UpdateView, DeleteView
from hello.models import Article, News
from .forms import ProfileForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required
def home(request):
    return render(request, 'registration/home.html')

class ArticleList(LoginRequiredMixin, ListView):
    template_name="registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
       


class NewsList(LoginRequiredMixin, ListView):
    template_name="registration/news_list.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return News.objects.all()
        else:
            return News.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, formvalidmixin, FieldsMixin ,CreateView):
    model = Article
    template_name="registration/article-create-update.html"



class ArticleUpdate(AuthorAccessMixin, formvalidmixin, FieldsMixin ,UpdateView):
    model = Article
    template_name="registration/article-create-update.html"


class Profile(UpdateView):
    model=User
    template_name="registration/profile.html"

    fields=['username','email','first_name', 'last_name']
    success_url=reverse_lazy("account:home")
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

class News(UpdateView):
    model=News
    template_name="registration/news.html"
    fields=["title", "discriptions", "category", "slug", "publish", "status"]
    success_url=reverse_lazy("account:home")
    def get_object(self):
        pass

class ArticleDelete(DeleteView):
    model = Article
    success_url= reverse_lazy('account:home')
    template_name="registration/article_confirm_delete.html"

class PasswordChange(PasswordChangeView):
    success_url= reverse_lazy('account:password_change_done')
    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'registration/signup.html'