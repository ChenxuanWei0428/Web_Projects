from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# this will be the first page of my blog
# include the following
# my introduction
# my contract information
# my cs project
def intro(request):
    return render(request, "blog/intro.html")


def cooking(request):
    return HttpResponse("cooking page")

def still_building(request):
    return render(request, "blog/still_building.html")