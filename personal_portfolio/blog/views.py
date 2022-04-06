from django.shortcuts import render
from django.http import HttpResponse  # added
from .models import BlogPost #added 


# Create your views here.


def home(request):  # function added
    return HttpResponse("blogs home page")

def all_blogs (request): #function added
    posts = BlogPost.objects.order_by('-post_date')[:5]
    print (type(posts))
    return render (request, 'blog/all_blogs.html', {'posts':posts})
     
