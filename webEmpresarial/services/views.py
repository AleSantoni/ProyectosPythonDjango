from django.shortcuts import render

from .models import Service

# Create your views here.


def services(request):
    services = Service.objects.all()  # esto crea una lista de todos los objetos de la clase Service
    return render(request, 'services/services.html', {"services": services})