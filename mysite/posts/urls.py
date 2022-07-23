# posts/urls.py
from django.urls import path

from .views import HomePageView, CreatePostView, ImageView, ImageViewExtracted


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/", CreatePostView.as_view(), name="add_post"),
    path("<int:pk>/", ImageView.as_view(), name="image"),
    path("<int:pk>/image_extracted/", ImageViewExtracted.as_view(), name="image_extracted"),
]
