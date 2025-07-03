from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world! This is my Django app.")

def homepage(request):
    return render(request, 'homepage.html')

def contact(request):
    return HttpResponse("This is the contact page of my Django app.")

def about(request):
    return HttpResponse("This is the about page of my Django app.")