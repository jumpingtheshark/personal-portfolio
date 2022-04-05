from django.shortcuts import render
from django.http import HttpResponse  # added
from .models import Project


# Create your views here.
def home(request):  # function added
    return HttpResponse("home page")



def home2 (request):
    projects=Project.objects.all()
    return render (request, 'folio/home.html', {'projects':projects})
