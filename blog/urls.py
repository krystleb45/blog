from django.urls import path
from .views import (
    BlogCreateView,
    HomePageView,
    AboutPageView,
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("pages/about/", AboutPageView.as_view(), name="about"),
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/new/", BlogCreateView.as_view(), name="blog_new"),
    path("blog/<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
