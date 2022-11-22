from django.shortcuts import render
from django.http import HttpResponse

from crawler import Fetcher

# Create your views here.
def index(request):

    #trigger the crawler on demand Parameter


    #write json data to model --> database


    #reponse to the requests
    return HttpResponse("coming to the world!")