from unicodedata import name
from django import views
from django.urls import path
from . import views


app_name = "simple_google"
urlpatterns = [
    # this page will take take to regular search page
    path("", views.search, name="search"),
    path("image", views.image, name="image"),
    path("advance", views.advance, name="advance"),
]
