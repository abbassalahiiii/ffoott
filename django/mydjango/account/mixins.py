from django.shortcuts import render, get_object_or_404
from django.http import Http404
from hello.models import Article

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
              self.fields = ["author","title","slug","category","discriptions","thunbnail","publish","status"]
        else:
              self.fields = ["title","slug","category","discriptions","thunbnail","publish"]
        return super().dispatch(request, *args, **kwargs)


class AuthorAccessMixin():
    def dispatch(self, request, pk , *args, **kwargs):
          article=get_object_or_404(Article, pk=pk)
          if article.author==request.user.is_superuser or request.user:
               return super().dispatch(request, *args, **kwargs)
          else:
               raise Http404("you can't see this page.")
        


class formvalidmixin():
      def form_valid(self, form):
            if self.request.user.is_superuser:
                  form.save()
            else:
                  self.obj=form.save(commit=False)
                  self.obj.author=self.request.user
                  self.obj.status='d'
            return super().form_valid(form)

