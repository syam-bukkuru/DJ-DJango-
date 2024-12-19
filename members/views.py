from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())
def home(request):
    return HttpResponse("Hello, we are in Home page..")

def about(request):
    return HttpResponse("Hello, we are in About page..")

def contact(request):
    return HttpResponse("Hi we are in Contact page..")