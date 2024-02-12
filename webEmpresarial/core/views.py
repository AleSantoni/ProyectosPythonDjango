from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

def about(request): 
   return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')


def sample(request):
    return render(request, 'core/sample.html')


# Create your views here.
