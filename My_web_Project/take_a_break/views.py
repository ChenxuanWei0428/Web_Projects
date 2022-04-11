from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Http
# Create your views here
# 
# 
# .
def search(request):
    return render(request, "take_a_break\search_page.html")

def advance(request):
    return render(request, "take_a_break/advance_search.html")

def image(request):
    return render(request, "take_a_break\image_search.html")








