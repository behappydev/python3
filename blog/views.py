from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Author, Category
from .forms  import PostForm, AuthorForm, CategoryForm, SearchForm

class PostList(ListView):
    model               = Post
    template_name       = "post_list.html"
    context_object_name = "posts"

class PostDetail(DetailView):
    model         = Post
    template_name = "post_detail.html"

class PostCreate(CreateView):
    model         = Post
    form_class    = PostForm
    template_name = "post_form.html"

class AuthorCreate(CreateView):
    model       = Author
    form_class  = AuthorForm
    template_name = "author_form.html"
    success_url = reverse_lazy("post_list")

class CategoryCreate(CreateView):
    model       = Category
    form_class  = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("post_list")

def search_posts(request):
    form    = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        q = form.cleaned_data["query"]
        results = Post.objects.filter(title__icontains=q)
    return render(request, "search_results.html", {"form": form, "results": results})
