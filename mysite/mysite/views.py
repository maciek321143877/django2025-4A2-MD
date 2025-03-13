from django.shortcuts import render
from django.http import HttpResponse
 
def landing_page(request):
     return HttpResponse("Hello, world of polls")