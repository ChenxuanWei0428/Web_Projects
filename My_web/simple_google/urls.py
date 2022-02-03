from unicodedata import name
from django import views
from django.urls import path
from . import views
urlpatterns = [
    # this page will take take to regular search page
    path("", views.start, name="start"),
]
