from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Http
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here
# 
# 
# .
def start(request, name):
    return render(request, "startpage\search_page.html", {
        "name": name.capitalize()
    })




