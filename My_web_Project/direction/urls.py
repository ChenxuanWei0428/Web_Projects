from unicodedata import name
from django import views
from django.urls import path
from . import views

app_name = "direction"
urlpatterns = [
    path("", views.start, name="start"),
    path("still_building", views.still_building, name="still_building"),
]