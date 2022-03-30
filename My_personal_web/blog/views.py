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


def cooking(request):
    return HttpResponse("cooking page")

def message(request, name, detail):
    return HttpResponse(f"The name of the message is {name} \n, message is {detail} \n")