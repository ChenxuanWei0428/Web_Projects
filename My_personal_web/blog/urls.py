from . import views
from django.urls import path

urlpatterns = [
    path("", views.start, name="Chenxuan Wei's Blog"),
    path("cooking", views.cooking, name = "My cooking recipe"),
    path("<str:name>/<str:detail>", views.message, name = "message")
]