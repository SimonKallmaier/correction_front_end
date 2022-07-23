# posts/urls.py
from django.urls import path

from .views import HomePageView, CreatePostView, ImageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/", CreatePostView.as_view(), name="add_post"),
    path("<int:pk>/", ImageView.as_view(), name="image"),
]
