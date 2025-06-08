from django.urls import path
from . import views

urlpatterns = [
    path("",               views.PostList.as_view(),      name="post_list"),
    path("post/<int:pk>/", views.PostDetail.as_view(),    name="post_detail"),
    path("post/new/",      views.PostCreate.as_view(),    name="post_create"),
    path("author/new/",    views.AuthorCreate.as_view(),  name="author_create"),
    path("category/new/",  views.CategoryCreate.as_view(),name="category_create"),
    path("search/",        views.search_posts,            name="search_posts"),
]
