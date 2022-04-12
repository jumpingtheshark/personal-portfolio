from django.shortcuts import render
from django.http import HttpResponse  # added
from .models import Project


# Create your views here.

def home2(request):  # function added
    return HttpResponse("home page")



def home (request):
    projects=Project.objects.all()
    return render (request, 'folio/home.html', {'projects':projects})

def pretty (request):
    return render (request, 'folio/base.html')

