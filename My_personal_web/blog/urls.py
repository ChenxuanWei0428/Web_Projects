from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path("", views.intro, name="Chenxuan Wei's Blog"),
    path("cooking", views.cooking, name = "My cooking recipe"),
    path("still_building", views.still_building, name = "still_building"),
]