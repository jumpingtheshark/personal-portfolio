from django.urls import path
from . import views

app_name = 'shows'
urlpatterns = [
    path('', views.all_shows, name="all_shows")
    ]


