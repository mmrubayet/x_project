from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
