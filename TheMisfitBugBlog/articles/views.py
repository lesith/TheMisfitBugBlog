from . import forms
from . import models
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Creating an Article
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ArticleCreateView(FormView):
    form_class = forms.ArticleForm
    template_name = 'article_create.html'
    success_url = '/articles/edit/'
    def form_valid(self, form):
        form.instance.author = self.request.user    # Passing Instance User to Author
        form.save()
        return super().form_valid(form)

# Listing Articles
class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'
    paginate_by = 10  # Pagination

# Listing Featured Articles
class FeaturedArticleListView(ListView):
    model = models.Article
    template_name = 'index.html'
    paginate_by = 10  # Pagination

# Article Detailed View
class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'

# Listing Articles for Edit and Delete
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ArticleEditListView(ListView):
    model = models.Article
    template_name = 'article_edit_list.html'
    paginate_by = 10  # Pagination

# Article Update View
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ArticleUpdateView(UpdateView):
    model = models.Article
    form_class = forms.ArticleForm
    template_name = 'article_update.html'
    success_url = '/articles/edit/' # Redirect to Edit List

# Article Delete View
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = '/articles/edit/' # Redirect to Edit List