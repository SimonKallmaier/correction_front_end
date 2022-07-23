from django.urls import path

from . import views

app_name = "correction"


urlpatterns = [
    path('', views.index, name='index'),
]
