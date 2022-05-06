from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # added

# from .models import BlogPost #added


'''
# Create your views here.
def all_blogs (request): #function added
    posts = BlogPost.objects.order_by('-post_date')
    print (type(posts))
    return render (request, 'blog/all_blogs.html', {'posts':posts})

'''


def all_shows(request):  # function added
    print ('all_shows')
    return HttpResponse("live shows")
