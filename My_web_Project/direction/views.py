from httplib2 import Http
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here
# 
# 
# .
def start(request):
    return render(request, "direction\direction.html")

def still_building(request):
    return render(request, "direction\still_building.html")







