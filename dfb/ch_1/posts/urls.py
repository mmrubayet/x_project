from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("read/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
]
