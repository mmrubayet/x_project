from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "posts/create.html"
    fields = ["title", "author", "body"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/update.html"
    fields = ["title", "body"]
