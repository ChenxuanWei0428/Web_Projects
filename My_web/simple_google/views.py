from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Http
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here
# 
# 
# .
def start(request):
    return render(request, "simple_google\search_page.html")








