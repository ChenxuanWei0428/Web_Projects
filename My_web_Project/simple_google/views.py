from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Http
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here
# 
# 
# .
def search(request):
    return render(request, "simple_google\search_page.html")

def advance(request):
    return render(request, "simple_google/advance_search.html")

def image(request):
    return render(request, "simple_google\image_search.html")








