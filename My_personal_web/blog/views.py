from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# this will be the first page of my blog
# include the following
# my introduction
# my contract information
# my cs project
def start(request):
    return HttpResponse("hello")
