from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello we are in Home page")

def about(request):
    return HttpResponse("Hello we are in About page..")

def contact(request):
    return HttpResponse("Hello we are in Contact page..")