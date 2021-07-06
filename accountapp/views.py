from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello_world(request):                        ##request
    return render(request,'accountapp/hello_world.html')